from Armes import*
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
    def __init__(self, coordinates: tuple, max_hits: int, weapon= Weapon):
        super().__init__(coordinates, max_hits, weapon)
        self._weapon=Lance_missile_anti_air()
        self._max_hits=6
        self._coordinates=[0,0,0]

    def go_to(self,x:int,y:int,z:int):
        try:
            Vessel.get_coordinates(x,y,z)
        except z !=0:
            print("Déplacement impossible")


class Submarine(Vessel):
    def __init__(self, coordinates: tuple, max_hits: int, weapon= Weapon):
        super().__init__(coordinates, max_hits, weapon)
        self._weapon=Lance_Torpille()
        self._max_hits=2
        self._coordinates=[-1,-1,-1]

    def go_to(self,x:int,y:int,z:int):
        try:
            Vessel.get_coordinates(x,y,z)
        except z !=-1 or z!=0:
            print("Déplacement impossible")


            

class Fregate(Vessel):
    def __init__(self, coordinates: tuple, max_hits: int, weapon= Weapon):
        super().__init__(coordinates, max_hits, weapon)
        self._weapon=Lance_missile_anti_surface()
        self._max_hits=5
        self._coordinates=[0,0,0]
            
    def go_to(self,x:int,y:int,z:int):
        try:
            Vessel.get_coordinates(x,y,z)
        except z !=0:
            print("Déplacement impossible")


class Destroyer(Vessel):
    def __init__(self, coordinates: tuple, max_hits: int, weapon= Weapon):
        super().__init__(coordinates, max_hits, weapon)
        self._weapon=Lance_Torpille()
        self._max_hits=4
        self._coordinates=[0,0,0]

    def go_to(self,x:int,y:int,z:int):
        try:
            Vessel.get_coordinates(x,y,z)
        except z !=0:
            print("Déplacement impossible")

class Aircraft(Vessel):
    def __init__(self, coordinates: tuple, max_hits: int, weapon= Weapon):
        super().__init__(coordinates, max_hits, weapon)
        self._weapon=Lance_missile_anti_surface()
        self._max_hits=1
        self._coordinates=[1,1,1]

    def go_to(self,x:int,y:int,z:int):
        try:
            Vessel.get_coordinates(x,y,z)
        except z !=1:
            print("Déplacement impossible")
