from tkinter import *
from tkinter import messagebox
import tkinter.font

root = Tk()

drawing_tool = NONE
left_but = "up"
x_pos, y_pos = NONE, NONE
x1_line_pt, y1_line_pt, x2_line_pt, y2_line_pt,= NONE, NONE,NONE, NONE


def pencil():
    global drawing_tool

    drawing_tool = "pencil"
def line():
    global drawing_tool
    drawing_tool = "line"
def text():
    global drawing_tool,txt

    drawing_tool = "text"


def left_but_down(event=NONE):
    global left_but,x1_line_pt,y1_line_pt
    left_but = "down"

    x1_line_pt= event.x
    y1_line_pt = event.y


def left_but_up(event=NONE):
    global left_but,x2_line_pt,y2_line_pt,x_pos,y_pos
    left_but = "up"

    x2_line_pt = event.x
    y2_line_pt = event.y

    x_pos, y_pos = NONE, NONE

    if drawing_tool == "line":
        draw_line(event)
    if drawing_tool == "text":
        text_draw(event)


def text_draw(event=NONE):
    global txt
    if txt.get() =="":
        messagebox.showinfo("Warning", "Please enter your text")
    if NONE not in (x1_line_pt, y1_line_pt):
        text_font = tkinter.font.Font(family="Halvetica", size=20, weight='bold', slant='italic')

        event.widget.create_text( x1_line_pt, y1_line_pt , fill="red", font=text_font, text=txt.get())

def draw_line(event=NONE):
    if NONE not in (x1_line_pt, y1_line_pt,x2_line_pt,y2_line_pt):
        event.widget.create_line(x1_line_pt,y1_line_pt,x2_line_pt,y2_line_pt,fill="blue",)


def pencil_draw(event=NONE):
    global x_pos,y_pos
    if left_but== "down":
        if x_pos is not NONE and y_pos is not NONE:
            event.widget.create_line(x_pos,y_pos,event.x,event.y,fill = "purple",width="2")

        x_pos = event.x
        y_pos = event.y




def motion(event=NONE):

    if drawing_tool == "pencil":
        pencil_draw(event)

var = StringVar()
label = Message( root, textvariable=var, relief=RAISED,width="550" )
var.set("Welcome! Please choose one of the following options on the bottom of the screen and enjoy :) ")

label.pack(side=TOP)

drawing_area = Canvas(root,width="550",height="550")

drawing_area.pack()



frame=Frame(root)
frame.pack(side=BOTTOM)

btn1 = Button(frame,width="15",text="Pencil",border="5",command=pencil)
btn1.pack(side=LEFT)

btn3 = Button(frame,width="15",text="Text",border="5",command=text)
btn3.pack(side=LEFT)

btn2 = Button(frame,width="15",text="Draw line",border="5",command=line)
btn2.pack(side=LEFT)


frame1=Frame(root)
frame1.pack(side=BOTTOM)
txt=StringVar()


entry=Entry(frame1,textvariable=txt)
entry.pack(side=RIGHT)
txt.set("Enter your text here")










drawing_area.bind("<Motion>", motion)
drawing_area.bind("<ButtonPress-1>", left_but_down)
drawing_area.bind("<ButtonRelease-1>", left_but_up)


root.mainloop()