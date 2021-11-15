name = input("please enter the name of source file：")
if name[-3:] != '.py':
    name += '.py'
txt = open(name,encoding='utf-8').read()
txt = txt.lower()
txt = txt.replace("'"," ")
for i in txt:
    if not i.isalpha():
        txt = txt.replace(i," ")
words = txt.split(" ")
words = [i for i in words if i != '']
key = ['int', 'False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
dic = {}
for i in key:
    dic[i] = 0
for i in words:
    if i in key:
        dic[i] += 1
for i in dic:
    print('{}:{}'.format(i,dic[i]))
