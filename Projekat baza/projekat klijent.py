import time
import tkinter
from tkinter import *
import sqlite3
import sys
import socket
import threading


HOST = '127.0.0.1'
PORT = 1456


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print("Connected on server")




def izvodjaci():
    try:

        con = None
        con = sqlite3.connect('chinook.db')

        cur = con.cursor()


        cur.execute('SELECT * from artists')
        data = cur.fetchall()


        lbox2.delete(0, END)
        for i in data:
            lbox2.insert(END, i)
      

    except sqlite3.Error:
        print("Error :",  sqlite3.Error)
        sys.exit(1)
    finally:

        if con:
            con.close()

def provera ():

    while True:

        try:

            con = None
            con = sqlite3.connect('chinook.db')

            cur = con.cursor()

            cur.execute('SELECT * from artists')
            data = cur.fetchall()
            x= len(data)

            p = data[x-1]


            lbox3.insert(0,"Trenutno postoji " + str(p[0]) + " izvodjaca, poslednji je : " + str(p[1]))


        except sqlite3.Error:
            print("Error :", sqlite3.Error)
            sys.exit(1)
        finally:

            if con:
                con.close()
                time.sleep(2)




def invoice():
    try:

        con = None
        con = sqlite3.connect('chinook.db')

        cur = con.cursor()



        cur.execute('SELECT * from invoices')
        data = cur.fetchall()

        lbox2.delete(0, END)
        for i in data:
            lbox2.insert(END, i)

    except sqlite3.Error:
        print("Error :",  sqlite3.Error)
        sys.exit(1)
    finally:

        if con:
            con.close()
def prikazi_pesme():
    try:

        con = None
        con = sqlite3.connect('chinook.db')

        cur = con.cursor()



        cur.execute('SELECT * from tracks')
        data = cur.fetchall()

        lbox2.delete(0, END)
        for i in data:
            lbox2.insert(END, i)

    except sqlite3.Error:
        print("Error :",  sqlite3.Error)
        sys.exit(1)
    finally:

        if con:
            con.close()

def sadrzaj_plejliste():
    try:

        con = None
        con = sqlite3.connect('chinook.db')

        cur = con.cursor()

        cur.execute('SELECT DISTINCT P.Name, T.Name FROM playlists P INNER JOIN playlist_track PT ON P.PlaylistID = PT.PlaylistID INNER JOIN tracks T ON PT.TrackID = T.TrackID')
        data = cur.fetchall()

        lbox2.delete(0, END)
        for i in data:
            lbox2.insert(END, i)

    except sqlite3.Error:
        print("Error :",  sqlite3.Error)
        sys.exit(1)
    finally:

        if con:
            con.close()
def musterija():
    try:

        con = None
        con = sqlite3.connect('chinook.db')

        cur = con.cursor()


        cur.execute('SELECT * from customers')
        data = cur.fetchall()

        lbox2.delete(0, END)
        for i in data:
            lbox2.insert(END, i)




    except sqlite3.Error:
        print("Error :",  sqlite3.Error)
        sys.exit(1)
    finally:

        if con:
            con.close()
def zanr():
    try:

        con = None
        con = sqlite3.connect('chinook.db')

        cur = con.cursor()

        cur.execute('SELECT A.Title,G.Name FROM albums A INNER JOIN tracks T on A.AlbumID = T.TrackID INNER JOIN genres G ON G.GenreID = T.TrackID')
        data = cur.fetchall()

        lbox2.delete(0, END)
        for i in data:
            lbox2.insert(END, i)




    except sqlite3.Error:
        print("Error :",  sqlite3.Error)
        sys.exit(1)
    finally:

        if con:
            con.close()


def dodavanje_izvodjaca():
    try:

        con = None
        con = sqlite3.connect('chinook.db')

        cur = con.cursor()



        cur.execute("INSERT INTO artists(Name) VALUES ('%s')"%(txtVar72.get()))
        con.commit()


        lbox2.delete(0, END)
        k = 'Dodavanje uspesno!'
        lbox2.insert(END, k)
        txtVar72.set('')



    except sqlite3.Error:
        print("Error :",  sqlite3.Error)
        sys.exit(1)
    finally:

        if con:
            con.close()

