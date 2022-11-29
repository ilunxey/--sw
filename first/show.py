from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as tkFont
win = Tk ()
win.title("answer")
win.geometry('500x500')
result = 'a'
def clickMe():
    if str.get() == 'a':
        label = Label(win, text='정답입니다!')
        label.place(x=250, y=250)
        print('정답입니다!')
    else:
        label = Label(win, text='오답!')
        label.place(x=250, y=250)
        print('오답입니다.')
str = StringVar()
textbox = ttk.Entry(win, width=20, textvariable=str)

#textbox.grid(column = 200 , row = 100)
textbox.place(x=200, y=100)
action=ttk.Button(win, text="정답 제출", command=clickMe)
#action.grid(column=200, row=101)
action.place(x=230, y=130)

def start():
    win.mainloop()
