import json
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, sex):
        self._name = name        # название  (доступен только в этом и дочерних классах)
        self._sex = sex          # пол (доступен только в этом и дочерних классах_
        self._alive = True      # статус жизни (доступен только внутри этого класса)

        with open("animals.json") as animal:
            animals = json.load(animal)
            self._kind = animals[name]       # тип питания
        print(f"Появился {self._name} пола {self._sex}, cемейства: {self._kind}")

    #вывести инфу по животному
    @abstractmethod
    def ShowInfo(self):
        pass
    #съесть кого-то
    def eating(self, Animal):
        if self._kind == "predators" and Animal._kind == "herbivores":
            print(f"{self._name} съел {Animal._name}")
            Animal.__alive = False

    #спариться
    @abstractmethod
    def pairing(self, Animal):
        pass

    # погибнуть
    def __del__(self):
        print(f"{self._name}, погиб во имя великой, но никому не понятной, цели")