def dodavanje_musterije():
    try:

        con = None
        con = sqlite3.connect('chinook.db')

        cur = con.cursor()

        cur.execute("INSERT INTO customers(FirstName, LastName, Company, Address, City, State, Country, PostalCode, Phone, Fax, Email,SupportRepID)VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%d')"
                    %(txtVar.get(),txtVar1.get(),txtVar2.get(),txtVar4.get(),txtVar5.get(),txtVar6.get(),txtVar7.get(),txtVar8.get(),txtVar9.get(),txtVar10.get(),txtVar3.get(),15))
        con.commit()


        lbox2.delete(0, END)
        k = 'Dodavanje uspesno!'
        lbox2.insert(END, k)
        txtVar.set('')
        txtVar1.set('')
        txtVar2.set('')
        txtVar3.set('')
        txtVar4.set('')
        txtVar5.set('')
        txtVar6.set('')
        txtVar7.set('')
        txtVar8.set('')
        txtVar9.set('')
        txtVar10.set('')




    except sqlite3.Error:
        print("Error :",  sqlite3.Error)
        sys.exit(1)
    finally:

        if con:
            con.close()
def dodavanje_pesama():
    try:

        con = None
        con = sqlite3.connect('chinook.db')

        cur = con.cursor()

        cur.execute(" INSERT INTO tracks(Name, AlbumID, MediaTypeID, GenreID,Composer, Milliseconds, Bytes, UnitPrice)"
                    "VALUES ('%s',%d, %d, %d,'%s','%s','%s','%s')"%(txtVar11.get(),50,50,50,txtVar12.get(),txtVar13.get(),txtVar14.get(),txtVar15.get()))
        con.commit()


        lbox2.delete(0, END)
        k = 'Dodavanje uspesno!'
        lbox2.insert(END, k)
        txtVar.set('')
        txtVar11.set('')
        txtVar12.set('')
        txtVar13.set('')
        txtVar14.set('')
        txtVar15.set('')





    except sqlite3.Error:
        print("Error :",  sqlite3.Error)
        sys.exit(1)
    finally:

        if con:
            con.close()


def dodavanje_server():
    zahtev = 1
    if zahtev == 1:


        s.send("1".encode("UTF-8"))

        p = s.recv(1024).decode("UTF-8")
        p = str(p)

        try:

            con = None
            con = sqlite3.connect('chinook.db')

            cur = con.cursor()



            cur.execute("INSERT INTO artists(Name) VALUES ('%s')"%(p))
            con.commit()


            lbox2.delete(0, END)
            k = 'Dodavanje uspesno!'
            lbox2.insert(END, k)
            txtVar.set('')



        except sqlite3.Error:
            print("Error :",  sqlite3.Error)
            sys.exit(1)
        finally:

            if con:
                con.close()


def provera_sa_servera():
    zahtev = 2
    if zahtev == 2:


        s.send("2".encode("UTF-8"))

        p = s.recv(1024).decode("UTF-8")
        p = str(p)


        try:

            con = None
            con = sqlite3.connect('chinook.db')

            cur = con.cursor()

            cur.execute('SELECT * from artists')
            data = cur.fetchall()
            lbox2.delete(0, END)

            if p != "prazno":

                for i in data:


                    if i[1] == p:

                        lbox2.insert(END, 'Postoji : ' + i [1])
                        break


                if lbox2.get([0]) == '':
                        lbox2.insert(END, 'Ne postoji takav izvodjac ! ('+ p + ')')
            else :
                lbox2.delete(0, END)
                lbox2.insert(0,'Morate uneti nesto na serveru')




        except sqlite3.Error:
            print("Error :",  sqlite3.Error)
            sys.exit(1)
        finally:

            if con:
                con.close()


root = tkinter.Tk()

