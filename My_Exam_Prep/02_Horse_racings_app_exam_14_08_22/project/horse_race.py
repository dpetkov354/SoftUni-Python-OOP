from project.func.validators import Validation


class HorseRace:
    def __init__(self, race_type: str):
        self.race_type = race_type
        self.jockeys = []

    @property
    def race_type(self):
        return self.__race_type

    @race_type.setter
    def race_type(self, value):
        if Validation.check_race_type(value):
            self.__race_type = value
