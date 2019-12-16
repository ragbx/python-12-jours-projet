from tkinter import Tk
from tkinter.ttk import Frame, Label
from PIL import Image, ImageTk
import os

window = Tk()
im = Image.open("/home/fpichenot/dev/python-12-jours-projet/data/input/img/bruegel_bet_detail.jpg")
ph = ImageTk.PhotoImage(im)

label = Label(window, image=ph)
label.pack()
window.mainloop()
