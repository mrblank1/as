import tkinter as tk
import turtle
import collections
from numpy import zeros
ctr=zeros(9)
top=tk.Tk()
C=tk.Canvas(top,width=400,height=400,bg='white')
C.pack()
S=turtle.TurtleScreen(C)
t=turtle.RawTurtle(S)
t.penup()
t.setposition(-150,-150)
t.pendown()

def main_field():
    t.pensize(4)
    t.color('orange')
    t.fd(300)
    t.left(90)
    t.fd(300)
    t.left(90)
    t.fd(300)
    t.left(90)
    t.fd(300)
    t.left(90)
    t.penup()
    t.fd(100)
    t.left(90)
    t.pendown()
    t.fd(100)
    t.left(90)
    t.fd(100)
    t.right(90)
    t.penup()
    t.fd(100)
    t.right(90)
    t.pendown()
    t.fd(100)
    t.penup()
    t.left(90)
    t.fd(100)
    t.right(180)
    t.pendown()
    t.fd(200)
    t.left(90)
    t.fd(200)
    t.left(90)
    t.penup()
    t.fd(100)
    t.left(90)
    t.pendown()
    t.fd(200)
    t.penup()
    t.right(90)
    t.fd(100)
    t.right(90)
    t.fd(100)
    t.pendown()
    t.right(90)
    t.fd(300)
    t.left(90)
    t.penup()
    t.setposition(-150,-150)
def cross():
    t.speed(3)
    t.penup()
    x=t.pos()
    t.setposition(t.xcor()+20,t.ycor()+20)
    t.pendown()
    t.color('blue')
    t.left(45)
    t.fd(80)
    t.left(135)
    t.penup()
    t.fd(60)
    t.left(135)
    t.pendown()
    t.fd(80)
    t.left(45)
    t.penup()
    t.setposition(x)
def circle():
    t.speed('fastest')
    t.setpos(t.xcor()+50,t.ycor()+20)
    t.color("red")
    t.pensize(2)
    t.pendown()
    for i in range(60):
        t.forward(3.4)
        t.left(6)
    t.penup()
    t.setpos(t.xcor()-50,t.ycor()-20)
    t.speed(3)

main_field()
text=tk.StringVar()
text.set('')
L=tk.Label(top,textvariable=text)
L.pack()
control=1
flag=zeros(9)
def win(a):
    global text
    if a==0:
        text.set("cross you fucking won")
    if a==3:
        text.set("circle You motherfucker")
def chH(a,b):
    sum=0
    sum2=0
    for i in a:
        sum+=ctr[i]
        sum2+=flag[i]
    if (sum2==3 or sum2==0) and sum==3:
        t.setpos(b)
        t.color('black')
        t.pensize(4)
        t.pendown()
        t.fd(250)
        t.penup()
        win(sum2)
        S.onclick(None)
def chV(a,b):
    sum=0
    sum2=0
    for i in a:
        sum+=ctr[i]
        sum2+=flag[i]
    if (sum2==3 or sum2==0) and sum==3:
        t.setpos(b)
        t.left(90)
        t.color('black')
        t.pensize(4)
        t.pendown()
        t.fd(250)
        t.penup()
        win(sum2)
        S.onclick(None)
def chD1(a,b):
    sum=0
    sum2=0
    for i in a:
        sum+=ctr[i]
        sum2+=flag[i]
    if (sum2==3 or sum2==0) and sum==3:
        t.setpos(b)
        t.left(45)
        t.color('black')
        t.pensize(4)
        t.pendown()
        t.fd(350)
        t.penup()
        win(sum2)
        S.onclick(None)
def chD2(a,b):
    sum=0
    sum2=0
    for i in a:
        sum+=ctr[i]
        sum2+=flag[i]
    if (sum2==3 or sum2==0) and sum==3:
        t.setpos(b)
        t.left(135)
        t.color('black')
        t.pensize(4)
        t.pendown()
        t.fd(350)
        t.penup()
        win(sum2)
        S.onclick(None)
###############################
def check():
    #first line hoizental
    chH(range(0,9,3),(-125,-100))
    #second line horizental
    chH(range(1,9,3),(-125,-0))
    #third line horizental
    chH(range(2,9,3),(-125,100))
    #first line vertical
    chV(range(3),(-100,-125))
    #second line vertical
    chV(range(3,6),(0,-125))
    #third line vertical
    chV(range(6,9),(100,-125))
    #first digonal 
    chD1(range(0,9,4),(-125,-125))
    #second diagonal
    chD2(range(2,7,2),(125,-125))
def indicate(x,y):
    S.onclick(None)
    global control
    if (x>-150 and x<-50):
        if(y>-150 and y<-50):
            t.setpos(-150,-150)
            if (control==0 and ctr[0]!=1):
                ctr[0]=1
                control=1
                flag[0]=1
                circle()
            elif (control==1 and ctr[0]!=1):
                ctr[0]=1
                control=0
                cross()
        if(y>-50 and y<50):
            t.setpos(-150,-50)
            if (control==0 and ctr[1]!=1):
                ctr[1]=1
                control=1
                flag[1]=1
                circle()
            elif (control==1 and ctr[1]!=1):
                ctr[1]=1
                control=0
                cross()
        if(y>50 and y<150):
            t.setpos(-150,50)
            if (control==0 and ctr[2]!=1):
                ctr[2]=1
                control=1
                flag[2]=1
                circle()
            elif (control==1 and ctr[2]!=1):
                ctr[2]=1
                control=0
                cross()
    if (x>-50 and x<50):
        if(y>-150 and y<-50):
            t.setpos(-50,-150)
            if (control==0 and ctr[3]!=1):
                ctr[3]=1
                control=1
                flag[3]=1
                circle()
            elif (control==1 and ctr[3]!=1):
                ctr[3]=1
                control=0
                cross()
        if(y>-50 and y<50):
            t.setpos(-50,-50)
            if (control==0 and ctr[4]!=1):
                ctr[4]=1
                control=1
                flag[4]=1
                circle()
            elif (control==1 and ctr[4]!=1):
                ctr[4]=1
                control=0
                cross()
        if(y>50 and y<150):
            t.setpos(-50,50)
            if (control==0 and ctr[5]!=1):
                ctr[5]=1
                control=1
                flag[5]=1
                circle()
            elif (control==1 and ctr[5]!=1):
                ctr[5]=1
                control=0
                cross()
    if (x>50 and x<150):
        if(y>-150 and y<-50):
            t.setpos(50,-150)
            if (control==0 and ctr[6]!=1):
                ctr[6]=1
                control=1
                flag[6]=1
                circle()
            elif (control==1 and ctr[6]!=1):
                ctr[6]=1
                control=0
                cross()
        if(y>-50 and y<50):
            t.setpos(50,-50)
            if (control==0 and ctr[7]!=1):
                ctr[7]=1
                control=1
                flag[7]=1
                circle()
            elif (control==1 and ctr[7]!=1):
                ctr[7]=1
                control=0
                cross()
        if(y>50 and y<150):
            t.setpos(50,50)
            if (control==0 and ctr[8]!=1):
                ctr[8]=1
                control=1
                flag[8]=1
                circle()
            elif (control==1 and ctr[8]!=1):
                ctr[8]=1
                control=0
                cross()
    S.onclick(indicate)
    check()   
S.onclick(indicate)
top.mainloop()