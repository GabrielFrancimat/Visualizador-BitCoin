from tkinter import *
from tkinter import ttk

color0 = "#444466" # Preto/Black
color1 = "#feffff" # Branco/White
color2 = "#6f9fbd" # Azul/Blue

backgroundColor = "#484f60" # Background

window = Tk()
window.title("")
window.geometry("320x350")
window.configure(bg=backgroundColor)

ttk.Separator(window,orient=HORIZONTAL).grid(row=0,columnspan=1,ipadx=)

window.mainloop()