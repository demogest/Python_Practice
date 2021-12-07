import tkinter as tk
from tkinter import messagebox


def load(file):
    dic = {}
    with open(file, "r") as f:
        for i in f.readlines():
            if i[-1] == '\n':
                i = i[:-1]
            key, val = map(str, i.split(" "))
            dic[key] = val
            print(i)
    return dic


def login():
    acc, pw = acct.get(), pwd.get()
    if (acc not in dic) or (dic[acc] != pw):
        messagebox.showerror(title='失败', message='登陆失败')
    else:
        messagebox.showinfo(title='成功', message='登陆成功')


dic = load('data.txt')
wd = tk.Tk()
wd.title = '登录窗口'
acct, pwd = tk.StringVar(), tk.StringVar()
tk.Label(wd, text='用户名').grid(row=0, rowspan=1, column=0, columnspan=3)
tk.Entry(wd, textvariable=acct).grid(row=0, column=3)
tk.Label(wd, text='口令').grid(row=1, rowspan=1, column=0, columnspan=3)
tk.Entry(wd, textvariable=pwd).grid(row=1, column=3)
tk.Button(wd, text='Login', command=login).grid(row=2, rowspan=1, column=0, columnspan=3)
tk.Button(wd, text='Quit', command=wd.destroy).grid(row=2, rowspan=1, column=3, columnspan=3)
wd.mainloop()
