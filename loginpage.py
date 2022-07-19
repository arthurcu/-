#
# @Time     : 2022/07/16 21:56
# @Author   : Dragon.G
# @File     : loginpage.py
import tkinter as tk
import ttkbootstrap as ttk
from getdata import get_data, judge_data
from tkinter import messagebox
from mainpage import Mainpage
from ttkbootstrap.constants import *


class Loginpage:
    def __init__(self):
        self.data = None
        self.password = None
        self.username = None
        self.width = 300
        self.height = 180
        self.root = ttk.Window()
        self.usernamevar = tk.StringVar()
        self.passwordvar = tk.StringVar()
        self.root.iconbitmap('logo.ico')
        self.init_geometry()
        self.root.resizable(False, False)
        self.root.title('常大查分助手')
        self.lp = ttk.Frame(self.root)
        self.add_assembly()
        self.lp.pack()
        self.add_assembly()
        self.root.mainloop()

    def init_geometry(self):
        self.root.geometry(
            '{}x{}+{}+{}'.format(self.width, self.height, int(self.get_screensize()[0] / 2 - self.width / 2),
                                 int(self.get_screensize()[1] / 2 - self.height / 2 - 50)))

    def add_assembly(self):
        ttk.Label(self.lp).grid(row=0, column=0)
        ttk.Label(self.lp, text='账号: ').grid(row=1, column=0)
        ttk.Entry(self.lp, textvariable=self.usernamevar).grid(row=1, column=1)
        ttk.Label(self.lp).grid(row=2, column=0)
        ttk.Label(self.lp, text='密码: ').grid(row=3, column=0)
        ttk.Entry(self.lp, textvariable=self.passwordvar, show='*').grid(row=3, column=1)
        ttk.Label(self.lp).grid(row=4, column=0)
        ttk.Button(self.lp, text='查询', width=7, command=self.click_login).grid(row=5, column=1)

    def get_screensize(self):
        sw, sh = self.root.maxsize()
        return sw, sh

    def click_login(self):
        self.username = self.usernamevar.get()
        self.password = self.passwordvar.get()
        self.data = get_data(username=self.username, password=self.password)
        flag, text = judge_data(self.data)
        if flag == 1:
            self.width = 1200
            self.height = 700
            self.init_geometry()
            self.lp.destroy()
            self.root.withdraw()
            Mainpage(self.root, self.data.text)
            self.root.deiconify()
        else:
            tk.messagebox.showwarning(title='警告', message=text)



if __name__ == '__main__':
    Loginpage()
