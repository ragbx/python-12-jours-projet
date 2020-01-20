"""
Ce script permet de lancer l'application.
Il doit être exécuter depuis la racine du projet.
"""

import tkinter as tk

import app_lib.gui as g


MASTER = tk.Tk()
g.GetGui(master=MASTER)
MASTER.mainloop()
