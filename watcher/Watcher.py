"""
Python实现功能，
1、第一行展示：在输入框输入若干进程名，逗号分隔，如：WeLink.exe,WeLinkPC.exe；点击按钮B，执行功能3
2、第二行为一个表格，展示功能3的结果
3、点击按钮B后，每隔5秒获取输入进程的进程名、PID、CPU利用率、内存使用量，若存在同名进程，全部分行打印
4、用pack布局
"""
import ctypes
import tkinter as tk
from tkinter import ttk
import psutil
import threading
import win32con
import win32process

def get_process_info(process_names):
    process_info = []
    for proc in psutil.process_iter(['name', 'pid', 'cpu_percent', 'memory_info', 'num_handles']):
        if proc.info['name'] in process_names:
            p = psutil.Process(pid=proc.info['pid'])
            process_handle = ctypes.windll.kernel32.OpenProcess(
                ctypes.c_uint(0x0400 | 0x0010), ctypes.c_bool(False), ctypes.c_uint(proc.info['pid'])
            )
            gdi_count = win32process.GetGuiResources(process_handle, win32con.GR_GDIOBJECTS)
            process_info.append((proc.info['name'],
                                 proc.info['pid'],
                                 proc.info['cpu_percent'],
                                 round(p.memory_full_info().uss/1024/1024, 2),
                                 proc.info['num_handles'],
                                 gdi_count
                                 ))
    return process_info


def update_table():
    process_names = input_entry.get().split(',')
    process_info = get_process_info(process_names)
    table.delete(*table.get_children())

    # 计算列之和
    cpu_sum = 0
    memory_sum = 0
    handle_sum = 0
    gdi_sum = 0
    for info in process_info:
        cpu_sum += info[2]
        memory_sum += info[3]
        handle_sum += info[4]
        gdi_sum += info[4]

    # 在第一行打印列之和
    table.insert('', 'end', values=["总计", "-", round(cpu_sum, 2), round(memory_sum, 2), round(handle_sum, 2), round(gdi_sum, 2)])

    for info in process_info:
        table.insert('', 'end', values=info)

    root.after(5000, update_table)

# 复制单个表格
def copy_cell_text(event):
    selected_item = table.focus()
    if selected_item:
        column = table.identify_column(event.x)
        row = table.identify_row(event.y)
        cell_value = table.set(selected_item, column)
        root.clipboard_clear()
        root.clipboard_append(cell_value)

# 复制整行
def copy_selection():
    selected_items = table.selection()
    if selected_items:
        content = ''
        for item in selected_items:
            values = table.item(item)['values']
            content += '\t'.join(str(value) for value in values) + '\n'
        root.clipboard_clear()
        root.clipboard_append(content)

def on_button_click():
    threading.Thread(target=update_table).start()


root = tk.Tk()
root.title("进程信息展示 | 输入进程名(,分隔) | 点击数值复制")
root.geometry("600x400")
root.wm_attributes('-topmost', 1)

# 输入框和按钮
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

input_label = tk.Label(input_frame, text="输入进程名(,分隔)：", font=('Microsoft YaHei', 15))
input_label.pack(side='left')

input_entry = tk.Entry(input_frame, width=20, font=('Microsoft YaHei', 15))
input_entry.pack(side='left')

zlabel = tk.Label(input_frame, text="   ")
zlabel.pack(side='left')

button = tk.Button(input_frame, text="执行功能3", command=on_button_click, font=('Microsoft YaHei', 10))
button.pack(side='left')

# 表格
columns = ("进程名", "PID", "CPU利用率", "内存使用量", "句柄", "GDI")
table = ttk.Treeview(root, columns=columns, show='headings')
for col in columns:
    table.heading(col, text=col)
    table.column(col, width=70)
table.pack(fill="both", expand=True)
table.bind("<Button-1>", copy_cell_text)

input_frame2 = tk.Frame(root)
input_frame2.pack(pady=10)
copy_button = tk.Button(input_frame2, text="复制整行", command=copy_selection)
copy_button.pack()

root.mainloop()
