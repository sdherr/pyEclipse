from enum import StrEnum, auto


class WorldType(StrEnum):
    ORANGE = auto()
    PINK = auto()
    BROWN = auto()
    WHITE = auto()
    ORBITAL = auto()


class PopulationSlot:
    def __init__(self, advanced: bool):
        self.empty = True
        self.advanced = advanced


class World:
    def __init__(self, type: WorldType, population: int, advancedPopulation: int = 0):
        self.type = type
        self.slots: list[PopulationSlot] = []
        for _ in range(population):
            self.slots.append(PopulationSlot(False))
        for _ in range(advancedPopulation):
            self.slots.append(PopulationSlot(True))
