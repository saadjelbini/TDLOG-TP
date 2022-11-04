from Armes import Weapon
from Armes import Lance_missile_anti_air
from Armes import Lance_missile_anti_surface
from Armes import Lance_Torpille
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

<<<<<<< HEAD
class Cruiser(Vessel):
    def __init__(self, coordinates: tuple, max_hits: int, weapon= Weapon):
        super().__init__(coordinates, max_hits, weapon)
        self._weapon=Lance_missile_anti_air()
        self._max_hits=6
        self._coordinates=[0,0,0]

    def go_to(self,x:int,y:int,z:int):
        try:
            Vessel.get_coordinates(x,y,z)
        except z ==0:
            print("Déplacement impossible")


class Submarine(Vessel):
    def __init__(self, coordinates: tuple, max_hits: int, weapon= Weapon):
        super().__init__(coordinates, max_hits, weapon)
        self._weapon=Lance_Torpille()
        self._max_hits=2
        self._coordinates=[-1,-1,-1]
=======

>>>>>>> b36d8c07e56a415c31c0be90b7bcfa73042f8969
            

class Fregate(Vessel):
    def __init__(self, coordinates: tuple, max_hits: int, weapon= Weapon):
        super().__init__(coordinates, max_hits, weapon)
        self._weapon=Lance_missile_anti_surface()
        self._max_hits=5
        self._coordinates=[0,0,0]
            

class Destroyer(Vessel):
    def __init__(self, coordinates: tuple, max_hits: int, weapon= Weapon):
        super().__init__(coordinates, max_hits, weapon)
        self._weapon=Lance_Torpille()
        self._max_hits=4
        self._coordinates=[0,0,0]


class Aircraft(Vessel):
    def __init__(self, coordinates: tuple, max_hits: int, weapon= Weapon):
        super().__init__(coordinates, max_hits, weapon)
        self._weapon=Lance_missile_anti_surface()
        self._max_hits=1
        self._coordinates=[1,1,1]