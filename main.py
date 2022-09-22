from Lions.lions import Lion
from Antilopes.antilopes import Antilop
from Сrocodiles.crocodiles import Crocodile

animal1 = Lion("lion", "man")
animal2 = Lion("lion", "woman")
print()
animal1.skip_year(4)
animal2.skip_year(4)
print()
animal3 = animal2.pairing(animal1)
print()
animal4 = Antilop("antelope", "woman")
animal2.squirm(animal4)
print()
animal5 = Crocodile("crocodile", "man")
print()

print("="*20 + "конец" + "="*20)