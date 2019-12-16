import tkinter as tk  # nécessaire pour interface graphique
from tkinter import scrolledtext as stext
import tkinter.ttk as ttk
import tkinter.filedialog as fdia
import os  # pour manipulation des chemins
from PIL import Image, ImageTk

MASTER = tk.Tk()
main_frame = tk.Frame(master=MASTER, padx=10, pady=10)
main_frame.pack(fill=tk.BOTH, expand=1)

img = Image.open("/home/fpichenot/dev/python-12-jours-projet/data/input/img/bruegel_winter_detail.png")
image = ImageTk.PhotoImage(img)

canvas = tk.Canvas(master=main_frame, width = 600, height = 600)
canvas.create_image((0, 0), image=image, anchor=tk.NW)
canvas.pack()#fill=tk.BOTH, expand=1)
MASTER.mainloop()
