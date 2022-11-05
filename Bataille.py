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

