# coding:utf-8
from func.Conet import *
import tkinter as tk
from PIL import ImageTk

_: int = 0

# 创建窗口
window = tk.Tk()
window.resizable(False, False)
window.title('A.U.A for {6-4}')


# 创建储存图片的类
class imgs():
    bg = ImageTk.PhotoImage(file='img/A.U.A icon.png')
    settings_img = ImageTk.PhotoImage(file='img/A.U.A Settings icon.png')


class label():
    bgLabel = tk.Label(window, width=696, height=566, image=imgs.bg)
    settings_imgBtn = tk.Button(window, image=imgs.settings_img, bd=0)


# 定义显示方法
def show():
    label.bgLabel.pack()
    label.settings_imgBtn.place(x=655, y=2)


# 调用显示方法
show()

tk.mainloop()
