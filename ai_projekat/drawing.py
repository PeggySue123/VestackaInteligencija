from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from checkLogic import *
from minimax import potezRacunara
from state import krajnjeStanje
import random

def iscrtajTablu(n: int, m: int, frame: Frame, fields: list[Label], walls: list[Label], p11: int, p12: int, p21: int, p22: int, p31: int, p32: int, p41: int, p42: int):
    for i in range (0,n):
        for j in range (0,m):
            if(j > 0 and j < m-1 and j%2 == 0):
                if(i==0 or i==n-1):
                    if( j < 19):
                        ttk.Label(frame, text=int(j/2), width=3).grid(column=j, row=i+1)
                    else:
                        ttk.Label(frame, text=chr(int(j/2)+55), width=3).grid(column=j, row=i+1)
                elif(i==1 or i==n-2):
                    ttk.Label(frame, text='=', width=3).grid(column=j, row=i+1)
                elif(j > 1 and j < m-2 and i > 1 and i < n-2 and i % 2 == 1):
                    label: Label = ttk.Label(frame, text='_', width=3)
                    walls.append(label)
                    label.grid(column=j, row=i+1)
                elif(j > 1 and j < m-2 and i > 1 and i < n-2 and i % 2 == 0):
                    if (i == p11 * 2 and j == p12 * 2):
                        label: Label = ttk.Label(frame, text='X1', width=3)
                        fields.append(label)
                        label.grid(column=j, row=i+1)
                        continue
                    elif (i == p21 * 2 and j == p22 * 2):
                        label: Label = ttk.Label(frame, text='X2', width=3)
                        fields.append(label)
                        label.grid(column=j, row=i+1)
                        continue
                    elif (i == p31 * 2 and j == p32 * 2):
                        label: Label = ttk.Label(frame, text='O1', width=3)
                        fields.append(label)
                        label.grid(column=j, row=i+1)
                        continue
                    elif (i == p41 * 2 and j == p42 * 2):
                        label: Label = ttk.Label(frame, text='O2', width=3)
                        fields.append(label)
                        label.grid(column=j, row=i+1)
                        continue
                    if (j<19):
                        if (i < 19):
                            label: Label = ttk.Label(frame, text=str(int(i/2)) + str(int(j/2)), width=3)
                            fields.append(label)
                            label.grid(column=j, row=i+1)
                        else:
                            label: Label = ttk.Label(frame, text=str(chr(int(i/2) + 55)) + str(int(j/2)), width=3)
                            fields.append(label)
                            label.grid(column=j, row=i+1)
                    else: 
                        if (i < 19):
                            label: Label = ttk.Label(frame, text=str(int(i/2)) + str(chr(int(j/2) + 55)), width=3)
                            fields.append(label)
                            label.grid(column=j, row=i+1)
                        else:
                            label: Label = ttk.Label(frame, text=str(chr(int(i/2) + 55)) + str(chr(int(j/2) + 55)), width=3)
                            fields.append(label)
                            label.grid(column=j, row=i+1)
            
            elif(i > 0 and i < n-1 and i%2 == 0):
                if(j==0 or j==m-1):
                    if( i < 19):
                        ttk.Label(frame, text=int(i/2), width=3).grid(column=j, row=i+1)
                    else:
                        ttk.Label(frame, text=chr(int(i/2)+55), width=3).grid(column=j, row=i+1)
                elif(j==1 or j==m-2):
                    ttk.Label(frame, text='||', width=3).grid(column=j, row=i+1)
                elif(i > 1 and i < n-2 and j > 1 and j < m-2 and j % 2 == 1):
                    label =ttk.Label(frame, text='|', width=3)
                    walls.append(label)
                    label.grid(column=j, row=i+1)

