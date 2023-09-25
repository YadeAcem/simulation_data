import re
import tkinter
from tkinter import messagebox
import matplotlib.pyplot as plt

def open_fasta():
    with open("Caenorhabditis_elegans.cds_pep.all.fa") as fasta_bestand:
        header = []
        seq = []
        temp = []
        for regel in fasta_bestand:
            if ">" in regel:
                temp = "".join(temp)
                if temp != "":
                    seq.append(temp)
                temp = []
                header.append(regel)
            else:
                strip = regel.strip("\n")
                temp.append(strip)
    return header, seq


def vind_zincf(header,seq):
    """komt nog"""
    count = 0
    header_zincf = []
    zincf_seq = []
    for i in seq:
        count += 1
        if re.search(r"C.{2}C.{2}C.{5}C.{2}C.{2}C", i):
            header_zincf.append(header[count-1])
            zincf_seq.append(i)

    return header_zincf


def open_gff3():
    with open("Caenorhabditis_elegans.gff3") as gff3_bestand:
        content_gff3 = []
        for regel in gff3_bestand:
            if "#" not in regel:
                strip = regel.strip("\n").split("\t")
                content_gff3.append(strip)
    return content_gff3


def vind_acc(header_zincf):
    """komt nog"""
    acc_codes = []
    for i in header_zincf:
        split = i.strip(">").split(" ")
        acc_codes.append(split[0])
    return acc_codes


def vind_anno_mrna(acc_codes, content_gff3):
    acc_anno_dict = {}
    for regel in content_gff3:
        if "mRNA" in regel:
            for element in regel:
                for i in acc_codes:
                    if i in element:
                        acc_anno_dict.update({i: regel})
    return acc_anno_dict


def vind_gene_code(header_zincf):
    gene_codes = []
    for i in header_zincf:
        split = i.split(" ")
        gene_codes.append(split[3])
    return gene_codes


def vind_anno_gene(gene_codes, content_gff3):
    gen_anno_dict = {}
    for regel in content_gff3:
        if "gene" in regel:
            for element in regel:
                for i in gene_codes:
                    if i in element:
                        gen_anno_dict.update({i: regel})

    return gen_anno_dict


def bereken_len_rna(acc_anno_dict, acc_codes):
    """komt nog"""
    lengte_rna = {}
    for i in acc_codes:
        a = acc_anno_dict.get(i)
        leng = int(a[4]) - int(a[3])
        lengte_rna.update({i:leng})
    return lengte_rna


def bereken_len_gen(gen_anno_dict, gene_codes):
    lengte_gene = {}
    for i in gene_codes:
        a = gen_anno_dict.get(i)
        leng = int(a[4]) - int(a[3])
        lengte_gene.update({i: leng})
    return lengte_gene


def bepaal_chr(acc_anno_dict):
    chromosoon = {"chr1"  : 0,
                  "chr2" : 0,
                  "chr3" : 0,
                  "chr4" : 0,
                  "chr5" : 0,
                  "chrX" : 0}

    for i in acc_codes:
        a = acc_anno_dict.get(i)
        if a[0] == "I":
            chromosoon["chr1"] += 1
        if a[0] == "II":
            chromosoon["chr2"] += 1
        if a[0] == "III":
            chromosoon["chr3"] += 1
        if a[0] == "IV":
            chromosoon["chr4"] += 1
        if a[0] == "V":
            chromosoon["chr5"] += 1
        if a[0] == "X":
            chromosoon["chrX"] += 1
    return chromosoon


def staafdiagram(lengte_rna):
    plt.bar(lengte_rna.keys(), lengte_rna.values())
    plt.xticks(rotation='vertical')
    plt.title("Lengte per zinc finger in mRNA")
    plt.xlabel("accessiecode")
    plt.ylabel("lengte gen (nt)")
    plt.show()


def cirkeldiagram(lengte_gene):
    format = lengte_gene.values()
    label = lengte_gene.keys()
    plt.pie(format, startangle=350,
            labels=label, autopct=lambda p:f"{p*sum(format)/100:.0f}", pctdistance=0.75)
    plt.title("lengte van genen met zinc finger (nt)")
    plt.show()


