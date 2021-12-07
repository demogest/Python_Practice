"""
2编写程序，定义有理数类,并且创建两个实例，完

成有理数的相加、相乘.(相减、相除选做)
"""
from decimal import *


class raNum:
    def __init__(self, number: Decimal):
        self.__number = number

    def __repr__(self):
        return str(self.__number)

    def __add__(self, other):
        return raNum(self.__number + other.__number)

    def __sub__(self, other):
        return raNum(self.__number - other.__number)

    def __mul__(self, other):
        return raNum(self.__number * other.__number)

    def __truediv__(self, other):
        return raNum(self.__number / other.__number)


a, b = map(raNum, map(Decimal, input("请输入两个有理数(a,b)：").split(' ')))
print("加法:{}\n数乘:{}\n减法:{}\n除法:{}\n"
      .format(a + b, a - b, a * b, a / b))
