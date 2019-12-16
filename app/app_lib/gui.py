import tkinter as tk  # nécessaire pour interface graphique
from tkinter import scrolledtext as stext
import tkinter.ttk as ttk
import tkinter.filedialog as fdia
import os  # pour manipulation des chemins
from PIL import Image, ImageTk



# fin declaration des paquets

class GetGui(tk.Frame):
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
        self.main_frame_title.pack(side=tk.TOP, fill=tk.BOTH, expand=0)

        self.create_image_navigator()
        self.create_image_manager()


    # on crée le cadre dans lequel apparaîtra l'image
    def create_image_navigator(self):
        self.image_navigator = tk.Frame(master=self.main_frame)
        self.image_navigator.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)


        # elements de image_navigator
        self.image_navigator_zone_affichage = tk.Canvas(
                master=self.image_navigator, width=700, height=500, bd=2, relief='sunken',scrollregion=(0,0,2000,2000))

        # gestion des scrollbars
        hbar=tk.Scrollbar(self.image_navigator,orient='horizontal')
        hbar.pack(side=tk.BOTTOM,fill=tk.X)
        hbar.config(command=self.image_navigator_zone_affichage.xview)

        vbar=tk.Scrollbar(self.image_navigator,orient='vertical')
        vbar.pack(side=tk.RIGHT,fill=tk.Y)
        vbar.config(command=self.image_navigator_zone_affichage.yview)
        self.image_navigator_zone_affichage.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        self.image_navigator_zone_affichage.pack(side=tk.LEFT,expand=True,fill=tk.BOTH)

    # on crée le cadre dans lequel on mettra les boutons
    def create_image_manager(self):
        # on crée une liste dans laquelle on stockera les chemins des images
        self.images_files_pathes = []

        # on crée un cadre
        self.image_manager = tk.Frame(master=self.main_frame, width=200)

        self.image_manager.pack(
                side=tk.RIGHT,
                fill=tk.Y,
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

        self.get_labels() # on récupère les intitulés des labels
        self.image_manager_labels_list = ttk.Combobox(master=self.image_manager_labels, values=self.labels)
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

        self.image_manager_listbox = tk.Listbox(master=self.image_manager_list)#stext.ScrolledText(master=self.image_manager_list)
        self.image_manager_listbox.pack(
                side=tk.TOP,
                fill=tk.BOTH,
                expand=1
        )

        self.image_manager_list_add=tk.Button(master=self.image_manager_list,text="Ajouter",font=("Arial",12), command=self.get_image_file_path)
        self.image_manager_list_add.pack(
                             side=tk.TOP,
                             fill=tk.BOTH,
                             expand=1)

        self.image_manager_list_load=tk.Button(master=self.image_manager_list,text="Charger",font=("Arial",12), command=self.load_image)
        self.image_manager_list_load.pack(
                             side=tk.TOP,
                             fill=tk.BOTH,
                             expand=1)

        self.image_manager_list_delete=tk.Button(master=self.image_manager_list,text="Supprimer",font=("Arial",12), command=self.del_image_file_path)
        self.image_manager_list_delete.pack(
                             side=tk.TOP,
                             fill=tk.BOTH,
                             expand=1)

        # fin des elements de image_navigator

    def get_labels(self):
        filename = "data/input/labels/labels.txt"
        with open(filename, "r", encoding="UTF8") as fh:
            self.labels = fh.read().splitlines()

    def get_image_file_path(self):
        self.image_file_path = fdia.askopenfilename(title = "Choisir un fichier", filetypes=[("PNG","*.png"), ("JPEG", "*.jp*g")])
        self.images_files_pathes.append(self.image_file_path)
        self.get_image_file_name()
        self.image_manager_listbox.insert(tk.END, self.image_file_name)

    def get_image_file_name(self):
        el = self.image_file_path.split("/")
        self.image_file_name = el[-1]


    def del_image_file_path(self):
        image_index_in_listbox = self.image_manager_listbox.curselection()
        if image_index_in_listbox:
            self.image_manager_listbox.delete(image_index_in_listbox)
            self.images_files_pathes.pop(image_index_in_listbox[0])

    def load_image(self):
        index_image_to_load = self.image_manager_listbox.curselection()
        file_path = self.images_files_pathes[index_image_to_load[0]]
        img = Image.open(file_path)
        image = ImageTk.PhotoImage(img)
        self.image_navigator_zone_affichage.create_image((0,0), image=image, anchor=tk.NW)
        self.image_navigator_zone_affichage.image = image
        self.image_navigator_zone_affichage.pack()


if __name__ == "__main__":
    MASTER = tk.Tk()
    GetGui(master=MASTER)
    MASTER.mainloop()
