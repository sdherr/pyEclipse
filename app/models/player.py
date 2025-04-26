from enum import StrEnum, auto


class Species(StrEnum):
    Terran = auto()
    Planta = auto()
    Mechanema = auto()
    Eridani = auto()
    Hydran = auto()
    Enlightened = auto()
    Rho_Indi = auto()
    # from Rise of Ancients
    Descendants = auto()
    Orion = auto()
    Exiles = auto()
    Magellan = auto()
    # from Shadow of Rift
    Octantis = auto()
    Shapers = auto()
    Unity = auto()


class Color(StrEnum):
    Blue = auto()
    Green = auto()
    Red = auto()
    White = auto()
    Black = auto()
    Yellow = auto()
    Purple = auto()
    Natural = auto()
    Grey = auto()

class Player:
    # TODO
    pass