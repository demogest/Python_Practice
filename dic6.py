import random
def listall(book:dict):
    if not book:
        print('Empty')
    for i in book:
        print(i)
def setone(book:dict):
    eng = input('Eng:')
    ch = input('Ch:')
    book[eng] = ch
    return 0
def delone(book:dict):
    eng = input('Eng:')
    if name in book:
        del book[eng]
        return 0
    print("Not found")
    return -1
def findByEng(book:dict):
    eng = input('Eng:')
    if eng in book:
        print('result is:{}'.format(book[eng]))
        return 0
    print('Not found')
    return -1
def findByCh(book:dict):
    ch = input('Ch:')
    if ch in book.values():
        print('result is:{}'.format(list(book.keys())[list(book.values()).index(ch)]))
        return 0
    print('Not found')
    return -1
def randEn(book:dict):
    if book:
        eng = random.choice(list(book.keys()))
        ch = input('{}:'.format(eng))
        if ch == book[eng]:
            print("Right")
        else:
            print('Wrong')
        return 0
    return -1
book = {}
fun = {'list':listall,'set':setone,'del':delone,'finde':findByEng,'findc':findByCh,'random':randEn}
while True:
    com =input("Command(list,set,del,finde,findc,random,exit):")
    if com in fun:
        fun[com](book)
    if com == 'exit':
        break
