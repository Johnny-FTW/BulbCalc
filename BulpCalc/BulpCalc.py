from tkinter import *

from fpdf import FPDF

import os

import tkinter as tk

import re

root = Tk()

root.title('BulpCalc')

root.geometry('800x600')

root.configure(bg='#F9e2c4')

root.resizable(width=False, height=False)

# panels-----------

panel_1 = PanedWindow(bd=4, relief="raised", bg="#eab676")
panel_1.pack(fill=BOTH, expand=1)

left_label = Label(panel_1, bg="#F9e2c4", width=22)

panel_1.add(left_label)
my_menu = Menu(root)

panel_2 = PanedWindow(panel_1, orient=VERTICAL, relief="flat", bg="#F9e2c4")
panel_1.add(panel_2)

top = Label(panel_2, heigh=4, bg="#F9e2c4")
panel_2.add(top)

bottom = Label(panel_2, bg="#F9e2c4")
panel_2.add(bottom)

root.config(menu=my_menu)

Nadpis = Label(panel_2, text="Bulb.Calc v1.0", bg='#F9e2c4', font=('Arial', 30))
Nadpis.place(x=180, y=8)


def restart_program():
    root.destroy()
    os.startfile("BulpCalc.py")

def back_to_root():
    frame_sprava.pack_forget()
    frame_trojclenka.pack_forget()
    frame_uspora.pack_forget()


file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New..", command=restart_program)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)
file_menu.add_separator()
file_menu.add_command(label="Back", command=back_to_root)


def press_sprava():
    hide_all_frames()
    frame_sprava.pack(fill="both", expand=1)


def press_trojclenka():
    hide_all_frames()
    frame_trojclenka.pack(fill="both", expand=1)


def press_uspora():
    hide_all_frames()
    frame_uspora.pack(fill="both", expand=1)


def hide_all_frames():
    frame_sprava.pack_forget()
    frame_trojclenka.pack_forget()
    panel_1.pack_forget()


# menu-----------------------

button1 = Button(root, text='Správa do auditu', font=('times new roman', 12),
                 relief='ridge', borderwidth=1, bg='#eab676', width=12,
                 height=2, command=press_sprava)
button1.place(x=25, y=100)

button2 = Button(root, text='Trojčlenka', font=('times new roman', 12),
                 relief='ridge', borderwidth=1, bg='#eab676', width=12,
                 height=2, command=press_trojclenka)
button2.place(x=25, y=175)

button3 = Button(root, text='Úspora energie', font=('times new roman', 12),
                 relief='ridge', borderwidth=1, bg='#eab676', width=12,
                 height=2, command=press_uspora)
button3.place(x=25, y=25)

# frames---------------------------------------------

frame_sprava = Frame(root, width=800, height=600, bg='#F9e2c4')
frame_trojclenka = Frame(root, width=800, height=600, bg='#F9e2c4')
frame_uspora = Frame(root, width=800, height=600, bg='#F9e2c4')

# photo------------------------------------------------------------
photo = PhotoImage(file=r"C:\Users\janha\Desktop\BulpCalc\file.png")
Button(panel_2, text='Click Me !', image=photo, width=600, height=510, bg='#F9e2c4', relief='flat').pack(side=BOTTOM)


# trojclenka------------------------------------------

def vypocet_trojclenky():
    x1 = E1.get()
    x2 = E2.get()
    x3 = E3.get()
    L4 = Label(frame_trojclenka, text="{:.3f}".format(float(x1) / float(x2) * float(x3)))
    L4.place(x=200, y=175)


L1 = Label(frame_trojclenka, text="Zadaj hrúbku materiálu: [m]")
L1.place(x=25, y=25)
E1 = Entry(frame_trojclenka, bd=5)
E1.place(x=200, y=25)

L2 = Label(frame_trojclenka, text="Zadaj lambdu:")
L2.place(x=25, y=75)
E2 = Entry(frame_trojclenka, bd=5)
E2.place(x=200, y=75)

L3 = Label(frame_trojclenka, text="Nová lambda:")
L3.place(x=25, y=125)
E3 = Entry(frame_trojclenka, bd=5)
E3.place(x=200, y=125)

L5 = Label(frame_trojclenka, text="m")
L5.place(x=230, y=175)

button4 = Button(frame_trojclenka, text='Výpočet',
                 command=vypocet_trojclenky,bg="orange")
button4.place(x=25, y=175)

# uspora----------------------------------------------

L11 = Label(frame_uspora, text="Potreba tepla na vykurovanie pred opatrením: [kWh/m2.a]")
L11.place(x=25, y=25)
E11 = Entry(frame_uspora, bd=5, width=10)
E11.place(x=350, y=25)

L22 = Label(frame_uspora, text="Potreba tepla na vykurovanie po opatrení: [kWh/m2.a]")
L22.place(x=25, y=75)
E22 = Entry(frame_uspora, bd=5, width=10)
E22.place(x=350, y=75)

L33 = Label(frame_uspora, text="Spotreba elektrickej energie: [MWh]")
L33.place(x=25, y=125)
E33 = Entry(frame_uspora, bd=5, width=10)
E33.place(x=350, y=125)

