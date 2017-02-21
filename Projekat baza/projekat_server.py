import socket

import threading
import tkinter
from tkinter import *

HOST = '127.0.0.1'
PORT = 1456

window = Tk()
window.minsize(350,650)
window.maxsize(350,650)


lbl1 = tkinter.Label(window,text = 'Unesite Ime')
lbl1.grid(row = 1, column = 0)

txtVar = StringVar()
txt = tkinter.Entry(window, textvariable = txtVar)
txt.grid(row = 1, column = 1)




s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

def komunikacija():
    conn, addr = s.accept()
    while True:
        zahtev = conn.recv(1024).decode("UTF-8")
        zahtev = str(zahtev)

        if zahtev == "1":

            upis = txtVar.get()


            conn.send(upis.encode("UTF-8"))

        if zahtev == "2":
                upis = txtVar.get()
                if upis == "":
                    x ='prazno'
                    conn.send(x.encode("UTF-8"))
                else:

                    conn.send(upis.encode("UTF-8"))







while True:

    threading.Thread(target=komunikacija,).start()

    window.mainloop()


