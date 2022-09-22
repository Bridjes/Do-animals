import json
import random

class Animals:
    def __init__(self, name, sex):
        self.name = name        # название
        self.sex = sex          # пол
        self.alive = True       # статус жизни

        with open("animals.json") as animal:
            animals = json.load(animal)
            self.kind = animals[name]       # тип питания
        print(f"Появился {self.name} пола {self.sex}, cемейства: {self.kind}")

    #вывести инфу по животному
    def ShowInfo(self):
        print(f"{self.name}, пол: {self.sex}, тип питания: {self.kind}, статус: {self.alive}")

    #съесть кого-то
    def eating(self, Animal):
        if self.kind == "predators" and Animal.kind == "herbivores":
            print(f"{self.name} съел {Animal.name}")
            Animal.alive = False

    #спариться
    def pairing(self, Animal):
        if self.name == Animal.name and self.sex != Animal.sex:
            n = random.randint(1, 2)
            sex = None
            if n == 1:
                sex = "man"
            else:
                sex = "woman"
            print("а вот и киндер подъехал")
            return Animals(self.name, sex)

    # погибнуть
    def __del__(self):
        print(f"{self.name}, погиб во имя великой, но никому не понятной, цели")