f1= Frame(root, padx = 10, pady = 10)
f1.grid(row = 1, column = 1)

btn2 = Button(f1, text = "Prikaz musterija ", command = musterija, width='15')
btn2.grid(row = 24, column = 1)

btn7 = Button(f1, text = "Prikaz sadrzaja plejlisti ", command = sadrzaj_plejliste, width='20')
btn7.grid(row = 1, column = 1)

lbl1 = tkinter.Label(f1)
lbl1.grid(row = 2, column = 0)

btn1 = Button(f1, text = "Prikaz invoice ", command = invoice, width='15')
btn1.grid(row = 3, column = 0)


btn8 = Button(f1, text = "Prikaz albuma po zanrovima ", command = zanr, width='25')
btn8.grid(row = 3, column = 1)

lbl2 = tkinter.Label(f1)
lbl2.grid(row = 4, column = 0)

btn = Button(f1, text = "Prikaz izvodjaca ", command = izvodjaci, width='15')
btn.grid(row = 5, column = 0)

lbl3 = tkinter.Label(f1,)
lbl3.grid(row = 6, column = 0)

txtVar72 = StringVar()
txt = tkinter.Entry(f1, textvariable = txtVar72)
txt.grid(row = 7, column = 1)



btn4 = Button(f1, text = "Dodaj izvodjaca ",command = dodavanje_izvodjaca,  width='15')
btn4.grid(row = 7, column = 0)

lbl4 = tkinter.Label(f1)
lbl4.grid(row = 8, column = 1)


btn5 = Button(f1, text = "Dodaj izvodjaca sa servera ",command = dodavanje_server,  width='20')
btn5.grid(row = 9, column = 0)

lbl5 = tkinter.Label(f1)
lbl5.grid(row = 10, column = 1)

btn6 = Button(f1, text = "Provera izvodjaca sa servera ",command = provera_sa_servera,  width='20')
btn6.grid(row = 11, column = 0)

lbl6 = tkinter.Label(f1,text= '-------------------------------------------')
lbl6.grid(row = 12, column = 0)


#ENTRY ZA DODAVANJE MUSTERIJA
txtVar = StringVar()
txt = tkinter.Entry(f1, textvariable = txtVar)
txt.grid(row = 13, column = 1)
lbl7 = tkinter.Label(f1,text='First Name: ')
lbl7.grid(row = 13, column = 0)

txtVar1 = StringVar()
txt1 = tkinter.Entry(f1, textvariable = txtVar1)
txt1.grid(row = 14, column = 1)
lbl8 = tkinter.Label(f1,text='Last Name: ')
lbl8.grid(row = 14, column = 0)

txtVar2 = StringVar()
txt2 = tkinter.Entry(f1, textvariable = txtVar2)
txt2.grid(row = 15, column = 1)
lbl9 = tkinter.Label(f1,text='Company: ')
lbl9.grid(row = 15, column = 0)

txtVar3 = StringVar()
txt3 = tkinter.Entry(f1, textvariable = txtVar3)
txt3.grid(row = 16, column = 1)
lbl10 = tkinter.Label(f1,text='Email: ')
lbl10.grid(row = 16, column = 0)


txtVar4 = StringVar()
txt4 = tkinter.Entry(f1, textvariable = txtVar4)
txt4.grid(row = 17, column = 1)
lbl11 = tkinter.Label(f1,text='Address: ')
lbl11.grid(row = 17, column = 0)

txtVar5 = StringVar()
txt5 = tkinter.Entry(f1, textvariable = txtVar5)
txt5.grid(row = 18, column = 1)
lbl12 = tkinter.Label(f1,text='City: ')
lbl12.grid(row = 18, column = 0)

txtVar6 = StringVar()
txt6 = tkinter.Entry(f1, textvariable = txtVar6)
txt6.grid(row = 19, column = 1)
lbl13 = tkinter.Label(f1,text='State: ')
lbl13.grid(row = 19, column = 0)

