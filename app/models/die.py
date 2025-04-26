from enum import StrEnum, auto


class Die(StrEnum):
    Yellow = auto()
    Orange = auto()
    Blue = auto()
    Red = auto()
    Pink = auto()
    Grey = auto()
    # TODO: Implement ping and grey

    @property
    def damage(self) -> int:
        if self == Die.Yellow:
            return 1
        elif self == Die.Orange:
            return 2
        elif self == Die.Blue:
            return 3
        elif self == Die.Red:
            return 4
