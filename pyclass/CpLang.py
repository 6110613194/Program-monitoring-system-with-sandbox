from pyclass.FileOperation import FileOperation
import os


def python(id,cp_run):
    os.system(cp_run)
    metafile = FileOperation(str(id), 'meta.txt')
    metafile.readFile()
    outfile = FileOperation(str(id), 'out.txt')
    outfile.readFile()
    errfile = FileOperation(str(id), 'err.txt')
    errfile.readFile()
    a = metafile.readFile().strip().split('\n')
    d = dict(s.split(':') for s in a)
    if d.get('status') == 'RE':
        return False,errfile.readFile()
    elif d.get('status') == 'SG':
        return False,'Program died on Signal. Try to change option'
    elif d.get('status') == 'TO':
        return False,'Time out!'
    elif d.get('status') == 'XX':
        return False,'Internal error of the sandbox'
    else:
        return True,outfile.readFile()

def java(id,cp,run):
    os.system(cp)
    metafile_cp = FileOperation(str(id), 'meta.txt')
    metafile_cp.readFile()
    errfile_cp = FileOperation(str(id), 'err.txt')
    errfile_cp.readFile()
    listmeta_cp = metafile_cp.readFile().strip().split('\n')
    d_cp = dict(s.split(':') for s in listmeta_cp)
    if d_cp.get('status') == 'RE':
        return False,errfile_cp.readFile()
    elif d_cp.get('status') == 'SG':
        return False,'Program died on Signal. Try to change option'
    elif d_cp.get('status') == 'TO':
        return False,'Time out!'
    elif d_cp.get('status') == 'XX':
        return False,'Internal error of the sandbox'
    else:
        os.system(run)
        metafile_run = FileOperation(str(id), 'meta.txt')
        metafile_run.readFile()
        outfile_run = FileOperation(str(id), 'out.txt')
        outfile_run.readFile()
        errfile_run = FileOperation(str(id), 'err.txt')
        errfile_run.readFile()
        listmeta_run = metafile_run.readFile().strip().split('\n')
        d_run = dict(s.split(':') for s in listmeta_run)
        if d_run.get('status') == 'RE':
            return False,errfile_run.readFile()
        elif d_run.get('status') == 'SG':
            return False,'Program died on Signal. Try to change option. Eg. Increase mem.'
        elif d_run.get('status') == 'TO':
            return False,'Time out!'
        elif d_run.get('status') == 'XX':
            return False,'Internal error of the sandbox'
        else:
            return True,outfile_run.readFile()