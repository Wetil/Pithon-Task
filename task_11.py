class Dessert:
    def __init__(self, name=None, calories=None):
        self.__name = name
        self.__calories = calories

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def calories(self):
        return self.__calories

    @calories.setter
    def calories(self, calories):
        self.__calories = calories

    def get_info(self):
        return self.__name, self.__calories

    def is_healthy(self):
        if(self.__calories != None and self.__calories < 200):
            return True
        return False

    def is_delicious(self):
        return True

dessert = Dessert("Апельсин", 50)
print(dessert.get_info())
print(dessert.is_healthy())
print(dessert.is_delicious())
