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


            

