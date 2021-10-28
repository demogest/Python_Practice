aList = []#列表初始化
aList = list(eval(input()))
if len(set(aList)) == len(aList):
    print('False')
else:
    print('True')
