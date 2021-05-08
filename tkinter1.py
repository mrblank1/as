import tkinter
from tkinter import messagebox
from tkinter import Canvas
top=tkinter.Tk()
top.geometry("200x200")
check1=tkinter.IntVar()
check2=tkinter.IntVar()
C1=tkinter.Checkbutton(top,onvalue=1,offvalue=0,variable=check1,text='fuck1')
C2=tkinter.Checkbutton(top,onvalue=1,offvalue=0,text='fuck 2',variable=check2 )
E1=tkinter.Entry()
L1=tkinter.Label(top,text='fuck your mother')
def showMessage():
    messagebox.showinfo('HI','fuck you and have a nice day motherfucker')
B= tkinter.Button(top,text='Fu**', command=showMessage,activebackground="red",fg='white',pady=20)
B.pack()
C1.pack()
C2.pack()
L1.pack(side='top')

top.mainloop()