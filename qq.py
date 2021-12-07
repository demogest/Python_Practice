import tkinter as tk
import tkinter.font as ft
from tkinter import messagebox


def sh():
    messagebox.showinfo('Pass', ps.get())


wd = tk.Tk()
#wd.geometry('480x320+10+10')
# ima = Image.open('gg.png').transpose(Image.ROTATE_90)
# # ima = ima.resize((324//2,115//2))
# qq = ImageTk.PhotoImage(ima)
ftf = ft.Font(weight="bold", size=15)
# prof = tk.Canvas(wd)
la = tk.Frame(wd, width=480, height=100, bg='#3366ff')
la.grid(row=0)
lb = tk.Frame(wd, width=480, height=220, bg='pink')
tk.Frame(wd, width=480, height=40, bg='pink').grid(row=1)
lb.grid(row=2)


# tk.Frame(lb, width=480, height=40).grid(row=0)
# conf = tk.Frame(lb,width)
tk.Label(lb, text='密码', font=ftf).grid(row=1, column=0, sticky='w', columnspan=1)
ps = tk.Entry(lb, show='*')
ps.grid(row=1, column=1, sticky='w')
tk.Label(lb, text='账号', font=ftf).grid(row=0, padx=0, pady=0, sticky='w', columnspan=1)
ac = tk.Entry(lb)
ac.grid(row=0, column=1, sticky='w')
tk.Button(lb, command=sh, text='登录', font=ftf).grid(row=3, column=1)
wd.title("腾讯QQ")
wd.iconbitmap("qq_logo_icon_206694.ico")
wd.mainloop()
