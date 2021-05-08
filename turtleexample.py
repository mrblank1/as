# import turtle
# import tkinter as tk

# def forward():
#     t.forward(100)

# def back():
#     t.back(100)

# def left():
#     t.left(90)

# def right():
#     t.right(90)

# root = tk.Tk()
# canvas = tk.Canvas(master = root, width = 500, height = 500)
# canvas.pack()

# t = turtle.RawTurtle(canvas)
# t.pencolor("#ff0000") # Red

# t.penup()   # Regarding one of the comments
# t.pendown() # Regarding one of the comments

# tk.Button(master = root, text = "Forward", command = forward).pack(side = tk.LEFT)
# tk.Button(master = root, text = "Back", command = back).pack(side = tk.LEFT)
# tk.Button(master = root, text = "Left", command = left).pack(side = tk.LEFT)
# tk.Button(master = root, text = "Right", command = right).pack(side = tk.LEFT)

# root.mainloop()
import tkinter as tk
import turtle
top= tk.Tk()
C= tk.Canvas(top,width=400,height=400,bg='white')

S=turtle.TurtleScreen(C)
t=turtle.RawTurtle(S)
S.onclick(t.goto)
C.pack()
top.mainloop()