def iscrtajIzbor(root: Tk, options: Frame, frame: Frame, btnTypeOfGame: Button, ts0: OptionMenu, ts1: OptionMenu, ts2: OptionMenu, ts4: OptionMenu, tableSizeN: StringVar, tableSizeM: StringVar, numberOfWalls: StringVar, typeOfGame: StringVar, fields: list[Label], walls: list[Label], zidovi: list[Label], a: list[int], b: list[int]):
    btnTypeOfGame.pack_forget()
    gameType = typeOfGame.get()
    ts4.pack_forget()
    if (gameType == "Čovek vs Računar"):
        firstPlayer = StringVar(root)
        firstPlayer.set("Prvi?")
        ts3 = OptionMenu(options, firstPlayer, "Korisnik", "Računar")
        ts3.pack(side=LEFT)

        label1 = Label(options, text="Unesite koordinate prvog pesaka sa razmakom:")
        label1.pack(side=LEFT)
        inPos1 = Entry(options, fg="grey", bg="white", width=5)
        inPos1.pack(side=LEFT)
        label2 = Label(options, text="Unesite koordinate drugog pesaka sa razmakom:")
        label2.pack(side=LEFT)
        inPos2 = Entry(options, fg="grey", bg="white", width=5)
        inPos2.pack(side=LEFT)

        buttonStart = ttk.Button(options, text="Start", command=lambda: upamtiPocetnoStanje(fields, walls, zidovi, options, tableSizeN, tableSizeM, numberOfWalls, firstPlayer,
        frame, inPos1, inPos2, label1, label2, ts0, ts1, ts2, ts3, buttonStart, a, b))
        buttonStart.pack(side=LEFT)
    else:
        label1 = Label(options, text="Unesite koordinate prvog pesaka igraca 1. sa razmakom:")
        label1.pack(side=TOP)
        inPos1 = Entry(options, fg="grey", bg="white", width=5)
        inPos1.pack(side=TOP)
        label2 = Label(options, text="Unesite koordinate drugog pesaka igraca 1. sa razmakom:")
        label2.pack(side=TOP)
        inPos2 = Entry(options, fg="grey", bg="white", width=5)
        inPos2.pack(side=TOP)

        label3 = Label(options, text="Unesite koordinate prvog pesaka igraca 2. sa razmakom:")
        label3.pack(side=TOP)
        inPos3 = Entry(options, fg="grey", bg="white", width=5)
        inPos3.pack(side=TOP)
        label4 = Label(options, text="Unesite koordinate drugog pesaka igraca 2. sa razmakom:")
        label4.pack(side=TOP)
        inPos4 = Entry(options, fg="grey", bg="white", width=5)
        inPos4.pack(side=TOP)

        buttonStart = ttk.Button(options, text="Start", command=lambda: upamtiPocetnoStanje2(fields, walls, zidovi, options, tableSizeN, tableSizeM, numberOfWalls, frame, inPos1, inPos2, inPos3, inPos4, label1, label2, label3, label4, ts0, ts1, ts2, buttonStart, a, b))
        buttonStart.pack(side=BOTTOM)

def iscrtajZid(args: list[int], frame: Frame, walls: list[Label], zidovi: list[Label]):
    for w in walls:
        if (args[8] == 0):
            if (int(w.grid_info()['row'])-1 == args[0] * 2 and int(w.grid_info()['column']) == args[1] * 2 + 1):
                w.config(text = '||')
                zidovi.append(w)
                label = ttk.Label(frame, text='||', width=3)
                zidovi.append(label)
                label.grid(row = args[0] * 2 + 2, column=args[1] * 2 + 1)
            elif (w.grid_info()['row']-1 == args[4] * 2 and w.grid_info()['column'] == args[5] * 2 + 1):
                w.config(text = '||')
                zidovi.append(w)
        else:
            if (w.grid_info()['row']-1 == args[0] * 2 + 1 and w.grid_info()['column'] == args[1] * 2):
                w.config(text = '=')
                zidovi.append(w)
                label = ttk.Label(frame, text='=', width=3)
                zidovi.append(label)
                label.grid(row = args[0] * 2 + 2, column=args[1] * 2 + 1)
            elif (w.grid_info()['row']-1 == args[2] * 2 + 1 and w.grid_info()['column'] == args[3] * 2):
                w.config(text = '=')
                zidovi.append(w)

