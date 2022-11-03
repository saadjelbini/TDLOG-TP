from Armes import Weapon

class Vessel:
    def __init(self, coordinates: tuple, max_hits: int weapon: Weapon):
        self._coordinates=coordinates
        self._max_hits=max_hits
        self._weapon=weapon
    
    def go_to(self, x: int, y:int, z:int):
        self._coordinates= [x, y, z]
       

    def get_coordinate(self,x, y,z):
        self._x=x
        self._y=y
        self._z=z

    def fire_at(self,x:int,y:int,z:int):
        if self._max_hits=0:
            print("DestroyedError")
        else self._coordinates> Weapon.range:
            print("OutOfRangeError")
            Weapon._ammunitions-=1
            
            
class Cruiser(Vessel):
    def go_to(self,x:int,y:int,z:int):
        try:
            Vessel.get_coordinates(x,y,z)
        except z ==0:
            print("Déplacement impossible")

