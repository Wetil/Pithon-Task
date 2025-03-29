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

class JellyBean(Dessert):
    def __init__(self, name=None, calories=None, flavor=None):
        super().__init__(name, calories)
        self.__flavor = flavor

    @property
    def flavor(self):
        return self.__flavor

    @flavor.setter
    def flavor(self, flavor):
        self.__flavor = flavor

    def get_info(self):
        return self.name, self.calories, self.__flavor

    def is_delicious(self):
        if self.__flavor == "black licorice":
            return False
        return True

dessert = Dessert("Апельсин", 50)
print(dessert.get_info())
print(dessert.is_healthy())
print(dessert.is_delicious())

print()

jellybean = JellyBean("Торт", 350, "black licorice")
print(jellybean.get_info())
print(jellybean.flavor)
print(jellybean.is_healthy())
print(jellybean.is_delicious())
