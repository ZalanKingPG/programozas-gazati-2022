termek_ara = int(input("Kérem a termék árát: "))
arfolyam = float(input("Kérem az euró árfolyamát: "))
pez = float(input("Mennyi euróval rendelkezel: "))
atvaltas = arfolyam * pez
if termek_ara <= atvaltas:
    print("A terméket meg tudod vásárolni")
if termek_ara > atvaltas:
    print("Nincs elég euród a termék megvásárlására!")