from project.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):
    INITIAL_CAPACITY = 25
    FISH_TYPES = ('SaltwaterFish',)

    def __init__(self, name):
        super().__init__(name, self.INITIAL_CAPACITY)
