import socket
import datetime
import time
import threading
import tkinter
from tkinter import *

HOST = '127.0.0.1'
PORT = 1476

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

svePoruke = {}
zahtev = ""



window = Tk()
window.minsize(350,650)
window.maxsize(350,650)

lstBox4 = Listbox(window)
lstBox4.place(x=0, y=0, width=350, height=650)

def komunikacija(lstBox4):
    conn, addr = s.accept()
    while True:
        zahtev = conn.recv(1024).decode("UTF-8")
        zahtev = str(zahtev)

        if zahtev == "1":


            vreme = datetime.datetime.now()

            vreme = str(vreme)

            p = "Vreme: " + vreme

            conn.send(p.encode("UTF-8"))
            n = conn.recv(1024).decode("UTF-8")
            lstBox4.insert(0, n + "| Vreme")



        elif zahtev == "2":
            p = conn.recv(1024).decode("UTF-8")
            print(p)

            lstBox4.insert(0,p)
            conn.send(p.encode("UTF-8"))




        else:
            p = conn.recv(1024).decode("UTF-8")
            lstBox4.insert(0, p + "| Kraj")
            break



while True:

    threading.Thread(target=komunikacija, args=(lstBox4,)).start()

    window.mainloop()


