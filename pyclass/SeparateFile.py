from .FileOperation import FileOperation


class SeparateFile(FileOperation):
    def __init__(self,id, filename):
        super().__init__(id,filename)
        self.__state_list = ['read-code','read-input','read-output']
    def separate(self, textmd=''):
        if textmd != '':
            self.writeFile(textmd)
        file_readline = self.readLineFile()
        markdown = self.readFile()

        result = {'markdown': markdown}
        state = ''
        b = False
        for line in file_readline:
            if line.find('[run-option]:#') >= 0:
                b = True
                state = 'run-option'

            elif line.find('[language]:#') >= 0:
                state = 'language'

            elif line.strip() == '::startcode::':
                state = 'read-code'
                continue

            elif line.strip() == '::endcode::':
                state = 'end-code'
                continue

            elif line.find('[check-condition]:#') >= 0:
                state = 'check-condition'

            elif line.strip() == '::start-input::':
                state = 'read-input'
                continue

            elif line.strip() == '::end-input::':
                state = 'end-input'
                continue

            elif line.strip() == '::start-output::':
                state = 'read-output'
                continue

            elif line.strip() == '::end-output::':
                state = 'end-output'
                continue

            elif line.find('[check-element]:#') >= 0:
                state = 'check-element'
            
            try:
                k, v = check_line(line, state)
            except TypeError:
                pass
            else:
                if k in result:
                    v = result[k]+v
                result[k] = v
        return result


def check_line(line, state):
    if state == 'run-option':
        run_option = line.strip().replace('[run-option]:#', '').split(' ')
        return 'run_option', run_option

    elif state == 'language':
        language = line.strip().replace('[language]:#', '')
        return 'language', language

    elif state == 'read-code':
        code = line
        return 'code', code

    elif state == 'check-condition':
        check_condition = line.strip().replace(
            '[check-condition]:#', '').split(' ')
        return 'check_condition', check_condition

    elif state == 'read-input':
        input = line
        return 'input', input

    elif state == 'read-output':
        output = line
        return 'output', output

    elif state == 'check-element':
        check_element = line.strip().replace(
            '[check-element]:#', '').split(' ')
        return 'check_element', check_element
