from classes import Animals
import json
import random

class Antilop(Animals):
    def __init__(self, name, sex):
        super().__init__(name, sex)
        with open("Antilopes/antilopesNames.json", encoding="utf-8") as f:
            lns = json.load(f)
            n = random.randint(0, len(lns[self.sex]) - 1)     # выдаёт случайный индекс для списка имён
            self.alias = lns[self.sex][n]   # выдаёт имя по выбранному полу и указанному индексу
        self.age = 0           # возраст
        print(f"по имени {self.alias}")

    # спаривание
    def pairing(self, Animal):
        if self.name == Animal.name and self.sex != Animal.sex and self.age > 4:
            n = random.randint(1, 2)
            sex = None
            if n == 1:
                sex = "man"
            else:
                sex = "woman"
            print("Антилопа родила:")
            return Antilop(self.name, sex)

    # повзрослеть
    def skip_year(self, year = 1):
        self.age += year
        print(f"Антилопа {self.alias} позврослела на {year} л.")