def iscrtajPesaka(args: list[int], fields: list[Label], b: list[int]):
    for field in fields:
        if (args[2] < 3):
            if (field.cget("text") == ('X' + str(args[2]))):
                if (int(field.grid_info()['row'] - 1) < 19 and int(field.grid_info()['column']) < 19):
                    field.config(text = (str(int((field.grid_info()['row']-1)/2)) + str(int(field.grid_info()['column']/2))))
                if (int(field.grid_info()['row'] - 1) > 19 and int(field.grid_info()['column']) < 19):
                    field.config(text = (str(chr(int((field.grid_info()['row']-1)/2 + 55))) + str(int(field.grid_info()['column']/2))))
                if (int(field.grid_info()['row'] - 1) < 19 and int(field.grid_info()['column']) > 19):
                    field.config(text = (str(int((field.grid_info()['row']-1)/2)) + str(chr(int(field.grid_info()['column']/2 + 55)))))
                if (int(field.grid_info()['row'] - 1) > 19 and int(field.grid_info()['column']) > 19):
                    field.config(text = (str(chr(int((field.grid_info()['row']-1)/2 + 55))) + str(chr(int(field.grid_info()['column']/2 + 55)))))
                if (args[2] == 1):
                    b[0] = args[0]
                    b[1] = args[1]
                else:
                    b[2] = args[0]
                    b[3] = args[1]
            elif ((int(field.grid_info()['row']) - 1)/2 == args[0] and field.grid_info()['column']/2 == args[1]):
                field.config(text = 'X' + str(args[2]))
        else:
            if (field.cget("text") == ('O' + str(args[2] - 2))):
                field.config(text = (str(int(field.grid_info()['row']-1)/2) + str(int(field.grid_info()['column']/2))))
                if (args[2] == 3):
                    b[4] = args[0]
                    b[5] = args[1]
                else:
                    b[6] = args[0]
                    b[7] = args[1]
            elif ((int(field.grid_info()['row']) - 1)/2 == args[0] and field.grid_info()['column']/2 == args[1]):
                field.config(text = ('O' + str(args[2] % 2)))

