import tkinter as tk
from tkinter import messagebox


def load(file):
    password = {}
    with open(file, "r") as f:
        for i in f.readlines():
            if i[-1] == '\n':
                i = i[:-1]
            key, val = map(str, i.split(","))
            password[key] = val
            print(i)
    return password


def loginenter(event):
    login()


def login():
    acc, pw = acct.get(), pwd.get()
    if (acc not in dic) or (dic[acc] != pw):
        messagebox.showerror(title='失败', message='登陆失败')
    else:
        messagebox.showinfo(title='成功', message='登陆成功')


def exit_esc(event):
    global wd
    wd.quit()


dic = load('data.txt')
wd = tk.Tk()
wd.title = '登录窗口'
acct, pwd = tk.StringVar(), tk.StringVar()
tk.Label(wd, text='用户名').grid(row=0, rowspan=1, column=0, columnspan=3)
acctin = tk.Entry(wd, textvariable=acct)
acctin.grid(row=0, column=3)
tk.Label(wd, text='口令').grid(row=1, rowspan=1, column=0, columnspan=3)
pwdin = tk.Entry(wd, textvariable=pwd)
pwdin.grid(row=1, column=3)
pwdin.bind('<Return>', loginenter)
tk.Button(wd, text='Login', command=login).grid(row=2, rowspan=1, column=0, columnspan=3)
tk.Button(wd, text='Quit', command=wd.quit).grid(row=2, rowspan=1, column=3, columnspan=3)
acctin.focus_force()
wd.bind('<Escape>', exit_esc)
wd.mainloop()
