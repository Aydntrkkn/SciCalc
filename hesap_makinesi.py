from tkinter import *
import math

pen = Tk()
pen.title("Hesap Makinem")
pen.iconbitmap('c:/Users/hesapm.ico')
pen.geometry("470x213")
pen.resizable(width=FALSE, height=FALSE)

standart = 0
bilimsel = 1

menu = Menu(pen)
pen.config(menu = menu)
dosya1 = Menu(menu, tearoff = 0)
menu.add_cascade(label = "Types", menu = dosya1)
dosya1.add_command(label="Standart", command = lambda : menu_ops(standart))
dosya1.add_command(label="Scientific",command = lambda : menu_ops(bilimsel))

def menu_ops(menu_pressed):
    print(menu_pressed)
    if (menu_pressed == 1):
        pen.geometry("700x195")

        sin = Button(text="         sin          ", fg="black", bg="#ffe4b5", padx=15, pady=10, command=lambda: ekran("sin"))
        sin.grid(row=3, column=5)

        cos = Button(text="          cos        ", fg="black", bg="#ffe4b5", padx=15, pady=10, command=lambda: ekran("cos"))
        cos.grid(row=4, column=5)

        tan = Button(text="          tan        ", fg="black", bg="#ffe4b5", padx=15, pady=10, command=lambda: ekran("tan"))
        tan.grid(row=5, column=5)

        nokta = Button(text="            .           ", fg="black", bg="#ffe4b5", padx=15, pady=10, command=lambda: ekran("."))
        nokta.grid(row=6, column=5)

        krkk = Button(text="           √x         ", fg="black", bg="#ffe4b5", padx=15, pady=10, command=lambda: ekran("karekök"))
        krkk.grid(row=3, column=6)

        log = Button(text="         log(x)      ", fg="black", bg="#ffe4b5", padx=15, pady=10, command=lambda: ekran("log"))
        log.grid(row=4, column=6)

        exp = Button(text="        exp(x)      ", fg="black", bg="#ffe4b5", padx=15, pady=10, command=lambda: ekran("exp"))
        exp.grid(row=5, column=6)

        pi = Button(text="          π            ", fg="black", bg="#ffe4b5", padx=15, pady=10, command=lambda: ekran(math.pi))
        pi.grid(row=6, column=6)
    else:
        butonlar()
    return menu_pressed

işl = Entry(pen)
işl.grid(row=0, column=0, columnspan = 2, sticky = W)


def ekran(button):
    sn = Label(text="\t\t\t\t\t")
    sn.grid(row=0, column=1, columnspan=2)

    alınan = işl.get()

    if button == "=":
        işl.delete(0, END)
        alınan_işlem = eval(alınan)
        sonuç = eval(str(alınan_işlem))
        print(alınan)
        sonuç = round(sonuç,5)
        sn = Label(text= str(alınan) + "  =  " + str(sonuç))
        sn.grid(row=0, column=1, columnspan = 2)
        sonuç.delete(0, END)

    elif button == "sin":
        alınan = eval(alınan)
        sonuç = math.sin(float(alınan))
        sonuç = round(sonuç,5)

        sn = Label(text = "sin(" + str(alınan) + ") = " + str(sonuç))
        sn.grid(row=0, column=1, columnspan=2)
        sonuç.delete(0, END)

    elif button == "cos":
        alınan = eval(alınan)
        sonuç = math.cos(float(alınan))
        sonuç = round(sonuç,5)

        sn = Label(text= "cos(" + str(alınan) + ") = " + str(sonuç))
        sn.grid(row=0, column=1, columnspan=2)
        sonuç.delete(0, END)
    elif button == "tan":
        alınan = eval(alınan)
        sonuç = math.tan(float(alınan))
        sonuç = round(sonuç,5)

        sn = Label(text="tan(" + str(alınan) + ") = " + str(sonuç))
        sn.grid(row=0, column=1, columnspan=2)
        sonuç.delete(0, END)

    elif button == "karekök":
        alınan = eval(alınan)
        sonuç = math.sqrt(float(alınan))
        sonuç = round(sonuç,5)

        sn = Label(text="√(" + str(alınan) + ") = " + str(sonuç))
        sn.grid(row=0, column=1, columnspan=2)
        sonuç.delete(0, END)

    elif button == "log":
        alınan = eval(alınan)
        sonuç = math.log10(float(alınan))
        sonuç = round(sonuç,5)

        sn = Label(text="log(" + str(alınan) + ") = " + str(sonuç))
        sn.grid(row=0, column=1, columnspan=2)
        sonuç.delete(0, END)

    elif button == "exp":
        alınan = eval(str(alınan))
        sonuç = math.exp(float(alınan))
        sonuç = round(sonuç,5)

        sn = Label(text="exp(" + str(alınan) + ") = " + str(sonuç))
        sn.grid(row=0, column=1, columnspan=2)
        sonuç.delete(0, END)

    işl.delete(0, END)
    işl.insert(0, str(alınan) + str(button))
    alınan = str(alınan) + str(button)

    sn = Label(text=str(sonuç))
    sn.grid(row=0, column=1, columnspan=2,)
    sonuç.delete(0, END)

