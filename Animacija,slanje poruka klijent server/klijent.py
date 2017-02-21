
import socket
import time
import threading
import tkinter
from tkinter import *
from tkinter import messagebox

HOST = '127.0.0.1'
PORT = 1476

z=0
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print("Connected on server")


svePoruke=[]

def animacija(canvas, arc, arc2):

    k = 1
    i = 21
    while z != 1:
        canvas.itemconfig(arc2, start = i, extent = 180 - i)
        canvas.itemconfig(arc, extent = i)
        if i == 180:
            i = 0
        i += k
        time.sleep(0.01)

def posalji():
    global z
    zahtev = int(rbVar.get())
    if zahtev == 1:
        print("Vreme")

        s.send("1".encode("UTF-8"))

        p = s.recv(1024).decode("UTF-8")
        p = str(p)
        lbox2.insert(0, p)
        s.send(p.encode("UTF-8"))

    elif zahtev == 2:
        s.send("2".encode("UTF-8"))

        p=txtVar.get()
        print(p)
        if len(lbox1.curselection()) !=  0 and p !="":

            p+= " salje " + lbox1.get(lbox1.curselection()) + "u "

            if cb1Var.get() == 1:
                p += "veliki "
            if cb2Var.get() == 1:
                p += "pozdrav!"


            s.send(p.encode("UTF-8"))
            n = s.recv(1024).decode("UTF-8")
            lbox2.insert(0, n)
        else:
            messagebox.showinfo("Greska!", "Morate uneti posaljioca i selektovati primaoca!")
            p += " -- Morate uneti posaljioca i selektovati primaoca !"
            s.send(p.encode("UTF-8"))
            n = s.recv(1024).decode("UTF-8")
            lbox2.insert(0, n)




    else:
        z=1
        n = txtVar.get()
        s.send("Kraj".encode("UTF-8"))
        s.send(n.encode("UTF-8"))
        s.close()








root = tkinter.Tk()

canvas = tkinter.Canvas(root, width = 300, height = 200, bg = "yellow")
arc = canvas.create_arc((10, 10, 250, 250), start = 0, extent = 20, fill = "red")
arc2 = canvas.create_arc((10, 10, 250, 250), start = 20, extent = 160, fill = "green")
canvas.grid(row = 0, column = 0)

t = threading.Thread(target=animacija, args=(canvas, arc, arc2))
t.start()

lbl1 = tkinter.Label(root, text = "Ime", bg='blue',width='50',fg='white')
lbl1.grid(row = 1, column = 0)

txtVar = StringVar()
txt = tkinter.Entry(root, textvariable = txtVar)
txt.grid(row = 2, column = 0)

lbl2 = tkinter.Label(root, text = "Zahtev")
lbl2.grid(row = 3, column = 0, sticky = W)

rbVar = IntVar()
rb1 = tkinter.Radiobutton(root, text = "Vreme", variable = rbVar, value = "1")
rb1.grid(row = 4, column = 0, sticky = W)
rb1.select()

rb2 = tkinter.Radiobutton(root, text = "Poruka", variable = rbVar, value = "2")
rb2.grid(row = 5, column = 0, sticky = W)





rb3 = tkinter.Radiobutton(root, text = "Kraj", variable = rbVar, value = "0")
rb3.grid(row = 10, column = 0, sticky = W)


lbox1 = tkinter.Listbox(root, height = 2,width='33')
lbox1.insert(END, "Milan")
lbox1.insert(END, "Nenad")
lbox1.grid(row = 6, column = 0,sticky= E)

cb1Var = IntVar()
cb1 = tkinter.Checkbutton(root, text = "Veliki", onvalue = 1, offvalue = 0, variable = cb1Var,width='30',bg='yellow')
cb1.grid(row = 7, column = 0)

cb2Var = IntVar()
cb2 = tkinter.Checkbutton(root, text = "Pozdrav", onvalue = 1, offvalue = 0, variable = cb2Var,width='30',bg='orange')
cb2.grid(row = 8, column = 0)



btn = Button(root, text = "Posalji zahtev serveru", command = posalji, bg='lightgreen', width='50')
btn.grid(row = 11, column = 0)

labela1= tkinter.Label(text="Odgovor sa servera")
labela1.grid(row=12,column=0)

f = Frame(root, padx = 10, pady = 10)
f.grid(row = 13, column = 0)
scrollbar = Scrollbar(f)
scrollbar.pack( side = RIGHT, fill=Y )
lbox2 = Listbox(f, height = 5, width = 50, yscrollcommand = scrollbar.set)
scrollbar.config( command = lbox2.yview )
lbox2.pack(side = LEFT, fill = BOTH)


root.mainloop()