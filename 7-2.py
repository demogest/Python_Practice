import tkinter as tk
from functools import partial
from tkinter import colorchooser


def ova(event):
    global sc
    canva.create_oval(event.x, event.y, event.x + 10, event.y + 10, fill=sc, outline=sc)


def eraser(event):
    global radius
    canva.create_oval(
        max(event.x - radius, 0),
        max(event.y - radius, 0),
        min(event.x + radius, 1028),
        min(event.y + radius, 720),
        fill='white',
        outline='white')


def changeToEraser():
    global canva, radius
    radius = int(ra.get())
    print(radius)
    canva.bind('<B1-Motion>', eraser)


def changeToPainter():
    global canva
    canva.bind('<B1-Motion>', ova)


def selectColor():
    global wd, canva, sc
    sc = colorchooser.askcolor(parent=wd, title="请选择颜色", color='black')[1]


def exit_esc(event):
    global wd
    wd.quit()


radius, sc = 10, 'black'
wd = tk.Tk()
wd.title('Painting using Ovals')
canva = tk.Canvas(width=1028, height=720, bg='white')
canva.grid(row=0, column=0, rowspan=3)
canva.bind('<B1-Motion>', ova)
ra = tk.StringVar()
radin = tk.Entry(wd, textvariable=ra)
radin.grid(row=1, column=2)
tk.Button(wd, text='Color', command=selectColor).grid(row=0, column=2)
tk.Button(wd, text='Painter', command=changeToPainter).grid(row=0, column=1)
tk.Button(wd, text='Eraser', command=changeToEraser).grid(row=1, column=1)
tk.Button(wd, text='Reset', command=partial(canva.delete, 'all')).grid(row=2, column=1)
wd.bind('<Escape>', exit_esc)
wd.mainloop()
