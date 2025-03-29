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

class JellyBean(Dessert):
    def __init__(self, name=None, calories=None, flavor=None):
        super().__init__(name, calories)
        self.__flavor = flavor

    def get_flavor(self):
        return self.__flavor

    def set_flavor(self, flavor):
        self.__flavor = flavor

    def get_info(self):
        return self.get_dessert() + (self.get_flavor(),)

    def is_delicious(self):
        if self.__flavor == "black licorice":
            return False
        return True

dessert = Dessert("Апельсин", 50)
print(dessert.get_dessert())
print(dessert.is_healthy())
print(dessert.is_delicious())

print()

jellybean = JellyBean("Торт", 350, "black licorice")
print(jellybean.get_info())
print(jellybean.get_flavor())
print(jellybean.is_healthy())
print(jellybean.is_delicious())
