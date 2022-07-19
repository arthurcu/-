#
# @Time     : 2022/07/19 0:27
# @Author   : Dragon.G
# @File     : table.py
import ttkbootstrap as ttk
import tkinter as tk
from dealwithdata import deal_with_data


class Table:
    def __init__(self, root, original_data):
        self.yscroll = None
        self.original_data = original_data
        self.root = root
        self.tree_view = None
        self.table_page = ttk.Frame(self.root)
        self.table_page.pack()
        self.create_page()

    def create_page(self):
        columns = (
            'course_term', 'course_name', 'course_mark', 'course_credit', 'course_type', 'mark_type')
        columns_values = ('学期', '课程名称', '分数', '学分', '课程类型', '考试类型')
        self.yscroll = tk.Scrollbar(self.root, orient=ttk.VERTICAL)
        self.tree_view = ttk.Treeview(self.root, show='headings', columns=columns, yscrollcommand=self.yscroll.set)
        self.tree_view.column('course_term', width=120, anchor='center')
        self.tree_view.column('course_name', width=300, anchor='center')
        self.tree_view.column('course_mark', width=120, anchor='center')
        self.tree_view.column('course_credit', width=120, anchor='center')
        self.tree_view.column('course_type', width=200, anchor='center')
        self.tree_view.column('mark_type', width=180, anchor='center')
        self.tree_view.heading('course_term', text='学期')
        self.tree_view.heading('course_name', text='课程名称')
        self.tree_view.heading('course_mark', text='分数')
        self.tree_view.heading('course_credit', text='学分')
        self.tree_view.heading('course_type', text='课程类型')
        self.tree_view.heading('mark_type', text='考试类型')
        self.tree_view.pack( fill=ttk.Y)
        self.show_data_frame()

    def show_data_frame(self):
        for _ in map(self.tree_view.delete, self.tree_view.get_children('')):
            pass
        data = deal_with_data(self.original_data)
        index = 0
        for item in data:
            self.tree_view.insert('', index + 1, values=(
                item['course_term'], item['course_name'], item['course_mark'], item['course_credit'],
                item['course_type'], item['mark_type']
            ))