L44 = Label(frame_uspora, text="Spotreba plynu/tepla: [MWh]")
L44.place(x=25, y=175)
E44 = Entry(frame_uspora, bd=5, width=10)
E44.place(x=350, y=175)

L55 = Label(frame_uspora, text="Z toho EE na vykurovanie: [MWh]")
L55.place(x=450, y=125)
E55 = Entry(frame_uspora, bd=5, width=10)
E55.place(x=650, y=125)

L66 = Label(frame_uspora, text="Z toho ZP na vykurovanie: [MWh]")
L66.place(x=450, y=175)
E66 = Entry(frame_uspora, bd=5, width=10)
E66.place(x=650, y=175)


def vypocet_uspory_EE():
    Pred = E11.get()
    Po = E22.get()
    Spot_EE = E33.get()
    Spot_Vyk_EE = E55.get()

    if Checkbutton12.get():
        uspora_EE = 0
    else:
        uspora_EE = (float(Po) / float(Pred) - 1) * (float(Spot_Vyk_EE) * -1)

    EE_po_naprave = float(Spot_EE) - uspora_EE

    L77 = Label(frame_uspora,
                text="Úspora EE je: {:.2f} MWh a predpokladaná ročná spotreba bude {:.2f} MWh.".format(uspora_EE,
                                                                                                       EE_po_naprave))
    L77.place(x=175, y=227)


def vypocet_uspory_ZP():
    Pred = E11.get()
    Po = E22.get()
    Spot_ZP = E44.get()
    Spot_Vyk_ZP = E66.get()

    if Checkbutton11.get():
        uspora_ZP = 0
    else:
        uspora_ZP = (float(Po) / float(Pred) - 1) * (float(Spot_Vyk_ZP) * -1)
    ZP_po_naprave = float(Spot_ZP) - uspora_ZP

    L78 = Label(frame_uspora,
                text="Úspora ZP/tepla je: {:.2f} MWh a predpokladaná ročná spotreba bude {:.2f} MWh.".format(uspora_ZP,
                                                                                                             ZP_po_naprave))
    L78.place(x=175, y=277)


button5 = Button(frame_uspora, text='Výpočet úspory EE',
                 command=vypocet_uspory_EE, bg="orange")
button5.place(x=25, y=225)

button6 = Button(frame_uspora, text='Výpočet úspory ZP',
                 command=vypocet_uspory_ZP, bg="orange")
button6.place(x=25, y=275)

Checkbutton11 = IntVar()
Checkbutton12 = IntVar()

Button11 = Checkbutton(frame_uspora, text="Nevykuruje sa plynom/teplom",
                       variable=Checkbutton11,
                       onvalue=1,
                       offvalue=0,
                       height=2,
                       width=25)

Button12 = Checkbutton(frame_uspora, text="Nevykuruje sa elektrinou",
                       variable=Checkbutton12,
                       onvalue=1,
                       offvalue=0,
                       height=2,
                       width=25)

Button11.pack(side=BOTTOM)
Button12.pack(side=BOTTOM)

# sprava_audit---------------------------------------------------

L111 = Label(frame_sprava, text='Názov spoločnosti:')
L111.place(x=25, y=25)
E111 = Entry(frame_sprava, bd=5, width=20)
E111.place(x=150, y=25)

L112 = Label(frame_sprava, text='Počet podlaží:')
L112.place(x=25, y=50)
E112 = Entry(frame_sprava, bd=5, width=5)
E112.place(x=150, y=50)

L113 = Label(frame_sprava, text='Miesto stavby v:')
L113.place(x=25, y=75)
E113 = Entry(frame_sprava, bd=5, width=15)
E113.place(x=150, y=75)

Checkbutton13 = IntVar()
Button13 = Checkbutton(frame_sprava, text="V prenájme",
                       variable=Checkbutton13,
                       onvalue=1,
                       offvalue=0,
                       height=1,
                       width=15)
Button13.pack(pady=0)

L114 = Label(frame_sprava, text='Materiál obv. steny:')
L114.place(x=475, y=25)
E114 = Entry(frame_sprava, bd=5, width=15)
E114.place(x=600, y=25)

Checkbutton15 = IntVar()
Button15 = Checkbutton(frame_sprava, text="Zateplená stena",
                       variable=Checkbutton15,
                       onvalue=1,
                       offvalue=0,
                       height=1,
                       width=15)
Button15.pack(pady=0)

L115 = Label(frame_sprava, text='Typ strechy:')
L115.place(x=475, y=50)
E115 = Entry(frame_sprava, bd=5, width=15)
E115.place(x=600, y=50)

Checkbutton16 = IntVar()
Button16 = Checkbutton(frame_sprava, text="Zateplená strecha",
                       variable=Checkbutton16,
                       onvalue=1,
                       offvalue=0,
                       height=1,
                       width=15)
Button16.pack(pady=0)

Checkbutton17 = IntVar()
Button17 = Checkbutton(frame_sprava, text="Nové okná",
                       variable=Checkbutton17,
                       onvalue=1,
                       offvalue=0,
                       height=1,
                       width=15)
