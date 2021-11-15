'''
1编写一个名为draw_ rect()的函数，接收一个turtle1对象和一个Rectangle对象作为形参，并使用turt1e绘对象和一个Rectangle对象作为形参，并使用turt1e绘
并使用turtle绘制这个矩形
'''
import turtle
class Rectangle:
    def __init__(self,long,wide):
        self.long=long
        self.wide=wide
def draw_rect(rectangle):
    turtle.setup(650,350,200,200)
    turtle.fd(rectangle.long)
    turtle.seth(90)
    turtle.fd(rectangle.wide)
    turtle.seth(180)
    turtle.fd(rectangle.long)
    turtle.seth(270)
    turtle.fd(rectangle.wide)
l,w=map(int,input("请输入矩形的长与宽(a,b):").split(' '))
rectangle=Rectangle(l,w)
draw_rect(rectangle)
