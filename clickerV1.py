import tkinter as tk

getal = 0
def mouse(event):
    global getal
    if getal == 0: 
        window.config(bg='green')
        print('scherm is groen! ')
        getal += 1
    elif getal == 1:
        window.config(bg='red')
        getal -= 1
        print('scherm is rood')

window = tk.Tk()
window.config(bg='red')




window.bind("<Leave>",mouse)
window.bind("<Enter>",mouse)

window.mainloop()