Button17.pack(pady=0)

L116 = Label(frame_sprava, text='Počet skiel:')
L116.place(x=475, y=75)
E116 = Entry(frame_sprava, bd=5, width=15)
E116.place(x=600, y=75)

L117 = Label(frame_sprava, text='Vykur. zabezpečuje:')
L117.place(x=475, y=100)
E117 = Entry(frame_sprava, bd=5, width=15)
E117.place(x=600, y=100)

L118 = Label(frame_sprava, text='PTV zabezpečuje:')
L118.place(x=475, y=125)
E118 = Entry(frame_sprava, bd=5, width=15)
E118.place(x=600, y=125)

Checkbutton18 = IntVar()
Button18 = Checkbutton(frame_sprava, text="Nové svietidlá",
                       variable=Checkbutton18,
                       onvalue=1,
                       offvalue=0,
                       height=1,
                       width=15)
Button18.pack(pady=0)

Checkbutton19 = IntVar()
Button19 = Checkbutton(frame_sprava, text="VZT v budove",
                       variable=Checkbutton19,
                       onvalue=1,
                       offvalue=0,
                       height=1,
                       width=15)
Button19.pack(pady=0)

T = tk.Text(frame_sprava)
quote = ''
T.pack(side=BOTTOM)
T.insert(tk.END, quote)


def uloz():
    global new_text
    spolocnost = E111.get()
    pocet_podlazi = E112.get()
    miesto_stavby = E113.get()

    if Checkbutton13.get():
        prenajom = 'Spoločnosť má priestory, v ktorých sídli v prenájme.'
    else:
        prenajom = 'Spoločnosť je majiteľom daného objektu.'

    obvodova_stena = E114.get()

    if Checkbutton15.get():
        zateplenie1 = 'so zateplením'
    else:
        zateplenie1 = 'bez zateplenia'

    strecha = E115.get()

    if Checkbutton16.get():
        zateplenie2 = 's tepelnou izoláciou'
    else:
        zateplenie2 = 'bez tepelnej izolácie'

    pocet_skiel = 'izolačním %s-sklom' % (E116.get())

    if Checkbutton17.get():
        material_okien = 'nové'

    else:
        material_okien = 'pôvodné'
        pocet_skiel = 'jednoduchým zasklením'

    vykurovanie = E117.get()
    voda = E118.get()

    if Checkbutton18.get():
        typ_svietidiel = 'LED'

    else:
        typ_svietidiel = 'žiarovkovými'

    if Checkbutton19.get():
        VZT = 'nachádzajú'

    else:
        VZT = 'nenachádzajú'

    text = ["Priestory spoločnosti {} sa nachádzajú v {}-podlažnom objekte v {}.\n".format(spolocnost, pocet_podlazi,miesto_stavby),
            "{}\nBudova má vlastný zdroj tepla na vykurovanie a prípravu teplej vody.\n".format(prenajom),
            "Obvodovú stenu tvorí {} {}.".format(obvodova_stena, zateplenie1),"\nStrecha objektu je {} {}.\n".format(strecha, zateplenie2),
            "Podlahu tvorí betónový podklad s keramickou dlažbou v maltovom lôžku.\nOkná sú {} s {}. ".format(material_okien, pocet_skiel),
            "Zdrojom vykurovania je {}.".format(vykurovanie),"\nPrípravu teplej vody zabezpečuje {}.\n".format(voda),
            "Priestory sú osvetľované {} svietidlami rôznych typov a výkonov.\n".format(typ_svietidiel),
            "Ovládanie je ručné, vypínače sú umiestnené na stenách jednotlivých miestností.\n"
            "Prevádzkový čas osvetlenia je podľa prevádzkovej doby objektu. \nV objekte sa {} VZT jednotky.".format(VZT)]

    new_text = ''
    items_sprava = len(text)

    for i in range(items_sprava):
        s1 = re.sub("[{}]", "", text[i])
        s1 = str(s1)
        new_text = str(new_text) + s1


    T.insert(tk.END, new_text)

def generovat():
    T.insert(tk.END, uloz)

def export_text():
    with open("Sprava.txt", "w", encoding="utf-8") as tx:
        tx.write(new_text)

def export_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 12)
    #pdf.cell(200, 10, txt=new_text,
    #         ln=1, align='C')
    f = open("Sprava.txt", "r",encoding="ISO8859_9")
    for x in f:
        pdf.cell(200, 10, txt = x, ln = 1, align = 'L')
    pdf.output("Sprava.pdf")


button9 = Button(frame_sprava, text='Generovať_správu',
                 command=uloz, bg='orange', width=15)
button9.place(x=25, y=120)

button10 = Button(frame_sprava, text='Export_to_txt',
                 command=export_text, bg='orange', width=15)
button10.place(x=25, y=150)

button11 = Button(frame_sprava, text='Export_to_PDF',
                 command=export_pdf, bg='orange', width=15)
button11.place(x=25, y=180)

# END---------------------------------------------------------

root.iconbitmap('lamp.ico')
root.mainloop()
