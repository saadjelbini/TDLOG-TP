from Armes import Weapon
import math
class Vessel:
    def __init__(self,coordinates : tuple, max_hits : int, weapon : Weapon):
        self._coordinates = coordinates
        self._max_hits = max_hits
        self._weapon = weapon

    def go_to(self,x:int,y:int,z:int):
        self._coordinates = [x,y,z]

    def get_coordinates(self,x:int ,y:int ,z:int):
        self._x=x
        self._y=y
        self._z=z

    def fire_at(self,x:int,y:int,z:int):
        if self._max_hits==0:
            print("DestroyedError")

        else:
            print("OutOfRangeError")
            Weapon._ammunitions-=1

class Cruiser(Vessel):
    def __init__(self):

        self.max_hits = 6
        self.coordinates=(0,0,0)
        #######self.weapon = "Anti-air" #a verifier
        
 class Submarine(Vessel):
    def __init__(self,x,y):
        self.max_hits = 2
        self.coordinates=(x,y,-1) or (x,y,0)
        ###self.weapon = "Lance-tropilles" #a verifier 
        
 class Fregate(Vessel):
    def __init__ (self,x,y):
        self.max_hits = 5
        self.coordinates=(x,y,-1)
      ##  self.weapon = "Lance-missilles antisurface" #a verifier
 class Destroyer(Vessel):
    def __init__ (self,x,y):
        self.max_hits = 4
        self.coordinates=(x,y,0)
        ##self.weapon = "Lance-tropilles" #a verifier
 class Aircraft(Vessel):
    def __init__ (self,x,y):
        self.max_hits = 1
        self.coordinates=(x,y,1)
        ##self.weapon = "Lance-missilles antisurface" #a verifier
            

