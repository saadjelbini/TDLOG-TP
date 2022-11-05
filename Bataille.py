from Armes import*
from vaisseaux import *

import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# introduction de termes
plateau = np.zeros([101,101,3],dtype =np.uint8)
bleu1 = [96,199,255]
bleu = [0,0,255]
rouge = [255,0,0]
vert = [0,255,0]
blanc = [255,255,255]
for i in range(len(plateau)):
    for j in range(len(plateau[i])):
        plateau[i][j] = bleu1

class espace_jeux():
    def __init__(self,x,y,z,list_vaisseaux):
        self.x =x
        self.y =y
        self.z= z
        self.list = list_vaisseaux
        
    def recevoir():
        
    def game_over(Player):
        if Player.hits == 0:
            print("game over")
        else:
            pass

        
class Player():
     def __init__(self,vessel_list: list , Arme_list: list , hits:int,ammunations:int):
        self.hits = 22

        def main():
    root = Tk()
    gui = fenetre(root)
    gui.root.mainloop()
    return None

# Les termes introduits

plateau = np.zeros([101,101,3],dtype =np.uint8)

liste_rayon_action = [40,40,30,20,30]
liste_vaisseaux = ["Cruiser","Submarine","Fregate","Destroyer","Aircraft"]

bleu1 = [96,199,255]
bleu = [0,0,255]
rouge = [255,0,0]
vert = [0,255,0]
blanc = [255,255,255]
for i in range(len(plateau)):
    for j in range(len(plateau[i])):
        plateau[i][j] = bleu1
        
# Interface graphique

class fenetre:
    def __init__(self, root):
        self.root = root
        self.root.title("Bataille Navale")
        self.root.geometry('900x900')

        # les boutons pour déterminer la latitude et la longitude
        latitude = tk.Label(root,text = "latitude")
        latitude.grid(column=0, row=2)
        longitude = tk.Label(root,text = "longitude")
        longitude.grid(column=0, row=3)
        self.entry_latitude = tk.Entry(root, width=10)
        self.entry_longitude = tk.Entry(root, width=10)
        self.entry_latitude.grid(column=1, row=2, padx=10)
        self.entry_longitude.grid(column=1, row=3, padx=10)

        # le menu déroulant pour choisir avec quel véhicule nous allons tirer
        labelChoix = tk.Label(root, text = "Veuillez choisir un navire/avion")
        labelChoix.grid(column=0, row=1)
        listeCombo = ttk.Combobox(root, values=liste_vaisseaux,width=10)
        listeCombo.current(0)
        listeCombo.grid(column=1, row=1)
        listeCombo.bind("<<ComboboxSelected>>")

        # le menu déroulant qui permet de choisir si nous envoyons un missile sous l'eau, en surface ou dans les airs
        Zlabel = tk.Label(root,text="hauteur")
        Z = ttk.Combobox(root,values=[-1,0,1],width=10)
        Z.bind("<<ComboboxSelected>>")
        Zlabel.grid(column=0, row=4)
        Z.grid(column=1, row=4)

        # bouton pour tirer
        bouton1 = Button(root,text='Tirer',command=tirer)
        bouton1.grid(column=0, row=5)
        
        # affiche le plateau de bataille navale
        label = Label(root,text='Bataille Navale',font = tkFont.Font(size=15))
        label.grid(column=0, row=0)
        fig = plt.figure(figsize=(10,10))
        ax = fig.add_subplot(1, 1, 1)
        chart = FigureCanvasTkAgg(fig, self.root)
        chart.get_tk_widget().grid(row = 10, column = 0)
        plt.title("Plateau de jeu",size=20)
        plt.xlim(0,100)
        plt.ylim(0,100)
        grid_x_ticks = np.arange(0, 100, 5)
        grid_y_ticks = np.arange(0, 100, 5)
        ax.set_xticks(grid_x_ticks , minor=False)
        ax.set_yticks(grid_y_ticks , minor=False)
        ax.grid(which='both')
        ax.grid(which='minor', alpha=0.2, linestyle='--')
        plt.imshow(plateau)

    def tirer():
        liste_hauteur=['sous le niveau de la mer','en surface','dans les airs']
        x = int(self.entry_latitude.get())
        y = int(self.entry_longitude.get())
        z = Z.get()
        rayon_action = liste_rayon_action[liste_vaisseaux.index(listeCombo.get())]
        for i in range(len(plateau)):
            for j in range(len(plateau[i])):
                if ((i-x)**2+(j-y)**2)**(1/2) <= rayon_action:
                    if plateau[i][j] == noir:
                        plateau[i][j] = vert
                        print("touché !")
                    else :
                        plateau[i][j] = blanc
                        print("Raté !")
                else :
                    pass           
        print("Vous avez tirez", liste_hauteur[Z.index(z)], "aux cordonnées de latitude x = ",x," et de longitude y = ",y)
        
main()
