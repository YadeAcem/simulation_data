import pandas as pb
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import *
from tkinter import ttk


def read_file(file):
    my_column = 'Ctrl_C1_Treatment_TR1_AR1'
    my_2column = 'Pat_P1_Treatment_TR1_AR1'
    df = pb.read_excel(file, sheet_name='AnalyticalReps')
    header = df.columns.tolist()
    x1 = df[[my_column]]
    x = np.array(df[[my_column]])
    y = np.array(df[[my_2column]])
    # print(x1.to_string())

    # plt.bar(x, y)
    # plt.show()



    # print(header)


    # print(header[0:7])
    # print(df.iloc[0])
    # print(df.head())
    # df.plot(kind ='hist' )
    # plt.show()

class GUI:
    def __init__(self):
        # maakt de window
        self.root = tk.Tk()
        self.root.title('Simulation data')
        self.root.iconphoto(False, tk.PhotoImage(file='UMC.icns'))
        self.root.geometry('500x500')

        # tabs
        self.my_notebook = ttk.Notebook(self.root)
        self.my_notebook.pack()

        # 2 frame top en bottum
        self.frame1 = tk.Frame(self.my_notebook, width=500, height=500, bg='blue')
        self.frame2 = tk.Frame(self.my_notebook, width=500, height=500, bg='red')
        # label
        self.label1 = tk.Label(self.frame1, text='settings')
        self.label2 = tk.Label(self.frame1, text='which columns would you like to see?')
        self.label3 = tk.Label(self.frame1, text='STILL WORK IN PROGRESS')



        # self.input = tk.Entry()


        # pack elements
        self.frame1.pack(fill='both', expand=1)
        self.frame2.pack(fill='both', expand=1)
        self.label1.pack()
        self.label2.pack()
        self.label3.pack()
        self.my_notebook.add(self.frame1, text='Targeted')
        self.my_notebook.add(self.frame2, text='Holistic')

        # self.input.pack()

        # show Gui
        tk.mainloop()


if __name__ == '__main__':
    My_Gui = GUI()
    simulation_data = 'Simulation_HeartProteomics_20230914.xlsx'
    read_file(simulation_data)




    # .loc[[2]] laat bv alleen rij 2 zien
    # .head(10) laat de eerste 10 rijen zien
    # .string print alles