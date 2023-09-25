import pandas as pb
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk, font
from tkinter import messagebox
from functools import partial
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)

from matplotlib import *


class GUI:
    def __init__(self):
        # list with cellijn
        self.options = list_cel
        self.options2 = listP_cel
        self.behand_list = list_VT
        self.tech_r = list_TR
        self.analy_r = list_AR
        self.column1_list =[]
        self.column2_list=[]
        self.file_name1 = ''
        self.file_name2 = ''
        self.df = df

        # maakt de window
        self.root = tk.Tk()

        # Creating a Font object of "TkDefaultFont"
        self.defaultFont = font.nametofont('TkDefaultFont')

        # Overriding default-font with custom settings
        # i.e changing font-family, size and weight
        self.defaultFont.configure(family='Inconsolata', size=15,
                                   weight=font.BOLD)

        # window bg
        # self.root.configure(background='#696969')

        # window size
        self.root.geometry('750x750')

        # window title
        self.root.title('Simulation data')

        # logo icon
        self.root.iconphoto(False, tk.PhotoImage(file='UMC.icns'))

        # tabs
        self.my_notebook = ttk.Notebook(self.root, width=750,
                                        height=650, )
        self.my_notebook.pack()

        # frames voor de tabs > targeted en holistic
        self.frame1 = tk.Frame(self.my_notebook, bg='grey')
        self.frame2 = tk.Frame(self.my_notebook, bg='red')

        # buttom frame for quit button
        self.bottom_frame = tk.Frame(self.root)

        # label for the tabs
        self.label1 = tk.Label(self.frame1, text='Settings', bg='grey')

        # self.label2 = tk.Label(self.frame1, text='which columns would
        # you like to see?',bg='grey')
        self.label3 = tk.Label(self.frame2,
                               text='Still work in progress', bg='red')

        # option frames for in frame1
        self.column = tk.LabelFrame(self.frame1, width=200, height=500,
                                    bg='light grey', text='Column 1')

        self.column2 = tk.LabelFrame(self.frame1, width=200, height=500,
                                     bg='light grey', text='Column 2')
        self.graph = tk.LabelFrame(self.frame1, width=200, height=500,
                                   bg='light grey', text='Graph')

        # buttons main page
        self.quit_but = tk.Button(self.bottom_frame, text='quit',
                                  fg='red', command=self.root.destroy)
        self.ok_but = tk.Button(self.bottom_frame, text='ok',
                                fg='green', command=self.graphs)
        self.analyse_but = tk.Button(self.bottom_frame, text='analyse',
                                     fg='blue', command=self.get_input)

        #
        # # intvar objecten voor de check buttons
        # self.cb_varC = tk.IntVar()
        # self.cb_varP = tk.IntVar()
        #
        # # zet de intvar objecten op 0
        # self.cb_varC.set(0)
        # self.cb_varP.set(0)

        self.BC = tk.Button(self.column, text='Control', font=10,
                            command=partial(self.new_options, "c"))
        self.BP = tk.Button(self.column, text='Patient', font=10,
                            command=partial(self.new_options, "p"))

        self.BC2 = tk.Button(self.column2, text='Control', font=10,
                            command=partial(self.new_options2, "c"))
        self.BP2 = tk.Button(self.column2, text='Patient', font=10,
                            command=partial(self.new_options2, "p"))
        self.graphB = tk.Button(self.graph, text='show graph', font=10,
                                command=self.scatter)


        # self.input = tk.Entry()

        # pack elements
        self.frame1.pack(fill='both', expand=1)
        self.frame2.pack(fill='both', expand=1)
        self.bottom_frame.pack()

        self.label1.pack()
        # self.label2.pack()
        self.label3.pack(pady=50)

        self.my_notebook.add(self.frame1, text='Targeted')
        self.my_notebook.add(self.frame2, text='Holistic')

        self.quit_but.pack(side='left')
        self.ok_but.pack(side='left')
        self.analyse_but.pack(side='left')

        self.column.pack(side='left', padx=15)
        self.column.pack_propagate(False)
        self.column.grid_propagate(False)

        self.column2.pack(side='left', padx=15)
        self.column2.pack_propagate(False)
        self.column2.grid_propagate(False)

        self.graph.pack(side='left', padx=15)
        self.graph.pack_propagate(False)
        self.graph.grid_propagate(False)

        # buttons for the first column options
        self.BC.place(x=45, y=20)
        self.BC.configure(highlightbackground='light grey')

        self.BP.place(x=100, y=20)
        self.BP.configure(highlightbackground='light grey')

        # buttons for the second column options
        self.BC2.place(x=45, y=20)
        self.BC2.configure(highlightbackground='light grey')

        self.BP2.place(x=100, y=20)
        self.BP2.configure(highlightbackground='light grey')

        self.graphB.place(x=100, y=20)
        self.graphB.configure(highlightbackground='light grey')



        """menu after control or patient is pressed for column1 """
        # new column frame when pressed
        self.name = tk.LabelFrame(self.column, width=200, height=450,
                                  bg='light grey', text='options')
        self.name.grid_propagate(False)

        # drop down menu
        self.clicked = tk.StringVar()
        self.clicked.set('choose cellijn')
        self.cellijn = tk.OptionMenu(self.name, self.clicked,
                                     *self.options)
        self.cellijn.configure(font=10, bg='light grey')

        # dropdown 2
        self.cellijn2 = tk.OptionMenu(self.name, self.clicked,
                                      *self.options2)
        self.cellijn2.configure(font=10, bg='light grey')

        # Vehicle & Treatment dropdown
        self.clicked2 = tk.StringVar()
        self.clicked2.set('choose treatment')
        self.behandeling = tk.OptionMenu(self.name, self.clicked2,
                                         *self.behand_list)
        self.behandeling.configure(font=10, bg='light grey')

        # Tr1 or Tr2 dropdown.
        self.clicked3 = tk.StringVar()
        self.clicked3.set('choose technical rep')
        self.which_tr = tk.OptionMenu(self.name, self.clicked3,
                                      *self.tech_r)
        self.which_tr.configure(font=10, bg='light grey')

        # AR 1,2,3,4,5
        self.clicked4 = tk.StringVar()
        self.clicked4.set('choose analy rep')
        self.which_ar = tk.OptionMenu(self.name, self.clicked4,
                                      *self.analy_r)
        self.which_ar.configure(font=10, bg='light grey')


        """menu after control or patient is pressed for column2 """
        # new column frame when pressed
        self.name2 = tk.LabelFrame(self.column2, width=200, height=450,
                                  bg='light grey', text='options')
        self.name2.grid_propagate(False)

        # drop down menu
        self.click = tk.StringVar()
        self.click.set('choose cellijn')
        self.cel = tk.OptionMenu(self.name2, self.click,
                                     *self.options)
        self.cel.configure(font=10, bg='light grey')

        # dropdown 2
        self.cel2 = tk.OptionMenu(self.name2, self.click,
                                      *self.options2)
        self.cel2.configure(font=10, bg='light grey')

        # Vehicle & Treatment dropdown
        self.click2 = tk.StringVar()
        self.click2.set('choose treatment')
        self.behandeling2 = tk.OptionMenu(self.name2, self.click2,
                                         *self.behand_list)
        self.behandeling2.configure(font=10, bg='light grey')

        # Tr1 or Tr2 dropdown.
        self.click3 = tk.StringVar()
        self.click3.set('choose technical rep')
        self.which_tr2 = tk.OptionMenu(self.name2, self.click3,
                                      *self.tech_r)
        self.which_tr2.configure(font=10, bg='light grey')

        # AR 1,2,3,4,5
        self.click4 = tk.StringVar()
        self.click4.set('choose analy rep')
        self.which_ar2 = tk.OptionMenu(self.name2, self.click4,
                                      *self.analy_r)
        self.which_ar2.configure(font=10, bg='light grey')


        # show Gui
        tk.mainloop()

    # def opt(self,func):
    #     if func == 'c':
    #         self.new_optionsC()
    #     else:
    #         self.new_optionsP()

    def new_options(self, func):
        self.BC.destroy()
        self.BP.destroy()
        self.name.pack(side='left', padx=10)
        self.name.pack_propagate(False)

        if func == 'c':
            self.column1_list.append('Ctrl')
            self.cellijn.place(x=10, y=10)
        else:
            self.column1_list.append('Pat')
            self.cellijn2.place(x=10, y=10)

        self.behandeling.place(x=10, y=50)
        self.which_tr.place(x=10, y=90)
        self.which_ar.place(x=10, y=130)

    def new_options2(self, func2):
        self.BC2.destroy()
        self.BP2.destroy()
        self.name2.pack(side='left', padx=10)
        self.name2.pack_propagate(False)

        if func2 == 'c':
            self.column2_list.append('Ctrl')
            self.cel.place(x=10, y=10)
        else:
            self.column2_list.append('Pat')
            self.cel2.place(x=10, y=10)

        self.behandeling2.place(x=10, y=50)
        self.which_tr2.place(x=10, y=90)
        self.which_ar2.place(x=10, y=130)


    def graphs(self):
        tk.messagebox.showinfo('selection', 'loading')

    def get_input(self):
        self.column1_list.extend([self.clicked.get(), self.clicked2.get(),
                             self.clicked3.get(), self.clicked4.get()])
        # print(f"[{', '.join(column1_list)}]")

        self.column2_list.extend([self.click.get(), self.click2.get(),
                             self.click3.get(), self.click4.get()])
        # print(f"[{', '.join(column2_list)}]")

        # return column1_list, column2_list
        self.file_name1 = "_".join([str(item) for item in self.column1_list])
        self.file_name2 = "_".join([str(item) for item in self.column2_list])

        # self.read_file(simulation_data)
        print('column 1 is: ',self.file_name1)
        print('column 2 is: ',self.file_name2)

        return self.file_name1, self.file_name2

    # def read_file(self,file):
    #     self.df = pb.read_excel(file, sheet_name='AnalyticalReps')

        # header = df.columns.tolist()
        # # print(df)
        # # print(column1)
        # # print(column2)
        # x = np.array(df[[column1]])
        # y = np.array(df[[column2]])
        #
        # x1 = df[[column1]]
        # y1 = df[[column2]]

        # print(x1.to_string())

        # print(header)
        # print(header[0:7])
        # print(df.iloc[0])
        # print(df.head())
        # df.plot(kind ='hist' )
        # plt.show()

    def scatter(self):
        column1 = self.file_name1
        column2 = self.file_name2

        x = np.array(self.df[[column1]])
        y = np.array(self.df[[column2]])
        plt.title('Scatter plot from' + column1+' and '+column2)

        plt.xlabel(column1, color='red')
        plt.ylabel(column2, color='blue')
        plt.scatter(x, y, c='red')
        plt.show()


if __name__ == '__main__':
    list_cel = ['C1', 'C2', 'C3']
    listP_cel = ['P1', 'P2', 'P3']
    list_VT = ['Vehicle', 'Treatment']
    list_TR = ['TR1', 'TR2']
    list_AR = ['AR1', 'AR2', 'AR3', 'AR4', 'AR5']
    simulation_data = 'Simulation_HeartProteomics_20230914.xlsx'
    df = pb.read_excel(simulation_data, sheet_name='AnalyticalReps')
    My_gui = GUI()

    # print(column1_list, column2_list)





    # .loc[[2]] laat bv alleen rij 2 zien
    # .head(10) laat de eerste 10 rijen zien
    # .string print alles
