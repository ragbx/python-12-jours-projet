###############
Spécification
###############

Auteur: Kaan Eraslan

=======
Résumé
=======

L'application est un labeliseur d'image en fonction d'un ficher
d'étiquette.

Il a 4 composants:

- Canvas d'image

- Liste des chemins d'image

- Groupe des boutons de radio 

- Boutons

===============
Entrée/Sortie
===============

Le programme prend un chemin d'un fichier qui contient 
des étiquettes séparés par des nouvelles lignes. Il va remplir
les textes des boutons de radio avec ces étiquettes.

Un exemple d'entrée:

.. code::

   visage
   oreille
   pied
   main
   jambe

Le programme va donner comme sortie, un fichier json.
Le fichier json contient un entrée pour chaque image.
Chaque entrée doit contenir les clés suivants:

- :code:`chemin_image`: elle doit être associé au chemin absolu
  d'image.

- :code:`proprietes`: elle doit être associé à une liste qui 
  contient les membres comme les suivants:

  - :code:`{"bbox": {"topLeft": {"x": 10, "y": 16}, 
    "bottomRight": {"x": 16, "y": 30}}, "label": "visage"}`

Un exemple de sortie:

.. code-block:: json

    {
        "chemin_image": "/home/usr1/image/image01.png",
        "proprietes": [
            {"bbox": {
                "topLeft": {"x": 10, "y": 16},
                "bottomRight": {"x": 16, "y": 30}
                },
             "label": "visage"
            },
            {"bbox": {
                "topLeft": {"x": 100, "y": 160},
                "bottomRight": {"x": 160, "y": 300}
                },
             "label": "oreille"
            },
            {"bbox": {
                "topLeft": {"x": 150, "y": 181},
                "bottomRight": {"x": 190, "y": 500}
                },
             "label": "jambe"
            },
        ]
    }

===========
Composants
===========

---------------
Canvas d'image
---------------

Il correspond à un widget de Canvas en tkinter. Elle nous permet
de charger et dessiner des images.
Dans notre programme, elle nous sert à marquer un ou plusieur 
rectangle sur l'image. Une fois qu'un rectangle a selectionné,
on enregistre les coordonnées de cette rectangle associé à 
un étiquette. Les coordonnées qu'on enregistre doivent contenir au moins,
le coin haut gauche et le coin bas droit.

-------------------------
Liste des chemin d'image
-------------------------

Il correspond à un widget de Listbox. Il nous permet d'afficher une liste 
des textes.
Ceux qu'on affiche dedans peuvent être soit le/s chemin/s d'image eux même soit 
une référence plus courtes aux chemins.
On peut ajouter et supprimer des chemins à partir de la liste à travers l'usage 
des boutons.


-----------------------------
Groupe des Boutons de Radio
-----------------------------

Le texte de ces boutons vient de fichier d'étiquette qu'on charge au programme.
Il nous permet d'associer le label, c'est à dire le texte de bouton avec le
rectangle de selection.
On ne peut associer qu'un seul label à une region sélectionnée.
Avant qu'on sélectionne une region, un bouton de radio doit être coché.

--------
Boutons
--------

A part de groupe des boutons de radio qui est généré en fonction du fichier
d'étiquette de l'utilisateur, on a une suite des boutons qui nous permet 
de gérer l'état de programme.

- Charger: Bouton qui sert à remplir la liste avec les chemins d'image
- Supprimer: Bouton qui sert à supprimer les chemins sélectionnés dans la liste.
- Ouvrir: Bouton qui sert à charger l'image au Canvas d'image.
- Sauvegarder: Bouton qui sert à sauvegarder les travaux effectués sur l'ensemble
  des images dans le format spécifié dans la section Entrée/Sortie.


==========================
Mise en Page de Programme
==========================

On vous propose ici une mise en page possible du programme.



+----------------------------------------------+
|         Mon Labéliseur Titre                 |
+--------------------------------+-------------+
|                                | Img Chemins |
|                                +-------------+ 
|                                |             |
|                                +-------------+ 
|                                |  chemin1    |
|                                +-------------+ 
|                                |  chemin2    |
|                                +-------------+ 
|   Canvas D'Image               |  chemin3    |
|                                +-------------+ 
|                                |  chemin_n   |
|                                +-------------+ 
|                                |             |
|                                +-------------+ 
|                                |  Bouton1    |
|                                +-------------+ 
|                                |  Bouton2    |
|                                +-------------+ 
|                                |  Bouton3    |
|                                +-------------+ 
|                                |             |
|                                +-------------+ 
|                                | Groupe      |
|                                | Radio       |
|                                +-------------+ 
|                                |  RBouton1   |
|                                +-------------+ 
|                                |  RBouton2   |
|                                +-------------+ 
|                                |  RBouton3   |
|                                +-------------+ 
|                                |             |
|                                +-------------+ 
|                                |  Bouton1    |
+--------------------------------+-------------+ 
