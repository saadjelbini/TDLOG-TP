
class Weapon:
    def __init__(self,ammunitions: int, range: int):
        self._ammunitions = ammunitions
        self._range = range

    def fire_at(self, x:int, y:int, z:int):
        self._x=x
        self._y=y
        self._z=z


class Lance_missile_anti_surface(Weapon):
    def __init__(self, ammunitions=40, range=30,):
        super().__init__(ammunitions, range)

    def fire_at(x:int,y:int,z:int):

        if Weapon._ammunitions==0:
            print("NoAmmunationError")

        elif z!=0:
            print("OutofRange")
            Weapon._ammunitions = Weapon._ammunitions - 1
        
        else:
            print(f"feu sur le point {x},{y},{z}")
                
        
        

class Lance_missile_anti_air(Weapon):
    def __init__(self, ammunitions=50, range=40):
        super().__init__(ammunitions, range)

    def fire_at(x:int,y:int,z:int):
        if Weapon._ammunitions==0:
            print("NoAmmunationError")

        elif z<=0:
            print("OutofRange")
            Weapon._ammunitions = Weapon._ammunitions - 1
        
        else:
            print(f"feu sur le point {x},{y},{z}")
                
        
            
class Lance_Torpille(Weapon):
    def __init__(self, ammunitions=15, range=20):
        super().__init__(ammunitions, range)

    def fire_at(x:int,y:int,z:int):

        if Weapon._ammunitions==0:
            print("NoAmmunationError")

        elif z>0:
            print("OutofRange")
            Weapon._ammunitions = Weapon._ammunitions - 1
        
        else:
            print(f"feu sur le point {x},{y},{z}")
                


        