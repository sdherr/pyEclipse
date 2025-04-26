from enum import Enum, auto
from typing import NamedTuple


class EvolutionAttributes(NamedTuple):
    value_: int
    cost: int


class EvolutionType(EvolutionAttributes, Enum):
    Extra_Build = EvolutionAttributes(auto(), 2)
    Extra_Upgrade = EvolutionAttributes(auto(), 3)
    Extra_Reputation_Ambassidor_Slot = EvolutionAttributes(auto(), 3)
    Extra_Reputation_Draw = EvolutionAttributes(auto(), 2)
    Extra_Research = EvolutionAttributes(auto(), 5)
    Extra_Evolution = EvolutionAttributes(auto(), 3)
    Extra_Colony_Ship = EvolutionAttributes(auto(), 2)
    Extra_Move = EvolutionAttributes(auto(), 3)
    Cheap_Interceptor = EvolutionAttributes(auto(), 3)
    Cheap_Cruiser = EvolutionAttributes(auto(), 3)
    Cheap_Dreadnought = EvolutionAttributes(auto(), 3)
    Cheap_Orbital = EvolutionAttributes(auto(), 3)
    Cheap_Monolith = EvolutionAttributes(auto(), 3)
    Additional_Pink = EvolutionAttributes(auto(), 5)
    Additional_Brown = EvolutionAttributes(auto(), 5)
    Additional_Orange = EvolutionAttributes(auto(), 5)
    Trading_Pink = EvolutionAttributes(auto(), 2)
    Trading_Brown = EvolutionAttributes(auto(), 2)
    Trading_Orange = EvolutionAttributes(auto(), 2)
    VP_Evolution = EvolutionAttributes(auto(), 8)
    VP_Orbital = EvolutionAttributes(auto(), 3)
    VP_Monolith = EvolutionAttributes(auto(), 4)
    VP_Sectors = EvolutionAttributes(auto(), 3)
    VP_Reputation = EvolutionAttributes(auto(), 3)
    VP_Galactic_Center = EvolutionAttributes(auto(), 4)
    VP_Artifact = EvolutionAttributes(auto(), 6)
