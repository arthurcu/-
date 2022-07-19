#
# @Time     : 2022/07/17 20:25
# @Author   : Dragon.G
# @File     : mainpage.py
import tkinter as tk
import ttkbootstrap as ttk
from table import Table


class Mainpage:
    def __init__(self, master, original_data):
        self.original_data = original_data
        self.mark_frame = None
        self.about_frame = None
        self.root = master
        self.create_page()
        self.show_mark()

    def create_page(self):
        self.about_page()
        self.mark_page()
        menubar = ttk.Menu(self.root)
        menubar.add_command(label='成绩显示', command=self.show_mark)
        menubar.add_command(label='关于', command=self.show_about)
        self.root['menu'] = menubar

    def about_page(self):
        self.about_frame = ttk.Frame(self.root)
        ttk.Label(self.about_frame, text='版本号:V 0.0.1').pack()
        ttk.Label(self.about_frame, text='关于作者:ArthurCU').pack()

    def show_about(self):
        self.mark_frame.pack_forget()
        self.about_frame.pack()

    def mark_page(self):
        self.mark_frame = ttk.Frame(self.root)
        Table(self.mark_frame, self.original_data)

    def show_mark(self):
        self.about_frame.pack_forget()
        self.mark_frame.pack()


if __name__ == '__main__':
    root = ttk.Window()
    Mainpage(root)
    root.mainloop()
