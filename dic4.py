def listall(book:dict):
    if not book:
        print('Empty')
    for i in book:
        print(i)

def addone(book:dict):
    name = input('Name:')
    author = input('Author:')
    content = input('Content:')
    if name not in book:
        book[name] = [author,content]
        return 0
    print('Existed')
    return -1
def delone(book:dict):
    name = input('Name:')
    if name in book:
        del book[name]
        return 0
    print("Not found")
    return -1

def findone(book:dict):
    name = input('Name:')
    if name in book:
        print('result is:\nAuthor:{}\nContent:{}'.format(book[name][0],book[name][1]))
        return 0
    print('Not found')
    return -1

book = {}
fun = {'list':listall,'add':addone,'del':delone,'find':findone}
while True:
    com =input("Command(list,add,del,find,exit):")
    if com == 'exit':
        break
    if com in fun:
        fun[com](book)

    
