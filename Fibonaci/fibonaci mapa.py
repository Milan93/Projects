from tkinter import *
from tkinter import messagebox
root = Tk()




def fib(n):
    if n<2:
        return n
    return fib(n-2)+ fib(n-1)


def done():
    global a

    lstbx.delete(0, END)
    start = 1
    check = var2.get()

    if check.isalpha() or check == "":
        messagebox.showinfo("Warning", "Please enter the number !")
    else:
        end = int(var2.get())

        a=list(map(fib,range(start,end+1)))
        for i in a:
         lstbx.insert(END, i)


label = Label( root, text="           Welcome! Please enter the length of the Fibonacci Numbers             ", relief=RAISED )
label.pack(side=TOP)

frame = Frame(root,width="30",height="30")
frame.pack()

var2 = StringVar()

entry= Entry(root,textvariable=var2)
entry.pack()


btn = Button(root,command=done,text= "Calculate")
btn.pack()


frame1 = Frame(root,width="50",height="50")
frame1.pack()

scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill=Y )
lstbx=Listbox(root,width="50",height="20",yscrollcommand = scrollbar.set)

lstbx.pack()
scrollbar.config( command = lstbx.yview )


root.mainloop()





