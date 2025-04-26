from enum import Enum, auto
from typing import NamedTuple


class DevelopmentCost(NamedTuple):
    value_: int
    economy: int
    materials: int
    science: int


class Development(DevelopmentCost, Enum):
    Ancient_Monument = DevelopmentCost(auto(), 13, 0, 0)
    Artifact_Link = DevelopmentCost(auto(), 0, 7, 7)
    Diplomatic_Fleet = DevelopmentCost(auto(), 0, 6, 0)
    Mining_Colony = DevelopmentCost(auto(), 5, 0, 5)
    Research_Station = DevelopmentCost(auto(), 5, 5, 0)
    Trade_Fleet = DevelopmentCost(auto(), 0, 5, 5)
    Shellworld = DevelopmentCost(auto(), 0, 20, 0)
    Warp_Portal = DevelopmentCost(auto(), 0, 8, 0)
    # From Shadow of the Rift
    # TODO: These
    Quantum_Labs = DevelopmentCost(auto(), 0, 7, 0)
    Ancient_Labs = DevelopmentCost(auto(), 8, 0, 0)
    Genetics_Labs = DevelopmentCost(auto(), 0, 3, 5)
