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

if __name__ == "__main__":
    main()