txtVar7 = StringVar()
txt7 = tkinter.Entry(f1, textvariable = txtVar7)
txt7.grid(row = 20, column = 1)
lbl14 = tkinter.Label(f1,text='Country ')
lbl14.grid(row = 20, column = 0)

txtVar8 = StringVar()
txt8 = tkinter.Entry(f1, textvariable = txtVar8)
txt8.grid(row = 21, column = 1)
lbl15 = tkinter.Label(f1,text='Postal code: ')
lbl15.grid(row = 21, column = 0)

txtVar9 = StringVar()
txt9 = tkinter.Entry(f1, textvariable = txtVar9)
txt9.grid(row = 22, column = 1)
lbl16 = tkinter.Label(f1,text='Phone: ')
lbl16.grid(row = 22, column = 0)

txtVar10 = StringVar()
txt10 = tkinter.Entry(f1, textvariable = txtVar10)
txt10.grid(row = 23, column = 1)
lbl17 = tkinter.Label(f1,text='Fax: ')
lbl17.grid(row = 23, column = 0)


btn7 = Button(f1, text = "Dodaj musteriju",command = dodavanje_musterije,  width='20')
btn7.grid(row = 24, column = 0)

lbl7 = tkinter.Label(f1,text= '-------------------------------------------')
lbl7.grid(row = 25, column = 0)

txtVar11 = StringVar()
txt11 = tkinter.Entry(f1, textvariable = txtVar11)
txt11.grid(row = 26, column = 1)
lbl18 = tkinter.Label(f1,text='Name: ')
lbl18.grid(row = 26, column = 0)

txtVar12 = StringVar()
txt12 = tkinter.Entry(f1, textvariable = txtVar12)
txt12.grid(row = 27, column = 1)
lbl19 = tkinter.Label(f1,text='Composer: ')
lbl19.grid(row = 27, column = 0)

txtVar13 = StringVar()
txt13 = tkinter.Entry(f1, textvariable = txtVar13)
txt13.grid(row = 28, column = 1)
lbl20 = tkinter.Label(f1,text='Milliseconds: ')
lbl20.grid(row = 28, column = 0)

txtVar14 = StringVar()
txt14 = tkinter.Entry(f1, textvariable = txtVar14)
txt14.grid(row = 29, column = 1)
lbl21 = tkinter.Label(f1,text='Bytes: ')
lbl21.grid(row = 29, column = 0)

txtVar15 = StringVar()
txt15 = tkinter.Entry(f1, textvariable = txtVar15)
txt15.grid(row = 30, column = 1)
lbl22 = tkinter.Label(f1,text='UnitPrice: ')
lbl22.grid(row = 30, column = 0)

btn8 = Button(f1, text = "Dodaj pesmu",command = dodavanje_pesama,  width='20')
btn8.grid(row = 31, column = 0)

btn9 = Button(f1, text = "Prikazi pesme",command = prikazi_pesme,  width='20')
btn9.grid(row = 31, column = 1)


f = Frame(root, padx = 10, pady = 10)
f.grid(row = 1, column = 2)


scrollbar = Scrollbar(f)
scrollbar.pack( side = RIGHT, fill=Y )
lbox2 = Listbox(f, height = 50, width = 100, yscrollcommand = scrollbar.set)
scrollbar.config( command = lbox2.yview )
lbox2.pack(side = RIGHT, fill = BOTH)


f3 = Frame(root, padx = 10, pady = 10)
f3.grid(row = 1, column = 3,sticky=N)

lbox3 = Listbox(f3, height = 50, width = 60)
lbox3.grid(row=1,column=1,)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Prikaz", menu=filemenu)
filemenu.add_command(label="Izvodjaci", command=izvodjaci)
filemenu.add_command(label="Pesme", command=prikazi_pesme)
filemenu.add_command(label="Plejliste", command=sadrzaj_plejliste)
filemenu.add_command(label="Musterije", command=musterija)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

t1 = threading.Thread(target=provera, )
t1.start()
root.config(menu=menubar)
root.mainloop()