import pandas as pb
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk, font
from tkinter import messagebox


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
        # list with cellijn
        self.options = list_cel
        self.behand_list = list_VT
        self.tech_r = list_TR
        self.analy_r = list_AR

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
        self.root.geometry('600x600')

        # window title
        self.root.title('Simulation data')

        # logo icon
        self.root.iconphoto(False, tk.PhotoImage(file='UMC.icns'))

        # tabs
        self.my_notebook = ttk.Notebook(self.root, width=500,
                                        height=500, )
        self.my_notebook.pack()

        # frame1 & 2
        self.frame1 = tk.Frame(self.my_notebook, width=500, height=500,
                               bg='grey')
        self.frame2 = tk.Frame(self.my_notebook, width=500, height=500,
                               bg='red')

        # buttom frame for quit button
        self.bottom_frame = tk.Frame(self.root)

        # label for the tabs
        self.label1 = tk.Label(self.frame1, text='Settings', bg='grey')
        # self.label2 = tk.Label(self.frame1, text='which columns would you like to see?',bg='grey')
        self.label3 = tk.Label(self.frame2,
                               text='Still work in progress', bg='red')

        # option frames for in frame1
        self.column = tk.LabelFrame(self.frame1, width=150, height=400,
                                    bg='light grey', text='Column 1')

        self.graph = tk.LabelFrame(self.frame1, width=150, height=400,
                                   bg='light grey', text='Column 2')
        self.show = tk.LabelFrame(self.frame1, width=150, height=400,
                                  bg='light grey', text='Graph')

        # labels for the options
        # self.cLabel = tk.Label(self.column, text='Columns', bg='white',width=10,height=400,font=1)

        # quit button
        self.quit_but = tk.Button(self.bottom_frame, text='quit',
                                  fg='red', command=self.root.destroy)
        self.ok_but = tk.Button(self.bottom_frame, text='analyse',
                                fg='green', command=self.graphs)
        #
        # # intvar objecten voor de check buttons
        # self.cb_varC = tk.IntVar()
        # self.cb_varP = tk.IntVar()
        #
        # # zet de intvar objecten op 0
        # self.cb_varC.set(0)
        # self.cb_varP.set(0)

        self.BC = tk.Button(self.column, text='Control', font=10,
                            command=self.new_optionsC)
        self.BP = tk.Button(self.column, text='Patient', font=10,
                            command=self.new_optionsP)

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

        self.column.pack(side='left', padx=10)
        self.column.pack_propagate(False)

        self.graph.pack(side='left', padx=10)
        self.graph.pack_propagate(False)

        self.show.pack(side='left', padx=10)
        self.show.pack_propagate(False)

        self.BC.pack(padx=5)
        self.BP.pack(padx=5)

        """menu after control or patient is pressed """
        # new column frame when pressed
        self.name = tk.LabelFrame(self.column, width=150, height=400,
                                  bg='light grey', text='options')

        # drop down menu
        self.clicked = tk.StringVar()
        self.clicked.set('choose cellijn')
        self.cellijn = tk.OptionMenu(self.name, self.clicked,
                                     *self.options)
        self.cellijn.configure(font=10)

        # Vehicle & Treatment dropdown
        self.clicked2 = tk.StringVar()
        self.clicked2.set('choose treatment')
        self.behandeling = tk.OptionMenu(self.name, self.clicked2,
                                         *self.behand_list)
        self.behandeling.configure(font=10)

        # Tr1 or Tr2 dropdown.
        self.clicked3 = tk.StringVar()
        self.clicked3.set('choose technical rep')
        self.which_tr = tk.OptionMenu(self.name, self.clicked3,
                                         *self.tech_r)
        self.which_tr.configure(font=10)

        # AR 1,2,3,4,5
        self.clicked4 = tk.StringVar()
        self.clicked4.set('choose analy rep')
        self.which_ar = tk.OptionMenu(self.name, self.clicked4,
                                         *self.analy_r)
        self.which_ar.configure(font=10)




        # show Gui
        tk.mainloop()

    def new_optionsC(self):
        self.name.pack(side='left', padx=10)
        self.name.pack_propagate(False)
        self.cellijn.pack(pady=10)
        self.behandeling.pack(pady=10 )
        self.which_tr.pack(pady=10)
        self.which_ar.pack(pady=10)


        print('control')
        # tk.messagebox.showinfo('selection','control was pressed')

    def new_optionsP(self):
        tk.messagebox.showinfo('selection', 'patient was pressed')

    def graphs(self):
        tk.messagebox.showinfo('selection', 'loading')


if __name__ == '__main__':
    list_cel=['C1','C2','C3']
    list_VT = ['Vehicle', 'Treatment']
    list_TR = ['Tr1','Tr2']
    list_AR = ['AR1','AR2','AR3','AR4','AR5']
    My_Gui = GUI()
    simulation_data = 'Simulation_HeartProteomics_20230914.xlsx'
    read_file(simulation_data)

    # .loc[[2]] laat bv alleen rij 2 zien
    # .head(10) laat de eerste 10 rijen zien
    # .string print alles
