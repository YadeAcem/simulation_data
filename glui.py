import tkinter

class GUI:
    def __init__(self):
        try:
            # maak de window
            self.main_window = tkinter.Tk()

            # Maak 2 frames aan (top and bottom)
            self.top_frame = tkinter.Frame(self.main_window)
            self.bottom_frame = tkinter.Frame(self.main_window)

            # Maak een label aan
            self.label1 = tkinter.Label(self.top_frame,
                                        text="Van welke plek wilt u het"
                                             " aantal proteinen zien?",
                                        bg="pink")

            # Plaats de label in de GUI
            self.label1.pack()

            # maak 19 intvar objecten voor de checkbuttons
            self.cb_var1 = tkinter.IntVar()
            self.cb_var2 = tkinter.IntVar()
            self.cb_var3 = tkinter.IntVar()
            self.cb_var4 = tkinter.IntVar()
            self.cb_var5 = tkinter.IntVar()
            self.cb_var6 = tkinter.IntVar()
            self.cb_var7 = tkinter.IntVar()
            self.cb_var8 = tkinter.IntVar()
            self.cb_var9 = tkinter.IntVar()
            self.cb_var10 = tkinter.IntVar()
            self.cb_var11 = tkinter.IntVar()
            self.cb_var12 = tkinter.IntVar()
            self.cb_var13 = tkinter.IntVar()
            self.cb_var14 = tkinter.IntVar()
            self.cb_var15 = tkinter.IntVar()
            self.cb_var16 = tkinter.IntVar()
            self.cb_var17 = tkinter.IntVar()
            self.cb_var18 = tkinter.IntVar()
            self.cb_var19 = tkinter.IntVar()

            # zet de 19 intvar objecten naar 0
            self.cb_var1.set(0)
            self.cb_var2.set(0)
            self.cb_var3.set(0)
            self.cb_var4.set(0)
            self.cb_var5.set(0)
            self.cb_var6.set(0)
            self.cb_var7.set(0)
            self.cb_var8.set(0)
            self.cb_var9.set(0)
            self.cb_var10.set(0)
            self.cb_var11.set(0)
            self.cb_var12.set(0)
            self.cb_var13.set(0)
            self.cb_var14.set(0)
            self.cb_var15.set(0)
            self.cb_var16.set(0)
            self.cb_var17.set(0)
            self.cb_var18.set(0)
            self.cb_var19.set(0)

            # pack de frames
            self.top_frame.pack()
            self.bottom_frame.pack()

            # maak de checkbuttons aan
            self.cb1 = tkinter.Checkbutton(self.top_frame,
                                           text="CDS",
                                           variable=self.cb_var1)
            self.cb2 = tkinter.Checkbutton(self.top_frame,
                                           text="Chromosome",
                                           variable=self.cb_var2)
            self.cb3 = tkinter.Checkbutton(self.top_frame,
                                           text="exon",
                                           variable=self.cb_var3)

            self.cb4 = tkinter.Checkbutton(self.top_frame,
                                           text="five_prime_UTR",
                                           variable=self.cb_var4)

            self.cb5 = tkinter.Checkbutton(self.top_frame,
                                           text="lnc_RNA",
                                           variable=self.cb_var5)

            self.cb6 = tkinter.Checkbutton(self.top_frame,
                                           text="miRNA",
                                           variable=self.cb_var6)

            self.cb7 = tkinter.Checkbutton(self.top_frame,
                                           text="mRNA",
                                           variable=self.cb_var7)

            self.cb8 = tkinter.Checkbutton(self.top_frame,
                                           text="ncRNA",
                                           variable=self.cb_var8)

            self.cb9 = tkinter.Checkbutton(self.top_frame,
                                           text="ncRNA_gene",
                                           variable=self.cb_var9)

            self.cb10 = tkinter.Checkbutton(self.top_frame,
                                            text="piRNA",
                                            variable=self.cb_var10)

            self.cb11 = tkinter.Checkbutton(self.top_frame,
                                            text="pre_miRNA",
                                            variable=self.cb_var11)

            self.cb12 = tkinter.Checkbutton(self.top_frame,
                                            text="pseudogene",
                                            variable=self.cb_var12)

            self.cb13 = tkinter.Checkbutton(self.top_frame,
                                            text="pseudogenic_script",
                                            variable=self.cb_var13)

            self.cb14 = tkinter.Checkbutton(self.top_frame,
                                            text="rRNA",
                                            variable=self.cb_var14)

            self.cb15 = tkinter.Checkbutton(self.top_frame,
                                            text="snoRNA",
                                            variable=self.cb_var15)

            self.cb16 = tkinter.Checkbutton(self.top_frame,
                                            text="snRNA",
                                            variable=self.cb_var16)

            self.cb17 = tkinter.Checkbutton(self.top_frame,
                                            text="three_prime_UTR",
                                            variable=self.cb_var17)

            self.cb18 = tkinter.Checkbutton(self.top_frame,
                                            text="tRNA",
                                            variable=self.cb_var18)

            self.cb19 = tkinter.Checkbutton(self.top_frame,
                                            text="gene",
                                            variable=self.cb_var19)

            # Checkbutton wordt zichtbaar
            self.cb1.pack()
            self.cb2.pack()
            self.cb3.pack()
            self.cb4.pack()
            self.cb5.pack()
            self.cb6.pack()
            self.cb7.pack()
            self.cb8.pack()
            self.cb9.pack()
            self.cb10.pack()
            self.cb11.pack()
            self.cb12.pack()
            self.cb13.pack()
            self.cb14.pack()
            self.cb15.pack()
            self.cb16.pack()
            self.cb17.pack()
            self.cb18.pack()
            self.cb19.pack()

            # maak buttons aan
            self.ok_button = tkinter.Button(self.bottom_frame,
                                            text="Show", fg="green",
                                            command=self.show_results)
            self.quit_button = tkinter.Button(self.bottom_frame,
                                              text="Quit", fg="red",
                                              command=self.main_window.
                                              destroy)
            # show buttons
            self.ok_button.pack(side="left")
            self.quit_button.pack(side="left")

            # zorgt dat de GUI verschijnt
            tkinter.mainloop()
        except AttributeError:
            print(
                "check uw tkinter/GUI. deze heeft geen goede attribute")
        except ModuleNotFoundError:
            print("Check uw import")

    def show_results(self):
        """wanner er op OK wordt gedrukt, laten we zien in een
        messagebox welke check box is aangefinkt"""
        try:
            self.message = "Goeie keus!:\n"
            if self.cb_var1.get() == 1:
                self.message = self.message + "Op het CDS liggen: " \
                                              "225661 verschillende " \
                                              "eiwitten\n "
            if self.cb_var2.get() == 1:
                self.message = self.message + "Op het chromosome " \
                                              "liggen: 7 " \
                                              "verschillende " \
                                              "eiwitten\n "
            if self.cb_var3.get() == 1:
                self.message = self.message + "Op het exon liggen: " \
                                              "273641 verschillende " \
                                              "eiwitten\n"
            if self.cb_var4.get() == 1:
                self.message = self.message + "Op het five_prime_UTR " \
                                              "liggen 31088 " \
                                              "verschillende eiwitten\n"
            if self.cb_var5.get() == 1:
                self.message = self.message + "Op het lnc_RNA liggen:" \
                                              "288 verschillende " \
                                              "eiwitten\n "
            if self.cb_var6.get() == 1:
                self.message = self.message + "Op het miRNA liggen: " \
                                              "458 verschillende " \
                                              "eiwitten\n "
            if self.cb_var7.get() == 1:
                self.message = self.message + "Op het mimRNA liggen: " \
                                              "335521 verschillende " \
                                              "eiwitten\n"
            if self.cb_var8.get() == 1:
                self.message = self.message + "Op het ncRNA liggen: " \
                                              "8441 verschillende " \
                                              "eiwittenn\n "
            if self.cb_var9.get() == 1:
                self.message = self.message + "Op het ncRNA_gene " \
                                              "liggen: 24791 " \
                                              "verschillende " \
                                              "eiwittenn\n "
            if self.cb_var10.get() == 1:
                self.message = self.message + "Op het piRNA liggen: " \
                                              "15363 verschillende" \
                                              " eiwitten\n"
            if self.cb_var11.get() == 1:
                self.message = self.message + "Op het pre_miRNA " \
                                              "liggen: 260 " \
                                              "verschillende " \
                                              "eiwitten\n "
            if self.cb_var12.get() == 1:
                self.message = self.message + "Op het pseudogene " \
                                              "liggen: 260 " \
                                              "verschillende " \
                                              "eiwitten\n "
            if self.cb_var13.get() == 1:
                self.message = self.message + "Op het " \
                                              "pseudogenic_transcript" \
                                              "liggen: 1958 " \
                                              "verschillende " \
                                              "eiwitten\n "
            if self.cb_var14.get() == 1:
                self.message = self.message + "Op het rRNA liggen: 22" \
                                              "verschillende " \
                                              "eiwitten\n "
            if self.cb_var15.get() == 1:
                self.message = self.message + "Op het snoRNA liggen: " \
                                              "346 verschillende " \
                                              "eiwitten\n "
            if self.cb_var16.get() == 1:
                self.message = self.message + "Op het snRNA liggen: " \
                                              "129 verschillende " \
                                              "eiwitten\n "
            if self.cb_var17.get() == 1:
                self.message = self.message + "Op het three_prime_UTR" \
                                              "liggen: 28213 " \
                                              "verschillende eiwitten\n"
            if self.cb_var18.get() == 1:
                self.message = self.message + "Op het tRNA liggen: " \
                                              "634 verschillende " \
                                              "eiwitten\n "
            if self.cb_var19.get() == 1:
                self.message = self.message + "Op de gene liggen: " \
                                              "20191 verschillende " \
                                              "eiwitten\n "

            tkinter.messagebox.showinfo("Selectie", self.message)

        except AttributeError:
            print("check uw tkinter. deze heef tgeen attribute"
                  " messagebx")
        except ModuleNotFoundError:
            print("Check uw import")

if __name__ == '__main__':
    My_Gui= GUI()