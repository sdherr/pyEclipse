from enum import Enum, auto
from typing import NamedTuple

from config import config


class DevelopmentCost(NamedTuple):
    value_: int
    economy: int
    materials: int
    science: int


class Development(DevelopmentCost, Enum):
    Ancient_Monument = (auto(), 13, 0, 0)
    Artifact_Link = (auto(), 0, 7, 7)
    Diplomatic_Fleet = (auto(), 0, 6, 0)
    Mining_Colony = (auto(), 5, 0, 5)
    Research_Station = (auto(), 5, 5, 0)
    Trade_Fleet = (auto(), 0, 5, 5)
    Shellworld = (auto(), 0, 20, 0)
    Warp_Portal = (auto(), 0, 8, 0)
    # From Shadow of the Rift
    # TODO: These
    Quantum_Labs = (auto(), 0, 7, 0)
    Ancient_Labs = (auto(), 8, 0, 0)
    Genetics_Labs = (auto(), 0, 3, 5)

    @classmethod
    def init_developments(cls) -> list["Development"]:
        ret = []
        if config.rota_developments:
            ret.extend([cls.Ancient_Monument, cls.Artifact_Link, cls.Diplomatic_Fleet, cls.Mining_Colony])
            ret.extend([cls.Research_Station, cls.Trade_Fleet, cls.Shellworld])
            if config.rota_warp_portal:
                ret.append(cls.Warp_Portal)

        if config.sotr_developments:
            ret.extend([cls.Quantum_Labs, cls.Ancient_Labs, cls.Ancient_Monument])

        return ret
