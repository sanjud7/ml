import tkinter as tk
from tkinter import *
from tkinter import filedialog


def clear_all():
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)
    e3.delete(0, tk.END)
    e4.delete(0, tk.END)
    e5.delete(0, tk.END)
    e6.delete(0, tk.END)


def cluster():
    a = int(e1.get())
    b = int(e2.get())
    c = float(e4.get())
    d = float(e3.get())

    e = float(e5.get())
    Z = a * c + b * d
    if Z >= e:
        y = 1
    else:
        y = 0
    Result.set(y)
    comp_res = Label(top, font=('lato black', 15, 'bold'), text='COMPARISON', fg="white", bg="black", width=22)
    comp_res.place(x=460, y=250)
    A_bit= Label(top, font=('lato black', 12, 'bold'), text='A\n0\n0\n1\n1', fg="black", width=2)
    A_bit.place(x=460, y=297)
    B_bit = Label(top, font=('lato black', 12, 'bold'), text='B\n0\n1\n0\n1', fg="black", width=2)
    B_bit.place(x=485, y=297)
    Expected= Label(top, font=('lato black',11, 'bold'), text='Expected Result\n0\n0\n0\n1', fg="black", width=15)
    Expected.place(x=520, y=297)
    if(a==0 and b==0):
        output= Label(top, font=('lato black', 11, 'bold'), text='Output\n'+str(y), fg="black", width=6)
        output.place(x=670, y=297)
        if(y==0):
            pass
        else:
            busted_display = Label(top, text="Incorrect Output values obtained !!! Try some different weights and threshold.", font=("arial", "15"),fg="red",bg="black")
            busted_display.place(x=40, y=530)
            busted_display.after(4000, busted_display.destroy)


    elif(a==0 and b==1):
        output = Label(top, font=('lato black', 11, 'bold'), text='Output\n\n'+str(y), fg="black", width=6)
        output.place(x=670, y=297)
        if(y==0):
            pass
        else:
            busted_display = Label(top,text="Incorrect Output values obtained !!! Try some different weights and threshold.",font=("arial", "15"), fg="red", bg="black")
            busted_display.place(x=40, y=530)
            busted_display.after(4000, busted_display.destroy)


    elif ( a ==1 and b == 0):
        output = Label(top, font=('lato black', 11, 'bold'), text='Output\n\n\n'+str(y), fg="black", width=6)
        output.place(x=670, y=297)
        if (y == 0):
            pass
        else:
            busted_display = Label(top,
                                   text="Incorrect Output values obtained !!! Try some different weights and threshold.",
                                   font=("arial", "15"), fg="red", bg="black")
            busted_display.place(x=40, y=530)
            busted_display.after(4000, busted_display.destroy)
    elif ( a == 1 and b == 1):
        output = Label(top, font=('lato black', 11, 'bold'), text='Output\n\n\n\n'+str(y), fg="black", width=6)
        output.place(x=670, y=297)
        if (y == 1):
            pass
        else:
            busted_display = Label(top,
                                   text="Incorrect Output values obtained !!! Try some different weights and threshold.",
                                   font=("arial", "15"), fg="red", bg="black")
            busted_display.place(x=40, y=530)
            busted_display.after(4000, busted_display.destroy)




def option_menu(event):
    e1.delete(0,'end')
    e1.insert("1",value_inside.get())
def option_menu1(event):
    e2.delete(0,'end')
    e2.insert("1", value_inside1.get())

def setw1(event):
    e3.delete(0,'end')
    e3.insert("1",w1.get())

def setw2(event):
    e4.delete(0,'end')
    e4.insert("1",w2.get())
def thres(event):
    e5.delete(0,'end')
    e5.insert("1",thres_hold.get())


top = tk.Tk()
top.title("GUI : AND Gate")
top.geometry("750x580")
top.resizable(width=False,height=False)

Result = StringVar()








headlabel = tk.Label(top, font=('lato black', 19, 'bold'), text=' AND Gate ', bg='black',width=35,height=1, fg='white')
headlabel.place(x=100,y=50)
La = Label(top, font=('lato black', 27, 'bold'), text='', padx=2, pady=2, bg="#e6e5e5", fg="black")
La.grid(row=1, column=0, sticky=W)

Label(top, font=('lato black', 15, 'bold'), text='First Bit a :', fg="black").place(x=150,y=150)
Label(top, font=('lato black', 15, 'bold'), text='Second Bit b :', fg="black").place(x=150,y=200)
Label(top, font=('lato black', 15, 'bold'), text='W1 :', fg="black").place(x=150,y=250)
Label(top, font=('lato black', 15, 'bold'), text='W2 :', fg="red").place(x=150,y=300)
Label(top, font=('lato black', 15, 'bold'), text='Threshold :', fg="blue").place(x=150,y=350)
Label(top, font=('lato black', 15, 'bold'), text='Result :', fg="black").place(x=150,y=400)



e1 = Entry(top, font=('arial', 10, 'bold'))
e2 = Entry(top, font=('arial', 10, 'bold'))
e3 = Entry(top, font=('arial', 10, 'bold'))
e4 = Entry(top, font=('arial', 10, 'bold'))
e5 = Entry(top, font=('arial', 10, 'bold'))
e6 = Entry(top, font=('arial', 10, 'bold'), textvariable=Result)


e1.place(x=285,y=155)
e2.place(x=290,y=205)
e3.place(x=285,y=255)
e4.place(x=285,y=299)
e5.place(x=285,y=350)
e6.place(x=285,y=400)


w1= Scale(top, from_=-1, to=2, orient=HORIZONTAL,bg="black",fg="white",command=setw1)
w1.place(x=20,y=238)
w2 = Scale(top, from_=-2, to=2, orient=HORIZONTAL,bg="red",fg="white",command=setw2)
w2.place(x=20,y=290)

thres_hold= Scale(top, from_=-2, to=2, orient=HORIZONTAL,bg="blue",fg="white",command=thres)
thres_hold.place(x=20,y=348)


bt = Button(top, font=('arial', 15, 'bold'), text=" Process ",width=10, padx=2, pady=2, bg="green", fg="white", command=cluster)
bt.place(x=150,y=460)

bt2 = Button(top, font=('arial', 15, 'bold'), text=" Clear All ",width=10, padx=2, pady=2, bg="black", fg="red",
             command=clear_all)
bt2.place(x=400,y=460)



options_list = [0,1]

value_inside =StringVar(top)
value_inside.set("select a bit value")
question_menu =OptionMenu(top, value_inside, *options_list,command=option_menu)

question_menu.place(x=500,y=149)
options_list1 = [0, 1]
value_inside1 = StringVar(top)
value_inside1.set("Select b bit value")
question_menu2 = OptionMenu(top, value_inside1, *options_list1,command=option_menu1)
question_menu2.place(x=500, y=205)







top.mainloop()