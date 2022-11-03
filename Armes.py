
class Weapon:
    def __init__(self,ammunitions: int, range: int):
        self._ammunitions = ammunitions
        self._range = range

    def fire_at(self, x:int, y:int, z:int):
        self._x=x
        self._y=y
        self._z=z


class Missile_anti_surface(Weapon):
    def __init__(self, ammunitions=40, range=30):
        super().__init__(ammunitions, range)

    def fire_at(x:int,y:int,z:int):
        try:
            try:
                print(f"feu sur le point {x},{y},{z}")
                Weapon._ammunitions = Weapon._ammunitions - 1
            except Weapon._ammunitions == 0 :
                print("NoAmmunationError")
        except z != 0:
            print("OutOfRangeError")
            Weapon._ammunitions = Weapon._ammunitions - 1

class Missile_anti_air(Weapon):
    def __init__(self, ammunitions=50, range=40):
        super().__init__(ammunitions, range)

    def fire_at(x:int,y:int,z:int):
        try:
            try:
                print(f"feu sur le point {x},{y},{z}")
                Weapon._ammunitions = Weapon._ammunitions - 1
            except Weapon._ammunitions == 0 :
                print("NoAmmunationError")
        except z <=0 :
            print("OutOfRangeError")
            Weapon._ammunitions = Weapon._ammunitions - 1

class Torpille(Weapon):
    def __init__(self, ammunitions=15, range=20):
        super().__init__(ammunitions, range)

    def fire_at(x:int,y:int,z:int):
        try:
            try:
                print(f"feu sur le point {x},{y},{z}")
                Weapon._ammunitions = Weapon._ammunitions - 1
            except Weapon._ammunitions == 0 :
                print("NoAmmunationError")
        except z >0 :
            print("OutOfRangeError")
            Weapon._ammunitions = Weapon._ammunitions - 1