import tkinter as tk
from tkinter import *
from tkinter import messagebox

val = ""
A=0
operator=""

def btn_1():
    global val
    val=val+"1"
    data.set(val)

def btn_2():
    global val
    val=val+"2"
    data.set(val)

def btn_3():
    global val
    val=val+"3"
    data.set(val)

def btn_4():
    global val
    val=val+"4"
    data.set(val)

def btn_5():
    global val
    val=val+"5"
    data.set(val)

def btn_6():
    global val
    val=val+"6"
    data.set(val)

def btn_7():
    global val
    val=val+"7"
    data.set(val)

def btn_8():
    global val
    val=val+"8"
    data.set(val)

def btn_9():
    global val
    val=val+"9"
    data.set(val)

def btn_0():
    global val
    val=val+"0"
    data.set(val)

def btn_plus():
    global A
    global operator
    global val
    A=int(val)
    operator="+"
    val=val+"+"
    data.set(val)

def btn_minus():
    global A
    global operator
    global val
    A=int(val)
    operator="-"
    val=val+"-"
    data.set(val)

def btn_mul():
    global A
    global operator
    global val
    A=int(val)
    operator="*"
    val=val+"x"
    data.set(val)

def btn_div():
    global A
    global operator
    global val
    A=int(val)
    operator="/"
    val=val+"/"
    data.set(val)

def c_pressed():
    global A
    global operator
    global val
    val=""
    A=0
    operator=""
    data.set(val)
    
def result():
    global A
    global operator
    global val
    val2=val
    if operator == "+":
        x=int((val2.split("+")[1]))
        C=A+x
        data.set(C)
        val=str(C)
    elif operator == "-":
        x=int((val2.split("-")[1]))
        C=A-x
        data.set(C)
        val=str(C)
    elif operator == "*":
        x=int((val2.split("x")[1]))
        C=A*x
        data.set(C)
        val=str(C)
    elif operator == "/":
        x=int((val2.split("/")[1]))
        if x==0:
            messagebox.showerror("Error","Divided by 0")
            A=""
            val=""
            data.set(val)
        else:
            C=A/x
            data.set(C)
            val=str(C)
        
root=tk.Tk()
root.geometry("250x400+500+200")
root.resizable(0,0)
root.title("Spacesid")

data=StringVar()

lbl = Label(
    root,
    text="temp",
    anchor=SE,
    font=("Verdana",20),
    textvariable=data,
    background="#ffffff",
    fg="#000000",
    )
lbl.pack(expand=True,fill="both")

btnrow1=Frame(root,bg="#000000")
btnrow1.pack(expand=True,fill="both")

btnrow2=Frame(root)
btnrow2.pack(expand=True,fill="both")

btnrow3=Frame(root)
btnrow3.pack(expand=True,fill="both")

btnrow4=Frame(root)
btnrow4.pack(expand=True,fill="both")

btn1 = Button(
    btnrow1,
    text="1",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_1,
    )
btn1.pack(side=LEFT,expand=True,fill="both")

btn2 = Button(
    btnrow1,
    text="2",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_2,
    )
btn2.pack(side=LEFT,expand=True,fill="both")

btn3 = Button(
    btnrow1,
    text="3",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_3,
    )
btn3.pack(side=LEFT,expand=True,fill="both")

btn4 = Button(
    btnrow1,
    text="+",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_plus
    )
btn4.pack(side=LEFT,expand=True,fill="both")






btn1 = Button(
    btnrow2,
    text="4",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_4
    )
btn1.pack(side=LEFT,expand=True,fill="both")

btn2 = Button(
    btnrow2,
    text="5",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_5
    )
btn2.pack(side=LEFT,expand=True,fill="both")

btn3 = Button(
    btnrow2,
    text="6",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_6
    )
btn3.pack(side=LEFT,expand=True,fill="both")

btn4 = Button(
    btnrow2,
    text="-",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_minus
    )
btn4.pack(side=LEFT,expand=True,fill="both")



btn1 = Button(
    btnrow3,
    text="7",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_7
    )
btn1.pack(side=LEFT,expand=True,fill="both")

btn2 = Button(
    btnrow3,
    text="8",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_8
    )
btn2.pack(side=LEFT,expand=True,fill="both")

btn3 = Button(
    btnrow3,
    text="9",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_9
    )
btn3.pack(side=LEFT,expand=True,fill="both")

btn4 = Button(
    btnrow3,
    text="x",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_mul
    )
btn4.pack(side=LEFT,expand=True,fill="both")

btn1 = Button(
    btnrow4,
    text="C",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=c_pressed
    )
btn1.pack(side=LEFT,expand=True,fill="both")

btn2 = Button(
    btnrow4,
    text="0",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_0
    )
btn2.pack(side=LEFT,expand=True,fill="both")

btn3 = Button(
    btnrow4,
    text="=",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=result
    )
btn3.pack(side=LEFT,expand=True,fill="both")

btn4 = Button(
    btnrow4,
    text="/",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_div
    )
btn4.pack(side=LEFT,expand=True,fill="both")

root.mainloop()
