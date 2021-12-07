import tkinter as tk
from functools import partial

def rec(event):
    global a, b, item
    if a < 0 and b < 0:
        a, b = event.x, event.y
    if item is not None:
        canva.delete(item)
    lx, ly = min(a, event.x), min(b, event.y)
    rx, ry = max(a, event.x), max(b, event.y)
    item = canva.create_rectangle(lx, ly, rx, ry, dash=2)
    print(a, b, event.x, event.y)


def clr(event):
    global a, b, item
    canva.delete(item)
    lx, ly = min(a, event.x), min(b, event.y)
    rx, ry = max(a, event.x), max(b, event.y)
    item = canva.create_rectangle(lx, ly, rx, ry)
    a, b, item = -1, -1, None


a, b, item = -1, -1, None
wd = tk.Tk()
canva = tk.Canvas(width=1028, height=720, bg='white')
canva.pack()
canva.bind('<B1-Motion>', rec)
canva.bind('<ButtonRelease-1>', clr)
canva.bind('<Button-3>', partial(canva.delete,'all'))
wd.mainloop()
