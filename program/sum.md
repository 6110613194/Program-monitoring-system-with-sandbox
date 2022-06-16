[run-option]:#time=10 mem=10240 filename=printnum
[language]:#py
::startcode::
sum = 0
for i in range(11):
    sum = sum + i
print("Sum =",sum)
::endcode::
[check-condition]:#exact-macth ignore-space
::start-output::
Sum = 55
::end-output::
[check-element]:#for print