'''
2编写程序，定义有理数类,并且创建两个实例，完成有理数的相加、相乘.(相减、相除选做)
'''
class raNum:
    def __init__(self,number:int):
        self.__number=number
    def getNum(self) -> int:
        return self.__number
    def plus(self,another) -> int:
        return self.__number + another.__number
    def multiply(self,another) -> int:
        return self.__number * another.__number
    def sub(self,another) -> int:
        return self.__number - another.__number
    def div(self,another) -> float:
        return self.__number / another.__number
a,b=map(int,input("请输入两个有理数(a,b)：").split(' '))
num1=raNum(a)
num2=raNum(b)
print("加法:{}\n数乘:{}\n减法:{}\n除法:{}\n".\
      format(num1.multiply(num2),num1.plus(num2),num1.sub(num2),num1.div(num2)))