def upamtiPocetnoStanje(fields: list[Label], walls: list[Label], zidovi: list[Label], options: Frame, tableSizeN: StringVar, tableSizeM: StringVar, numberOfWalls: StringVar, 
firstPlayer: StringVar, frame: Frame, inPos1: Entry, inPos2: Entry, label1: Label, label2: Label, ts0: OptionMenu, ts1: OptionMenu, 
ts2: OptionMenu, ts3: OptionMenu, buttonStart: Button, a: list[int], b:list[int]):

    n = int(tableSizeN.get())*2+3
    m = int(tableSizeM.get())*2+3

    numOfWalls = int(numberOfWalls.get())

    if (firstPlayer.get() == "Korisnik"):
        firstPlay = int(0)
    else: firstPlay = int(1)

    Pesak1 = inPos1.get().split(sep=" ", maxsplit=5)

    Pesak2 = inPos2.get().split(sep=" ", maxsplit=5)

    a.append(n)
    a.append(m)
    a.append(numOfWalls)
    a.append(firstPlay)
    p11 = int(Pesak1[0])
    p12 = int(Pesak1[1])
    p21 = int(Pesak2[0])
    p22 = int(Pesak2[1])
    if (p11 * 2 <= n - 3 and p11 >= 1):
        a.append(p11)
    else:
        messagebox.showinfo(title='Lose koordinate', message='Vrsta za poziciju pesaka mora biti u opsegu 1 do ' + str((n - 3) / 2))
        a.clear()
        return
    if (p12 * 2 <= m - 3  and p12 >= 1):
        a.append(p12)
    else:
        messagebox.showinfo(title='Lose koordinate', message='Kolona za poziciju pesaka mora biti u opsegu 1 do ' + str((m - 3) / 2))
        a.clear()
        return
    if (p21 * 2 <= n - 3  and p21 >= 1):
        a.append(p21)
    else:
        messagebox.showinfo(title='Lose koordinate', message='Vrsta za poziciju pesaka mora biti u opsegu 1 do ' + str((n - 3) / 2))
        a.clear()
        return
    if (p22 * 2 <= m - 3  and p22 >= 1):
        a.append(p22)
    else:
        messagebox.showinfo(title='Lose koordinate', message='Kolona za poziciju pesaka mora biti u opsegu 1 do ' + str((m - 3) / 2))
        a.clear()
        return
    
    c: list[int] = []
    d: list[int] = []
    for x in range(1, int(tableSizeN.get())):
        c.append(x)
    for x in range(1, int(tableSizeM.get())):
        d.append(x)
    x1 = random.choice(c)
    x2 = random.choice(d)
    x3 = random.choice(c)
    x4 = random.choice(d)
    a.append(x1)
    a.append(x2)
    a.append(x3)
    a.append(x4)
    while((x1 == p11 and x2 == p12) or (x1 == p21 and x2 == p22)):
        x1 = random.choice(c)
        x2 = random.choice(d)
        a[8] = x1
        a[9] = x2
    while((x3 == p11 and x4 == p12) or (x3 == p21 and x4 == p22) or (x3 == x1 and x4 == x2)):
        x3 = random.choice(c)
        x4 = random.choice(d)
        a[10] = x3
        a[11] = x4
    print(x1, x2, x3, x4)
    #print(a[8])
    #print(a[9])
    #print(a[10])
    #print(a[11])
    #print(c)
    #print(d)
    
    inPos1.pack_forget()
    inPos2.pack_forget()
    label1.pack_forget()
    label2.pack_forget()
    ts0.pack_forget()
    ts1.pack_forget()
    ts2.pack_forget()
    ts3.pack_forget()
    buttonStart.pack_forget()

    #koordinate X1
    b.append(a[4])
    b.append(a[5])
    #koordinate X2
    b.append(a[6])
    b.append(a[7])
    #koordinate O1
    b.append(a[8])
    b.append(a[9])
    #koordinate O2
    b.append(a[10])
    b.append(a[11])
    #plavi zidovi čoveka
    b.append(a[2])
    #zeleni zidovi čoveka
    b.append(a[2])
    #plavi zidovi računara
    b.append(a[2])
    #zeleni zidovi računara
    b.append(a[2])

    b.append(0)
    b.append(firstPlay)

    iscrtajTablu(a[0], a[1], frame, fields, walls, a[4], a[5], a[6], a[7], a[8], a[9], a [10], a[11])
    labelMove = Label(options, text="Unesite indeks pesaka i nove koordinate:")
    labelMove.pack(side=LEFT)
    entryIndex = Entry(options, fg="grey", bg="white", width=5)
    entryIndex.pack(side=LEFT)
    entryCoor = Entry(options, fg="grey", bg="white", width=5)
    entryCoor.pack(side=LEFT)
    if (firstPlay == 1):
        potezRacunara(b, 1, 1, zidovi, 0, fields, a, walls, frame, buttonStart)
    buttonStart = ttk.Button(options, text="Play", command=lambda: preuzimanjePromena(frame, entryIndex, entryCoor, labelMove, a, b, fields, walls, zidovi, buttonStart))
    buttonStart.pack(side=LEFT)

