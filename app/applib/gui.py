"""
Cette classe permet de gérer l'interface graphique
"""

# déclaration des paquets

import tkinter as tk  # nécessaire pour interface graphique
from tkinter import scrolledtext as stext
import tkinter.ttk as ttk
import os  # pour manipulation des chemins
# fin declaration des paquets

class get_gui(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_main_frame()

    # On crée le cadre principal
    def create_main_frame(self):
        self.main_frame = tk.Frame(master=self.master, padx=10, pady=10)
        self.main_frame.pack(fill=tk.BOTH, expand=1)

        # les elements de cadre principal
        self.main_frame_title = tk.Label(master=self.main_frame,
            text="Application 12 jours",
            font=("Arial", 16)
            )
        self.main_frame_title.pack(side=tk.TOP, fill=tk.BOTH, 
                            expand=0)

        self.create_image_navigator()
        self.create_image_manager()


    # on crée le cadre dans lequel apparaîtra l'image
    def create_image_navigator(self):
        self.image_navigator = tk.Frame(master=self.main_frame)
        self.image_navigator.pack(side=tk.LEFT, fill=tk.BOTH, 
        expand=1)

        # elements de image_navigator
        self.image_navigator_zone_affichage_text = stext.ScrolledText(
            master=self.image_navigator
        )
        self.image_navigator_zone_affichage_text.pack(
                side=tk.LEFT,
                fill=tk.BOTH,
                expand=1
        )

    # on crée le cadre dans lequel on mettra les boutons
    def create_image_manager(self):
        # on crée un cadre
        self.image_manager = tk.Frame(master=self.main_frame, width=200)
        
        self.image_manager.pack(
                side=tk.RIGHT,
                #fill=tk.BOTH, 
                expand=1)
        

        # on imbrique un premier élément pour gérer les labels
        self.image_manager_labels = tk.Frame(master=self.image_manager)
        self.image_manager_labels.pack(
                             side=tk.TOP,
                             fill=tk.BOTH,
                             expand=1)
        self.image_manager_labels_title = tk.Label(master=self.image_manager_labels,
            text="Etiquettes",
            font=("Arial", 12)
            )
        self.image_manager_labels_title.pack(
                             side=tk.TOP,
                             fill=tk.BOTH,
                             expand=1)
        self.image_manager_labels_list = ttk.Combobox(master=self.image_manager_labels, values=["ligne 1", "ligne 2", "ligne 3", "ligne 4"])
        self.image_manager_labels_list.pack()

        # on imbrique un second élément pour sauvegarder les résultats
        self.image_manager_save=tk.Button(master=self.image_manager,text="Sauvegarder",font=("Arial",12))
        self.image_manager_save.pack(
                             side=tk.TOP,
                             fill=tk.BOTH,
                             expand=1)

        # on imbrique un troisième élément pour gérer la liste des images
        self.image_manager_list = tk.Frame(master=self.image_manager)
        self.image_manager_list.pack(
                             side=tk.TOP,
                             fill=tk.BOTH,
                             expand=1)

        self.image_manager_list_title = tk.Label(master=self.image_manager_list,
            text="Liste d'images",
            font=("Arial", 12)
            )
        self.image_manager_list_title.pack(
                             side=tk.TOP,
                             fill=tk.BOTH,
                             expand=1)

        self.image_manager_text = stext.ScrolledText(
            master=self.image_manager_list
        )
        self.image_manager_text.pack(
                side=tk.TOP,
                fill=tk.BOTH,
                expand=1
        )

        self.image_manager_list_add=tk.Button(master=self.image_manager_list,text="AJouter",font=("Arial",12))
        self.image_manager_list_add.pack(
                             side=tk.TOP,
                             fill=tk.BOTH,
                             expand=1)

        self.image_manager_list_load=tk.Button(master=self.image_manager_list,text="Charger",font=("Arial",12))
        self.image_manager_list_load.pack(
                             side=tk.TOP,
                             fill=tk.BOTH,
                             expand=1)

        self.image_manager_list_delete=tk.Button(master=self.image_manager_list,text="Supprimer",font=("Arial",12))
        self.image_manager_list_delete.pack(
                             side=tk.TOP,
                             fill=tk.BOTH,
                             expand=1)

        # fin des elements de image_navigator

    

if __name__ == "__main__":
    root = tk.Tk()
    monapp = gui(master=root)
    root.mainloop()
