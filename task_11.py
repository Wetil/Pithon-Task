class Dessert:
    def __init__(self, name=None, calories=None):
        self.__name = name
        self.__calories = calories

    def get_dessert(self):
        return self.__name, self.__calories

    def set_dessert(self, name, calories):
        self.__name = name
        self.__calories = calories

    def is_healthy(self):
        if(self.__calories != None and self.__calories < 200):
            return True
        return False

    def is_delicious(self):
        return True

dessert = Dessert("Апельсин", 50)
print(dessert.get_dessert())
print(dessert.is_healthy())
print(dessert.is_delicious())
