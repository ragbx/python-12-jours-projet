from tkinter import *
MASTER=Tk()
main_frame = Frame(master=MASTER, padx=10, pady=10)
main_frame.pack(expand=True, fill=BOTH)

image_navigator=Frame(master=main_frame,width=300,height=300)
image_navigator.pack(side=LEFT, expand=True, fill=BOTH) #.grid(row=0,column=0)
image_navigator_zone_affichage=Canvas(image_navigator,bg='#FFFFFF',width=300,height=300,scrollregion=(0,0,500,500))
hbar=Scrollbar(image_navigator,orient=HORIZONTAL)
hbar.pack(side=BOTTOM,fill=X)
hbar.config(command=image_navigator_zone_affichage.xview)
vbar=Scrollbar(image_navigator,orient=VERTICAL)
vbar.pack(side=RIGHT,fill=Y)
vbar.config(command=image_navigator_zone_affichage.yview)
image_navigator_zone_affichage.config(width=300,height=300)
image_navigator_zone_affichage.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
image_navigator_zone_affichage.pack(side=LEFT,expand=True,fill=BOTH)

image_manager = Frame(master=main_frame,width=300,height=300)
image_manager.pack(side=RIGHT, expand=True, fill=BOTH) #.grid(row=0,column=0)
image_manager_labels = Frame(master=image_manager)
image_manager_labels.pack(
                     side=TOP,
                     fill=BOTH,
                     expand=1)
image_manager_labels_title = Label(master=image_manager_labels,
    text="Etiquettes",
    font=("Arial", 12)
    )
image_manager_labels_title.pack(
                     side=TOP,
                     fill=BOTH,
                     expand=1)

MASTER.mainloop()
