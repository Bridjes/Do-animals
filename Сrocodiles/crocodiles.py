from classes import Animals
import json
import random

class Crocodile(Animals):
    def __init__(self, name = "crocodile", sex = "man" if random.randint(0, 1) == 1 else "woman", age = 0):
        super().__init__(name, sex)
        with open("Сrocodiles/crocodileNames.json", encoding="utf-8") as f:
            lns = json.load(f)
            n = random.randint(0, len(lns[self._sex]) - 1)     # выдаёт случайный индекс для списка имён
            self.alias = lns[self._sex][n]   # выдаёт имя по выбранному полу и указанному индексу
        self.__age = age           # возраст (теперь доступен только в этом классе)
        print(f"по имени {self.alias}")

    def ShowInfo(self):
        alive = "жив" if self._alive else "мёртв"
        print(f"Крокодил {self.alias}, возраст {self.__age}, статус жизни: {alive}")

    # спаривание
    def pairing(self, Animal):
        if self._name == Animal._name and self._sex != Animal._sex and self.__age > 4:
            n = random.randint(1, 2)
            sex = None
            if n == 1:
                sex = "man"
            else:
                sex = "woman"
            print(f"Крокодилиха родила:")
            return Crocodile(self._name, sex)

    # показать возраст
    def get_age(self):
        return self.__age

    # изменить возраст (только в большую сторону)
    def set_age(self, y):
        if y > self.__age:
            self.__age = y

    # показать, что возраст удалить нельзя
    def del_age(self):
        print("удаление не доступно")

    age = property(get_age, set_age, del_age, "возраст")

    # рявкнуть
    def squirm(self, animal):
        if animal._kind == "herbivores":
            if self._sex == "man":
                print(f"Крокодил {self.alias} зарычал, {animal._name} дал драпу")
            else:
                print(f"Крокодил {self.alias} зарычала, {animal._name} дал драпу")