def upamtiPocetnoStanje2(fields: list[Label], walls: list[Label], zidovi: list[Label], options: Frame, tableSizeN: StringVar, tableSizeM: StringVar, numberOfWalls: StringVar, frame: Frame, inPos1: Entry, inPos2: Entry, inPos3: Entry, inPos4: Entry, label1: Label, label2: Label, label3: Label, label4: Label, ts0: OptionMenu, ts1: OptionMenu, 
ts2: OptionMenu, buttonStart: Button, a: list[int], b:list[int]):

    n = int(tableSizeN.get())*2+3
    m = int(tableSizeM.get())*2+3

    numOfWalls = int(numberOfWalls.get())

    Pesak1 = inPos1.get().split(sep=" ", maxsplit=5)

    Pesak2 = inPos2.get().split(sep=" ", maxsplit=5)

    Pesak3 = inPos3.get().split(sep=" ", maxsplit=5)

    Pesak4 = inPos4.get().split(sep=" ", maxsplit=5)

    a.append(n)
    a.append(m)
    a.append(numOfWalls)
    a.append(0)
    p11 = int(Pesak1[0])
    p12 = int(Pesak1[1])
    p21 = int(Pesak2[0])
    p22 = int(Pesak2[1])
    if (p11 * 2 <= n - 3 and p11 >= 1):
        a.append(p11)
    else:
        messagebox.showinfo(title='Lose koordinate', message='Vrsta za poziciju pesaka mora biti u opsegu 1 do ' + str(n))
        a.clear()
        return
    if (p12 * 2 <= m - 3  and p12 >= 1):
        a.append(p12)
    else:
        messagebox.showinfo(title='Lose koordinate', message='Kolona za poziciju pesaka mora biti u opsegu 1 do ' + str(m))
        a.clear()
        return
    if (p21 * 2 <= n - 3  and p21 >= 1):
        a.append(p21)
    else:
        messagebox.showinfo(title='Lose koordinate', message='Vrsta za poziciju pesaka mora biti u opsegu 1 do ' + str(n))
        a.clear()
        return
    if (p22 * 2 <= m - 3  and p22 >= 1):
        a.append(p22)
    else:
        messagebox.showinfo(title='Lose koordinate', message='Kolona za poziciju pesaka mora biti u opsegu 1 do ' + str(m))
        a.clear()
        return
    p31 = int(Pesak3[0])
    p32 = int(Pesak3[1])
    p41 = int(Pesak4[0])
    p42 = int(Pesak4[1])
    if (p31 * 2 <= n - 3 and p31 >= 1):
        a.append(p31)
    else:
        messagebox.showinfo(title='Lose koordinate', message='Vrsta za poziciju pesaka mora biti u opsegu 1 do ' + str(n))
        a.clear()
        return
    if (p32 * 2 <= m - 3  and p32 >= 1):
        a.append(p32)
    else:
        messagebox.showinfo(title='Lose koordinate', message='Kolona za poziciju pesaka mora biti u opsegu 1 do ' + str(m))
        a.clear()
        return
    if (p41 * 2 <= n - 3  and p41 >= 1):
        a.append(p41)
    else:
        messagebox.showinfo(title='Lose koordinate', message='Vrsta za poziciju pesaka mora biti u opsegu 1 do ' + str(n))
        a.clear()
        return
    if (p42 * 2 <= m - 3  and p42 >= 1):
        a.append(p42)
    else:
        messagebox.showinfo(title='Lose koordinate', message='Kolona za poziciju pesaka mora biti u opsegu 1 do ' + str(m))
        a.clear()
        return
    
    inPos1.pack_forget()
    inPos2.pack_forget()
    inPos3.pack_forget()
    inPos4.pack_forget()
    label1.pack_forget()
    label2.pack_forget()
    label3.pack_forget()
    label4.pack_forget()
    ts0.pack_forget()
    ts1.pack_forget()
    ts2.pack_forget()
    buttonStart.pack_forget()

    #koordinate X1
    b.append(a[4])
    b.append(a[5])
    #koordinate X2
    b.append(a[6])
    b.append(a[7])
    #koordinate O1
    b.append(a[8])
    b.append(a[9])
    #koordinate O2
    b.append(a[10])
    b.append(a[11])
    #plavi zidovi 1. čoveka
    b.append(a[2])
    #zeleni zidovi 1. čoveka
    b.append(a[2])
    #plavi zidovi 2. čoveka
    b.append(a[2])
    #zeleni zidovi 2. čoveka
    b.append(a[2])

    b.append(1)
    b.append(0)

    iscrtajTablu(a[0], a[1], frame, fields, walls, a[4], a[5], a[6], a[7], a[8], a[9], a [10], a[11])
    labelMove = Label(options, text="Unesite indeks pesaka i nove koordinate:")
    labelMove.pack(side=LEFT)
    entryIndex = Entry(options, fg="grey", bg="white", width=5)
    entryIndex.pack(side=LEFT)
    entryCoor = Entry(options, fg="grey", bg="white", width=5)
    entryCoor.pack(side=LEFT)
    buttonStart = ttk.Button(options, text="Play", command=lambda: preuzimanjePromena(frame, entryIndex, entryCoor, labelMove, a, b, fields, walls, zidovi, buttonStart))
    buttonStart.pack(side=LEFT)

