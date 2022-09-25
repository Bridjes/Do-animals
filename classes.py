import json
import random

class Animals:
    def __init__(self, name, sex):
        self._name = name        # название  (доступен только в этом и дочерних классах)
        self._sex = sex          # пол (доступен только в этом и дочерних классах_
        self._alive = True      # статус жизни (доступен только внутри этого класса)

        with open("animals.json") as animal:
            animals = json.load(animal)
            self._kind = animals[name]       # тип питания
        print(f"Появился {self._name} пола {self._sex}, cемейства: {self._kind}")

    #вывести инфу по животному
    def ShowInfo(self):
        print(f"{self._name}, пол: {self._sex}, тип питания: {self._kind}, статус жизни: {self.__alive}")

    #съесть кого-то
    def eating(self, Animal):
        if self._kind == "predators" and Animal._kind == "herbivores":
            print(f"{self._name} съел {Animal._name}")
            Animal.__alive = False

    #спариться
    def pairing(self, Animal):
        if self._name == Animal._name and self._sex != Animal._sex:
            n = random.randint(1, 2)
            sex = None
            if n == 1:
                sex = "man"
            else:
                sex = "woman"
            print("а вот и киндер подъехал")
            return Animals(self._name, sex)

    # погибнуть
    def __del__(self):
        print(f"{self._name}, погиб во имя великой, но никому не понятной, цели")