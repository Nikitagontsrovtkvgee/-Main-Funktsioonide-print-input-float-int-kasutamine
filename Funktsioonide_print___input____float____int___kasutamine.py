#1
print("Tere, maailm")
nimi=input("Mis on sinu nimi?").capitalize()
print(f"Tere maailm!, Tervitan sind {nimi}")
vanus=int(input("Kui vana sa oled?"))
print(f"Tere maailm!, Tervitan sind {nimi} Sa oled {vanus} aastat vana")
#2
vanus = 18
eesnimi = "Jaak"
pikkus = 16.5
kas_k�ib_koolis = True
print(f"muutuja {vanus} on {type(vanus)}")
print(f"muutuja {eesnimi} on {type(eesnimi)}")
print(f"muutuja {pikkus} on {type(pikkus)}")
print(f"muutuja {kas_k�ib_koolis} on {type(kas_k�ib_koolis)}")
#3
from random import *
kommide_arv=randint(10,100)
print(f("Laua peal on {kommide_arv}"))
mitu=int(input("Mitu tahad s��ja?"))
print(f"laua peal on j��nud {kommide_arv-mitu}")