from tkinter import *
from functools import partial
def cls():
    var.set('0')
def equal():
    global flag
    flag = True
    if var.get()[-1] in map(str,range(10)):
        x = eval(var.get())
        str(x)
        var.set(x)
    else:
        var.set("Wrong")
def calu(op):
    global flag
    flag = False
    var.set(var.get()+op)
def set_point():
    s = var.get() + '.'
    var.set(s)
def setNum(num):
    global flag
    if var.get() =='0' or flag:
        flag = False
        var.set(str(num))
    else:
        s = var.get() + str(num)
        var.set(s)
def createButton(root,text,command,row,column,columnspan=1,wi=10):
    Button(root,text=text,command=command,width=wi,height=2).grid(row=row,column=column,columnspan=columnspan)
root = Tk()
root.title('计算器')
root.geometry('320x500')
flag = False
var = StringVar()
var.set('0')
entry = Entry(root, textvariable=var)
entry.pack(fill=X)
frame_2 = Frame(root)
cal = ['+','-','*','/']
for i in range(1,4):
    for j in range(1,4):
        createButton(frame_2,str((3-i)*3+j),partial(setNum,(3-i)*3+j),i-1,j-1)
createButton(frame_2,"0",set[0],3,0)
for i in range(4):
    createButton(frame_2,cal[i],partial(calu,cal[i]),i,3)
createButton(frame_2,'.',set_point,3,1)
createButton(frame_2,"=",equal,3,2)
frame_2.pack()
root.mainloop()