class GUI:
    def __init__(self, chromosoon):
        self.chromosoon = chromosoon
        # Maak de window aan.
        self.main_window = tkinter.Tk()

        # Maak twee frames aan (top en bottom)
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(0)


        self.titel = tkinter.Label(self.top_frame,
                                   text=" aantal zinc finger op Chr")

        # Maak radiobuttons voor de 6 chromosonen
        self.chr1 = tkinter.Radiobutton(self.top_frame,
                                        text="Chr1",
                                        value=1,
                                        indicator=0,
                                        background="light green",
                                        variable=self.radio_var,
                                        command=lambda: print("test"))
        self.chr2 = tkinter.Radiobutton(self.top_frame,
                                        text="Chr2",
                                        value=2,
                                        indicator=0,
                                        background="light green",
                                        variable=self.radio_var,
                                        command=lambda: print("geen test"))
        self.chr3 = tkinter.Radiobutton(self.top_frame,
                                        text="Chr3",
                                        value=3,
                                        indicator=0,
                                        background="light green",
                                        variable=self.radio_var)
        self.chr4 = tkinter.Radiobutton(self.top_frame,
                                        text="Chr4",
                                        value=4,
                                        indicator=0,
                                        background="light green",
                                        variable=self.radio_var)
        self.chr5 = tkinter.Radiobutton(self.top_frame,
                                        text="Chr5",
                                        value=5,
                                        indicator=0,
                                        background="light green",
                                        variable=self.radio_var)
        self.chrX = tkinter.Radiobutton(self.top_frame,
                                        text="ChrX",
                                        value=6,
                                        indicator=0,
                                        background="light green",
                                        variable=self.radio_var)

        # maak een button aan om te stoppen
        self.zoekknop = tkinter.Button(self.bottom_frame,
                                       text="Zoek",
                                       command=lambda: self.aantal_gen())
        self.stopknop = tkinter.Button(self.bottom_frame,
                                       text="Quit",
                                       command=self.main_window.destroy)

        self.titel.pack()

        # Pack de radiobuttons
        self.chr1.pack(side="left")
        self.chr2.pack(side="left")
        self.chr3.pack(side="left")
        self.chr4.pack(side="left")
        self.chr5.pack(side="left")
        self.chrX.pack(side="left")

        # Pack de zoek en stop knop
        self.zoekknop.pack(side="right")
        self.stopknop.pack(side="left")

        # Pack de frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Zorgt ervoor dat de GUI tevoorschijn komt
        tkinter.mainloop()

    def aantal_gen(self):
        """"""
        if self.radio_var.get() == 1:
            tkinter.messagebox.showinfo("Aantal zinc finger genen",
                                        "Op chromosoon 1 zitten " +
                                        str(self.chromosoon.get("chr1"))
                                        + " zinc finger genen.")
        if self.radio_var.get() == 2:
            tkinter.messagebox.showinfo("Aantal zinc finger genen",
                                        "Op chromosoon 2 zitten " +
                                        str(self.chromosoon.get("chr2"))
                                        + " zinc finger genen.")
        if self.radio_var.get() == 3:
            tkinter.messagebox.showinfo("Aantal zinc finger genen",
                                        "Op chromosoon 3 zitten " +
                                        str(self.chromosoon.get("chr3"))
                                        + " zinc finger genen.")
        if self.radio_var.get() == 4:
            tkinter.messagebox.showinfo("Aantal zinc finger genen",
                                        "Op chromosoon 4 zitten " +
                                        str(self.chromosoon.get("chr4"))
                                        + " zinc finger genen.")
        if self.radio_var.get() == 5:
            tkinter.messagebox.showinfo("Aantal zinc finger genen",
                                        "Op chromosoon 5 zitten " +
                                        str(self.chromosoon.get("chr5"))
                                        + " zinc finger genen.")
        if self.radio_var.get() == 6:
            tkinter.messagebox.showinfo("Aantal zinc finger genen",
                                        "Op chromosoon X zitten " +
                                        str(self.chromosoon.get("chrX"))
                                        + " zinc finger genen.")




if __name__ == '__main__':
    header, seq = open_fasta()
    header_zincf = vind_zincf(header, seq)
    content_gff3 = open_gff3()
    acc_codes = vind_acc(header_zincf)
    acc_anno_dict = vind_anno_mrna(acc_codes, content_gff3)
    lengte_rna = bereken_len_rna(acc_anno_dict, acc_codes)
    chromosoon = bepaal_chr(acc_anno_dict)
    gene_codes = vind_gene_code(header_zincf)
    gen_anno_dict = vind_anno_gene(gene_codes, content_gff3)
    lengte_gene = bereken_len_gen(gen_anno_dict, gene_codes)
    staafdiagram(lengte_rna)
    cirkeldiagram(lengte_gene)
    positie = GUI(chromosoon)