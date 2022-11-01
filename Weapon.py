class weapon:
    def __init__(self, munition:int, range:int):
        self.munition= munition
        self.range= range
        

    def fire_at(self, x:int, y:int, z:int):

        self.x=x
        self.y=y
        self.z=z
    
    def fire_at(self, x, y, z):
        print("fire_at(",x,", ",y,", ",z,")")





class Lance_missile_Anti_Surface(weapon):
    def __init__(self, munition=30, range=40):
        super.__init__(munition, range)


    def fire_at(self, x, y, z):
        if self.munition==0:
            print("NoAmmunitionError")
        elif z!=0:
            print("OutOfRangeError")
            self.munition-=1
        else:
            super().fire_at(x,y,z)

class Lance_missile_Anti_Air(weapon):
    def __init__(self, munition=50, range=40):
        super.__init__(munition, range)


    def fire_at(self, x, y, z):
        if self.munition==0:
            print("NoAmmunitionError")
        elif z<=0:
            print("OutOfRangeError")
            self.munition-=1
        else:
            super().fire_at(x,y,z)

class Lance_Torpille(weapon):
    def __init__(self, munition=15, range=20):
        super.__init__(munition, range)


    def fire_at(self, x, y, z):
        if self.munition==0:
            print("NoAmmunitionError")
        elif z>0:
            print("OutOfRangeError")
            self.munition-=1
        else:
            super().fire_at(x,y,z)




