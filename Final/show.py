from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter

import pandas as pd

corr = None

def clickMe():
    global corr

    if str.get() == result:
        label = Label(win, text='정답입니다!')
        label.place(x=250, y=250)
        corr = True
    else:
        label = Label(win, text='오답!')
        label.place(x=250, y=250)

def k(difficulty, x):
    global win, str, result
    if difficulty == 'easy':
        df = pd.read_excel('forest.xlsx')
    elif difficulty == 'normal':
        df = pd.read_excel('desert.xlsx')
    else:
        df = pd.read_excel('space.xlsx')

    if x == 'l':
        num = 0
        quiz = df.loc[num, '문제']
        result = df.loc[num, '답']
        # if type(result) == int:
        #     result = str(result)
    elif x == 'r':
        num = 1
        quiz = df.loc[num, '문제']
        result = df.loc[num, '답']
        # if type(result) == int:
        #     result = str(result)
    elif x == 'd':
        num = 2
        quiz = df.loc[num, '문제']
        result = df.loc[num, '답']
        # if type(result) == int:
        #     result = str(result)
    else:
        num = 3
        quiz = df.loc[num, '문제']
        result = df.loc[num, '답']
        # if type(result) == int:
        #     result = str(result)

    
    
    
    win = Tk ()
    win.title("answer")
    win.geometry('500x500')
    label = Label(win, text=quiz)
    label.place(x=150, y=50)
    

    str = StringVar()   
    textbox = ttk.Entry(win, width=20, textvariable=str)
    textbox.place(x=200, y=400)
    action=ttk.Button(win, text="정답 제출", command=clickMe)
    action.place(x=230, y=130)
    win.mainloop()
    return corr

