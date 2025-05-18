from enum import Enum, auto
from typing import NamedTuple


class EvolutionAttributes(NamedTuple):
    value_: int
    cost: int


class Evolution(EvolutionAttributes, Enum):
    Extra_Build = (auto(), 2)
    Extra_Upgrade = (auto(), 3)
    Extra_Reputation_Ambassidor_Slot = (auto(), 3)
    Extra_Reputation_Draw = (auto(), 2)
    Extra_Research = (auto(), 5)
    Extra_Evolution = (auto(), 3)
    Extra_Colony_Ship = (auto(), 2)
    Extra_Move = (auto(), 3)
    Cheap_Interceptor = (auto(), 3)
    Cheap_Cruiser = (auto(), 3)
    Cheap_Dreadnought = (auto(), 3)
    Cheap_Orbital = (auto(), 3)
    Cheap_Monolith = (auto(), 3)
    Additional_Pink = (auto(), 5)
    Additional_Brown = (auto(), 5)
    Additional_Orange = (auto(), 5)
    Trading_Pink = (auto(), 2)
    Trading_Brown = (auto(), 2)
    Trading_Orange = (auto(), 2)
    VP_Evolution = (auto(), 8)
    VP_Orbital = (auto(), 3)
    VP_Monolith = (auto(), 4)
    VP_Sectors = (auto(), 3)
    VP_Reputation = (auto(), 3)
    VP_Galactic_Center = (auto(), 4)
    VP_Artifact = (auto(), 6)

    @classmethod
    def init_evolution(cls) -> list["Evolution"]:
        ret = list(Evolution)  # Start with one of each
        # Plus a few doubles and one triple (Extra_Upgrade).
        ret.extend([cls.Extra_Build, cls.Extra_Reputation_Draw, cls.Extra_Research, cls.Extra_Move])
        ret.extend([cls.VP_Evolution, cls.Extra_Evolution, cls.Extra_Upgrade, cls.Extra_Upgrade])
        return ret