def izborPocetnihParametara(root: Tk, frame: Frame, a: list[int], b: list[int], fields: list[Label], walls: list[Label], zidovi: list[Label]):
    options = ttk.Frame(frame, padding=10)
    options.grid(columnspan = 100)
    ttk.Label(options, text="Dobrodošli u Blockade!").pack(side=LEFT)

    tableSizeN = StringVar(options)
    tableSizeN.set("Vrsta?")
    ts0 = OptionMenu(options, tableSizeN, "4", "6", "8", "10", "12", "14", "16", "18", "20", "22", "24")
    ts0.pack(side=LEFT)
    tableSizeM = StringVar(options)
    tableSizeM.set("Kolona?")
    ts1 = OptionMenu(options, tableSizeM, "3", "5", "7", "9", "11", "13", "15", "17", "19", "21")
    ts1.pack(side=LEFT)

    numberOfWalls = StringVar(root)
    numberOfWalls.set("Zidova?")
    ts2 = OptionMenu(options, numberOfWalls, "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18")
    ts2.pack(side=LEFT)

    typeOfGame = StringVar(root)
    typeOfGame.set('Izaberite tip igre')
    ts4 = OptionMenu(options, typeOfGame, "Čovek vs Čovek", "Čovek vs Računar")
    ts4.pack(side=LEFT)

    btnTypeOfGame = ttk.Button(options, text="Izaberi tip igre", command=lambda: iscrtajIzbor(root, options, frame, btnTypeOfGame, ts0, ts1, ts2, ts4, tableSizeN, tableSizeM, numberOfWalls, typeOfGame, fields, walls, zidovi, a, b))
    btnTypeOfGame.pack(side=LEFT)
    ttk.Button(options, text="Quit", command=root.destroy).pack(side=LEFT)

