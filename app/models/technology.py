from enum import Enum, StrEnum, auto
from random import shuffle
from typing import NamedTuple

from app.models.config import config
from app.models.ships.shipPart import ShipPart as SP


class TechnologyType(StrEnum):
    Military = auto()
    Grid = auto()
    Nano = auto()
    Rare = auto()


class TechnologyAttributes(NamedTuple):
    value_: int
    default_cost: int
    minimum_cost: int
    type: TechnologyType
    ship_part: SP | None


class Technology(TechnologyAttributes, Enum):
    Neutron_Bombs = (auto(), 2, 2, TechnologyType.Military, None)
    Starbase = (auto(), 4, 3, TechnologyType.Military, None)
    Plasma_Cannon = (auto(), 6, 4, TechnologyType.Military, SP.Plasma_Cannon)
    Phase_Shield = (auto(), 8, 5, TechnologyType.Military, SP.Phase_Shield)
    Advanced_Mining = (auto(), 10, 6, TechnologyType.Military, None)
    Tachyon_Source = (auto(), 12, 6, TechnologyType.Military, SP.Tachyon_Source)
    Plasma_Missile = (auto(), 14, 7, TechnologyType.Military, SP.Plasma_Missile)
    Gluon_Computer = (auto(), 16, 8, TechnologyType.Military, SP.Gluon_Computer)
    Gauss_Shield = (auto(), 2, 2, TechnologyType.Grid, SP.Gauss_Shield)
    Improved_Hull = (auto(), 4, 3, TechnologyType.Grid, SP.Improved_Hull)
    Fusion_Source = (auto(), 6, 4, TechnologyType.Grid, SP.Fusion_Source)
    Positron_Computer = (auto(), 8, 5, TechnologyType.Grid, SP.Positron_Computer)
    Advanced_Economy = (auto(), 10, 6, TechnologyType.Grid, None)
    Tachyon_Drive = (auto(), 12, 6, TechnologyType.Grid, SP.Tachyon_Drive)
    Antimatter_Cannon = (auto(), 14, 7, TechnologyType.Grid, SP.Antimatter_Cannon)
    Quantum_Grid = (auto(), 16, 8, TechnologyType.Grid, None)
    Nanorobots = (auto(), 2, 2, TechnologyType.Nano, None)
    Fusion_Drive = (auto(), 4, 3, TechnologyType.Nano, SP.Fusion_Drive)
    Advanced_Robotics = (auto(), 6, 4, TechnologyType.Nano, None)
    Orbital = (auto(), 8, 5, TechnologyType.Nano, None)
    Advanced_Labs = (auto(), 10, 6, TechnologyType.Nano, None)
    Monolith = (auto(), 12, 6, TechnologyType.Nano, None)
    Artifact_Key = (auto(), 14, 7, TechnologyType.Nano, None)
    Wormhole_Generator = (auto(), 16, 8, TechnologyType.Nano, None)
    # From Rise of the Ancients
    Antimatter_Splitter = (auto(), 5, 5, TechnologyType.Rare, None)
    Neutron_Absorber = (auto(), 5, 5, TechnologyType.Rare, None)
    Distortion_Shield = (auto(), 7, 6, TechnologyType.Rare, None)
    Cloaking_Device = (auto(), 7, 6, TechnologyType.Rare, None)
    Point_Defence = (auto(), 11, 8, TechnologyType.Rare, None)
    Conifold_Field = (auto(), 5, 5, TechnologyType.Rare, SP.Conifold_Field)
    Sentient_Hull = (auto(), 5, 5, TechnologyType.Rare, SP.Sentient_Hull)
    Interceptor_Bay = (auto(), 9, 7, TechnologyType.Rare, SP.Interceptor_Bay)
    Flux_Missile = (auto(), 11, 8, TechnologyType.Rare, SP.Flux_Missile)
    Zero_Point_Source = (auto(), 15, 10, TechnologyType.Rare, SP.Zero_Point_Source)
    # From Shadow of the Rift
    Advanced_Genetics = (auto(), 7, 6, TechnologyType.Rare, None)
    Metasynthesis = (auto(), 17, 11, TechnologyType.Rare, None)
    Rift_Cannon = (auto(), 9, 7, TechnologyType.Rare, SP.Rift_Cannon)
    Soliton_Cannon = (auto(), 9, 7, TechnologyType.Rare, SP.Soliton_Cannon)
    Absorption_Shield = (auto(), 7, 6, TechnologyType.Rare, SP.Absorption_Shield)
    Transition_Drive = (auto(), 9, 7, TechnologyType.Rare, SP.Transition_Drive)

    @classmethod
    def init_technologies(cls) -> list["Technology"]:
        ret = []
        for _ in range(5):
            ret.extend([cls.Neutron_Bombs, cls.Starbase, cls.Plasma_Cannon, cls.Gauss_Shield, cls.Improved_Hull])
            ret.extend([cls.Fusion_Source, cls.Nanorobots, cls.Fusion_Drive, cls.Advanced_Robotics])
        for _ in range(4):
            ret.extend([cls.Advanced_Mining, cls.Advanced_Economy, cls.Advanced_Labs])
            ret.extend([cls.Positron_Computer, cls.Orbital, cls.Phase_Shield])
        for _ in range(3):
            ret.extend([cls.Tachyon_Source, cls.Tachyon_Drive, cls.Plasma_Missile, cls.Gluon_Computer])
            ret.extend([cls.Antimatter_Cannon, cls.Quantum_Grid, cls.Monolith, cls.Artifact_Key])
            ret.append(cls.Wormhole_Generator)

        if config.number_of_players > 6:
            # An extra one of each, with some exceptions.
            for tech in Technology:
                if (
                    tech.type == TechnologyType.Rare
                    or tech.default_cost == 2
                    or tech in (cls.Starbase, cls.Tachyon_Drive, cls.Artifact_Key)
                ):
                    continue
                ret.append(tech)

        rare = []
        if config.rota_rare_technologies:
            rare.extend([cls.Antimatter_Splitter, cls.Distortion_Shield, cls.Cloaking_Device, cls.Point_Defence])
            rare.extend([cls.Conifold_Field, cls.Sentient_Hull, cls.Interceptor_Bay, cls.Flux_Missile])
            rare.append(cls.Zero_Point_Source)

        if config.sotr_rare_technologies:
            rare.extend([cls.Absorption_Shield, cls.Metasynthesis, cls.Rift_Cannon, cls.Soliton_Cannon])
            rare.append(cls.Transition_Drive)
            if config.sotr_evolution:
                rare.append(cls.Advanced_Genetics)

        # max of 12 rare technoloies
        shuffle(rare)
        ret.extend(rare[0:12])

        return ret
