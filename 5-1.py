class Account:
   def __init__(self,li:list):
      self.__aid = li[0]
      self.__pwd = li[1]
      self.__bal = li[2]
   def show(self):
      print("账号:"+self.__aid)
      print("密码:"+self.__pwd)
      print("余额:"+str(self.__bal))
   def deposit(self,num:int):
      self.__bal += num
   def withdrawal(self,num):
      self.__bal -= num
if __name__ == '__main__':
   li=list(input().split(','))
   li[2] = int(li[2])
   a = Account(li)
   a.show()