def preuzimanjePromena(frame: Frame, entryIndex: Entry, entryCoor: Entry, labelMove: Label, a: list[int], b: list[int], fields: list[Label],
walls: list[Label], zidovi: list[Label], buttonStart: Button):
    buttonStart.pack_forget()
    tekstLabele : StringVar
    tekstLabele = labelMove.cget('text')
    if(tekstLabele == "Unesite indeks pesaka i nove koordinate:"):
        indexPesaka : int
        indexPesaka = int(entryIndex.get())
        koordX : int
        koordY : int
        koordinataX : StringVar
        koordinataY : StringVar
        x = entryCoor.get()
        koordinataY = x[1]
        koordinataX = x[0]
        if(koordinataX < "1" or koordinataX > "9"):
            koordX = (int(ord(koordinataX)) - 55)
        else:
            koordX= int(koordinataX)
        if(koordinataY < "1" or koordinataY > "9"):
            koordY=(int(ord(koordinataY)) - 55)
        else:
            koordY=int(koordinataY)
        if (b[12] == 0):
            if (proveraPromenePesaka(koordX, koordY, indexPesaka, b, zidovi, fields, a)):
                iscrtajPesaka([koordX, koordY, indexPesaka], fields, b)
            else:
                messagebox.showinfo(title='Lose koordinate', message='Pesak X' + str(indexPesaka) + ' ne moze biti pomeren na unetu poziciju. Unesite nove koordinate')
                buttonStart.pack(side = LEFT)
                return
        else:
            if (b[13] == 0):
                if (proveraPromenePesaka(koordX, koordY, indexPesaka, b, zidovi, fields, a)):
                    iscrtajPesaka([koordX, koordY, indexPesaka], fields, b)
                else:
                    messagebox.showinfo(title='Lose koordinate', message='Pesak X' + str(indexPesaka) + ' ne moze biti pomeren na unetu poziciju. Unesite nove koordinate')
                    buttonStart.pack(side = LEFT)
                    return
            else:
                if (proveraPromenePesaka(koordX, koordY, indexPesaka + 2, b, zidovi, fields, a)):
                    iscrtajPesaka([koordX, koordY, indexPesaka + 2], fields, b)
                else:
                    messagebox.showinfo(title='Lose koordinate', message='Pesak O' + str(indexPesaka) + ' ne moze biti pomeren na unetu poziciju. Unesite nove koordinate')
                    buttonStart.pack(side = LEFT)
                    return
        x = krajnjeStanje(b, a)
        if (x[0]):
            if (x[1] == 1 or x[1] == 2):
                if (b[12] == 0):
                    messagebox.showinfo('Igra je zavrsena', 'Cestitamo, pobedili ste!!!')
                else: messagebox.showinfo('Igra je zavrsena', 'Cestitamo, pobedio je igrac 1!!!')
                buttonStart.pack_forget()
                return
            else:
                if (b[12] == 0):
                    messagebox.showinfo('Igra je zavrsena', 'Dobro ste igrali, ali racunar je bio bolji!!!')
                else: messagebox.showinfo('Igra je zavrsena', 'Cestitamo, pobedio je igrac 2!!!')
                buttonStart.pack_forget()
                return
        labelMove.config(text = "Unesite boju zida kog postavljate i 4 polja između kojih se zid nalazi sa razmacima:")
        buttonStart.pack(side = LEFT)
        entryCoor.delete(0, END)
        entryIndex.delete(0, END)
    else:
        buttonStart.pack_forget()
        if (b[12] == 0):
            if ((imaLiZidova(0, 0, b) == False) and (imaLiZidova(0, 1, b) == False)):
                labelMove.config(text = "Unesite indeks pesaka i nove koordinate:")
                potezRacunara(b, 1, 1, zidovi, 0, fields, a, walls, frame, buttonStart)
                buttonStart.pack(side = LEFT)
                return
        else:
            if (b[13] == 0):
                if ((imaLiZidova(0, 0, b) == False) and (imaLiZidova(0, 1, b) == False)):
                    labelMove.config(text = "Unesite indeks pesaka i nove koordinate:")
                    buttonStart.pack(side = LEFT)
                    return
            else:
                if ((imaLiZidova(1, 0, b) == False) and (imaLiZidova(1, 1, b) == False)):
                    labelMove.config(text = "Unesite indeks pesaka i nove koordinate:")
                    buttonStart.pack(side = LEFT)
                    return
        bojaZida : int
        boja : StringVar
        boja = entryIndex.get()
        if(boja == "plavi"):
            bojaZida = 0
        else:
            bojaZida = 1
        koord1 : int
        koord2 : int
        koord3 : int
        koord4 : int
        koord5 : int
        koord6 : int
        koord7 : int
        koord8 : int
        koordinata1 : StringVar
        koordinata2 : StringVar
        koordinata3 : StringVar
        koordinata4 : StringVar
        koordinata5 : StringVar
        koordinata6 : StringVar
        koordinata7 : StringVar
        koordinata8 : StringVar
        koordinate = entryCoor.get().split(' ', 5)
        koordinate78 = koordinate.pop()
        koordinate56 = koordinate.pop()
        koordinate34 = koordinate.pop()
        koordinate12 = koordinate.pop()
        koordinata1 = koordinate12[0]
        koordinata2 = koordinate12[1]
        koordinata3 = koordinate34[0]
        koordinata4 = koordinate34[1]
        koordinata5 = koordinate56[0]
        koordinata6 = koordinate56[1]
        koordinata7 = koordinate78[0]
        koordinata8 = koordinate78[1]
        if(koordinata1 < "1" or koordinata1 > "9"):
            koord1 = (int(ord(koordinata1)) - 55)
        else:
            koord1= int(koordinata1)
        if(koordinata2 < "1" or koordinata2 > "9"):
            koord2=(int(ord(koordinata2)) - 55)
        else:
            koord2=int(koordinata2)
        if(koordinata3 < "1" or koordinata3 > "9"):
            koord3 = (int(ord(koordinata3)) - 55)
        else:
            koord3= int(koordinata3)
        if(koordinata4 < "1" or koordinata4 > "9"):
            koord4=(int(ord(koordinata4)) - 55)
        else:
            koord4=int(koordinata4)
        if(koordinata5 < "1" or koordinata5 > "9"):
            koord5 = (int(ord(koordinata5)) - 55)
        else:
            koord5= int(koordinata5)
        if(koordinata6 < "1" or koordinata6 > "9"):
            koord6=(int(ord(koordinata6)) - 55)
        else:
            koord6=int(koordinata6)
        if(koordinata7 < "1" or koordinata7 > "9"):
            koord7 = (int(ord(koordinata7)) - 55)
        else:
            koord7= int(koordinata7)
        if(koordinata8 < "1" or koordinata8 > "9"):
            koord8=(int(ord(koordinata8)) - 55)
        else:
            koord8=int(koordinata8)
        if b[12] == 0:
            if (imaLiZidova(0, bojaZida, b)):
                if (proveraPromeneZida([koord1, koord2, koord3, koord4, koord5, koord6, koord7, koord8, bojaZida], fields, zidovi, a, walls, frame)):
                    iscrtajZid([koord1, koord2, koord3, koord4, koord5, koord6, koord7, koord8, bojaZida], frame, walls, zidovi)
                else:
                    messagebox.showinfo(title='Lose koordinate', message='Zid ne moze biti postavljen na uneto mesto. Unesite nove koordinate')
                    buttonStart.pack(side = LEFT)
                    return
            else:
                messagebox.showinfo(title='Nema postavljanja zida', message='Nemate zidove u izabranoj boji')
                buttonStart.pack(side = LEFT)
                return
        else:
            if (b[13] == 0):
                if (imaLiZidova(0, bojaZida, b)):
                    if (proveraPromeneZida([koord1, koord2, koord3, koord4, koord5, koord6, koord7, koord8, bojaZida], fields, zidovi, a, walls, frame)):
                        iscrtajZid([koord1, koord2, koord3, koord4, koord5, koord6, koord7, koord8, bojaZida], frame, walls, zidovi)
                    else:
                        messagebox.showinfo(title='Lose koordinate', message='Zid ne moze biti postavljen na uneto mesto. Unesite nove koordinate')
                        buttonStart.pack(side = LEFT)
                        return
                else:
                    messagebox.showinfo(title='Nema postavljanja zida', message='Nemate zidove u izabranoj boji')
                    buttonStart.pack(side = LEFT)
                    return
            else:
                if (imaLiZidova(1, bojaZida, b)):
                    if (proveraPromeneZida([koord1, koord2, koord3, koord4, koord5, koord6, koord7, koord8, bojaZida], fields, zidovi, a, walls, frame)):
                        iscrtajZid([koord1, koord2, koord3, koord4, koord5, koord6, koord7, koord8, bojaZida], frame, walls, zidovi)
                    else:
                        messagebox.showinfo(title='Lose koordinate', message='Zid ne moze biti postavljen na uneto mesto. Unesite nove koordinate')
                        buttonStart.pack(side = LEFT)
                        return
                else:
                    messagebox.showinfo(title='Nema postavljanja zida', message='Nemate zidove u izabranoj boji')
                    buttonStart.pack(side = LEFT)
                    return
        if (b[12] == 0):
            b[13] = 1
            potezRacunara(b, 1, 1, zidovi, 0, fields, a, walls, frame, buttonStart)
            b[13] = 0
        labelMove.config(text = "Unesite indeks pesaka i nove koordinate:")
        buttonStart.pack(side = LEFT)
        entryCoor.delete(0, END)
        entryIndex.delete(0, END)
        if (b[12] == 1):
            b[13] = (b[13] + 1) % 2