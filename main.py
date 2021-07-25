'''
Author: your name
Date: 2021-07-25 23:05:19
LastEditTime: 2021-07-25 23:14:17
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \tkinter-example\main.py
'''
import tkinter as tk
# 引入字体模块
import tkinter.font as tkFont

# main function
def main():
    root = tk.Tk()
    root.geometry("600x400")
    root.title("hello")
    
    lb = tk.Label(root, text="Hello World!", font= ("华文正楷", 30), bg='gray', padx=200, pady=100)
    lb.grid()

    root.mainloop()

# main entrance
if __name__ == "__main__":
    main()