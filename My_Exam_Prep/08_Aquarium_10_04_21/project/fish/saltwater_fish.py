from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    INITIAL_SIZE = 5
    INCREMENT_SIZE = 2

    def __init__(self, name, species, price):
        super().__init__(name, species, self.INITIAL_SIZE, price)

    def eat(self):
        self.size += self.INCREMENT_SIZE
