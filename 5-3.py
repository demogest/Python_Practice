class Contact:
    def __init__(self,name:str,num:str):
        self.__name = name
        self.__num = num
    def setName(self,name:str):
        self.__name = name
    def setPhone(self,num:str):
        self.__num = num
    def getPhone(self):
        return self.__num
    def getName(self):
        return self.__name
class Phonebook:
    def __init__(self,person:list):
        self.__dict = {}
        for i in person:
            self.__dict[i.getName()] = i.getPhone()
    def setByName(self,name:str,num:str):
        self.__dict[name] = num
        print('修改后,{}的电话号码为{}'.format(name,self.__dict[name]))
    def findByName(self,name:str):
        return self.__dict.get(name)
    def countByfir(self,lett:str):
        cnt = 0
        for i in self.__dict.keys():
            if i[0] == lett:
                cnt+=1
        return cnt
    def totContact(self):
        return len(self.__dict)
if __name__=='__main__':
    li = list(input().split(','))
    contacts = [li[i:i+2] for i in range(0, len(li), 2)]
    people =[]
    for i in contacts:
        people.append(Contact(i[0],i[1]))
    book = Phonebook(people)
    for i in people:
        print(i.getName(),end=',')
        print(i.getPhone())
    book.setByName('mary','13698765432')
    num = book.findByName('peter')
    if num != None:
        print('经过查找,peter的电话号码为{}'.format(num))
    print('通讯录中总共有{}条联系人信息'.format(book.totContact()))
    print('通讯录中姓名以m字符开始的联系人有{}条'.format(book.countByfir('m')))
    
