import tkinter as tk
from tkinter import ttk, StringVar
from tkinter.filedialog import askopenfilename


class GUI():
    def __init__(self):
        self.window = tk.Tk()
        self.input_text = StringVar()
        self.filepath = ''

        self.window.title('Open file dialog')
        self.window.resizable(False, False)
        self.window.geometry('300x150')

        self.openB = tk.Button(self.window, text="Users File",command=lambda: self.open_file(), fg='blue').pack()
        self.fileEntry = tk.Entry(self.window, textvariable=self.input_text, width=70).pack(pady=5)


        self.okB =ttk.Button(self.window, text="use",
                             command=lambda: self.stop_window())

        self.window.mainloop()

    def stop_window(self):
        self.window.destroy()

    def open_file(self):
        self.filepath = askopenfilename(title='open file')
        self.input_text.set(self.filepath)


        self.okB.pack(pady=5)


    def get_path(self):
        return self.filepath


