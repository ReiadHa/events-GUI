# import tkinter as tk


# def up():
#     global number
#     number += 1
#     clicker()
# def down():
#     global number
#     number -= 1
#     clicker()

# def clicker():
#     global number,label1
#     if number < 0:
#         window.config(bg='red')
#     elif number > 0 :
#         window.config(bg='green')
#     elif number == 0:
#         window.config(bg='grey')
#     labstr = tk.StringVar(value=f'{number}')
#     label1.config(textvariable=labstr)
# def click(event):
#     global number
#     print('clicked')
#     if up :
#         number = number * 3
#     elif down :
#         number = number / 3


# window = tk.Tk()
# window.geometry('300x300')

# number = 0 
# label1 = tk.Label( text= f'{number}',width=20)
# label1.place(anchor='center',relx=0.5,rely = 0.5)
# button1 = tk.Button(text='Up')
# button2 = tk.Button(text='Down')
# button1.pack(side=tk.TOP)
# button2.pack(side=tk.BOTTOM)
# window.bind("<Double-Button-1>",click)

# clicker()
# window.mainloop()

import tkinter as tk 
#=================== funtions hier onder=================================
def up():
    global number,keer
    number += 1
    print(number)
    keer = True
    clicker()
def down():
    global number, keer
    number -= 1
    print(number)
    keer = False
    clicker()
def clicker():
    global number,lab
    if number < 0:
        win.config(bg='red')
    elif number > 0 :
        win.config(bg='green')
    elif number == 0:
        win.config(bg='grey')
    labstr = tk.StringVar(value=f'{number:.0f}')
    lab.config(textvariable=labstr)

def Dclick(event):
    global number
    print('clicked')
    if keer == True :
        number = number * 3
    elif keer == False :
        number = number / 3
    labstr = tk.StringVar(value=f'{number:.0f}')
    lab.config(textvariable=labstr)
#==================== window/labels/buttons setup hieronder====================
keer = False
number = 0
win = tk.Tk()
win.geometry('300x150')
lab = tk.Label( text= f'{number:.0f}',width=20)
lab.config(bg='white')
button1 = tk.Button(text='Up',width=20)
button2 = tk.Button(text='Down',width=20)
lab.place(anchor='center',relx=0.5,rely = 0.5)
button1.pack(side=tk.TOP)
button2.pack(side=tk.BOTTOM)
button1.config(command=up)
button2.config(command=down)
lab.bind("<Double-Button-1>",Dclick)
clicker()

#=====window mainloop========
win.mainloop()