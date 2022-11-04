from Armes import Lance_Torpille
from Armes import Lance_missile_anti_air
from Armes import Lance_missile_anti_surface
from Vaisseaux import Vessel

Lance_missile_antisurface = Lance_missile_anti_surface(40,30)
Lance_missile_anti_air = Lance_missile_anti_air(50,40)
Lance_torpilles = Lance_Torpille(15,20)



Cruiser = Vessel([0,0,0],6,Lance_missile_anti_air)
Submarine = Vessel([x,y,z],2,Lance_torpilles)
Fregate = Vessel([x,y,0],5,Lance_missile_antisurface)
Destroyer = Vessel([x,y,0],4,Lance_torpilles)
Aircraft = Vessel([x,y,0],1,Lance_missile_antisurface)