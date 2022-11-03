from Armes import Weapon
from math import sqrt
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
        if sqrt(x**2+y**2) > Weapon._range:
            print("OutOfRangeError")
            Weapon._ammunitions-=1

class Cruiser(Vessel):
    def go_to(self,x:int,y:int,z:int):
        try:
            Vessel.get_coordinates(x,y,z)
        except z ==0:
            print("Déplacement impossible")