def temizle():
    işl.delete(0, END)

#  Butonlar

def butonlar():
    pen.geometry("470x213")

    bir = Button(text="\t1\t", fg="black", bg="white", padx=15, pady=10, command=lambda : ekran(1))
    bir.grid(row=3, column=0)

    iki = Button(text="\t2\t", fg="black", bg="white", padx=15, pady=10, command=lambda : ekran(2))
    iki.grid(row=3, column=1)

    üç = Button(text="\t3\t", fg="black", bg="white", padx=15, pady=10, command=lambda : ekran(3))
    üç.grid(row=3, column=2)

    dört = Button(text="\t4\t", fg="black", bg="white", padx=15, pady=10, command=lambda : ekran(4))
    dört.grid(row=4, column=0)

    beş = Button(text="\t5\t", fg="black", bg="white", padx=15, pady=10, command=lambda : ekran(5))
    beş.grid(row=4, column=1)

    altı = Button(text="\t6\t", fg="black", bg="white", padx=15, pady=10, command=lambda : ekran(6))
    altı.grid(row=4, column=2)

    yedi = Button(text="\t7\t", fg="black", bg="white", padx=15, pady=10, command=lambda : ekran(7))
    yedi.grid(row=5, column=0)

    sekiz = Button(text="\t8\t", fg="black", bg="white", padx=15, pady=10, command=lambda : ekran(8))
    sekiz.grid(row=5, column=1)

    dokuz = Button(text="\t9\t", fg="black", bg="white", padx=15, pady=10, command=lambda : ekran(9))
    dokuz.grid(row=5, column=2)

    sıfır = Button(text="\t0\t", fg="black", bg="white", padx=15, pady=10, command=lambda : ekran(0))
    sıfır.grid(row=6, column=1)

    çarp = Button(text="    x    ", fg="black", bg="orange", padx=15, pady=10, command=lambda : ekran("*"))
    çarp.grid(row=3, column=4)

    böl = Button(text="     /    ", fg="black", bg="orange", padx=15, pady=10, command=lambda : ekran("/"))
    böl.grid(row=4, column=4)

    topla = Button(text="    +    ", fg="black", bg="orange", padx=15, pady=10, command=lambda : ekran("+"))
    topla.grid(row=5, column=4)

    çıkar = Button(text="    -     ", fg="black", bg="orange", padx=15, pady=10, command=lambda : ekran("-"))
    çıkar.grid(row=6, column=4)

    eşittir = Button(text="\t=\t", fg="black", bg="orange", padx=15, pady=10, command=lambda : ekran("="))
    eşittir.grid(row=6, column=2)

    c = Button(text="          Temizle         ", fg="black", bg="orange", padx=15, pady=10, command=temizle)
    c.grid(row=6, column=0)

butonlar()

pen.mainloop()

