from enum import Enum, StrEnum, auto

from ships.shipPart import ShipPart as SP


class TechnologyType(StrEnum):
    Military = auto()
    Grid = auto()
    Nano = auto()
    Rare = auto()


class TechnologyAttributes:
    value_: int
    default_cost: int
    minimum_cost: int
    type: TechnologyType
    ship_part: SP | None


class Technology(Enum, TechnologyAttributes):
    Neutron_Bombs = TechnologyAttributes(auto(), 2, 2, TechnologyType.Military, None)
    Starbase = TechnologyAttributes(auto(), 4, 3, TechnologyType.Military, None)
    Plasma_Cannon = TechnologyAttributes(auto(), 6, 4, TechnologyType.Military, SP.Plasma_Cannon)
    Phase_Shield = TechnologyAttributes(auto(), 8, 5, TechnologyType.Military, SP.Phase_Shield)
    Advanced_Mining = TechnologyAttributes(auto(), 10, 6, TechnologyType.Military, None)
    Tachyon_Source = TechnologyAttributes(auto(), 12, 6, TechnologyType.Military, SP.Tachyon_Source)
    Plasma_Missile = TechnologyAttributes(auto(), 14, 7, TechnologyType.Military, SP.Plasma_Missile)
    Gluon_Computer = TechnologyAttributes(auto(), 16, 8, TechnologyType.Military, SP.Gluon_Computer)
    Gauss_Shield = TechnologyAttributes(auto(), 2, 2, TechnologyType.Grid, SP.Gauss_Shield)
    Improved_Hull = TechnologyAttributes(auto(), 4, 3, TechnologyType.Grid, SP.Improved_Hull)
    Fusion_Source = TechnologyAttributes(auto(), 6, 4, TechnologyType.Grid, SP.Fusion_Source)
    Positron_Computer = TechnologyAttributes(auto(), 8, 5, TechnologyType.Grid, SP.Positron_Computer)
    Advanced_Economy = TechnologyAttributes(auto(), 10, 6, TechnologyType.Grid, None)
    Tachyon_Drive = TechnologyAttributes(auto(), 12, 6, TechnologyType.Grid, SP.Tachyon_Drive)
    Antimatter_Cannon = TechnologyAttributes(auto(), 14, 7, TechnologyType.Grid, SP.Antimatter_Cannon)
    Quantum_Grid = TechnologyAttributes(auto(), 16, 8, TechnologyType.Grid, None)
    Nanorobots = TechnologyAttributes(auto(), 2, 2, TechnologyType.Nano, None)
    Fusion_Drive = TechnologyAttributes(auto(), 4, 3, TechnologyType.Nano, SP.Fusion_Drive)
    Advanced_Robotics = TechnologyAttributes(auto(), 6, 4, TechnologyType.Nano, None)
    Orbital = TechnologyAttributes(auto(), 8, 5, TechnologyType.Nano, None)
    Advanced_Labs = TechnologyAttributes(auto(), 10, 6, TechnologyType.Nano, None)
    Monolith = TechnologyAttributes(auto(), 12, 6, TechnologyType.Nano, None)
    Artifact_Key = TechnologyAttributes(auto(), 14, 7, TechnologyType.Nano, None)
    Wormhole_Generator = TechnologyAttributes(auto(), 16, 8, TechnologyType.Nano, None)
    # From Rise of the Ancients
    Antimatter_Splitter = TechnologyAttributes(auto(), 5, 5, TechnologyType.Rare, None)
    Neutron_Absorber = TechnologyAttributes(auto(), 5, 5, TechnologyType.Rare, None)
    Distortion_Shield = TechnologyAttributes(auto(), 7, 6, TechnologyType.Rare, None)
    Cloaking_Device = TechnologyAttributes(auto(), 7, 6, TechnologyType.Rare, None)
    Point_Defence = TechnologyAttributes(auto(), 11, 8, TechnologyType.Rare, None)
    Conifold_Field = TechnologyAttributes(auto(), 5, 5, TechnologyType.Rare, SP.Conifold_Field)
    Sentient_Hull = TechnologyAttributes(auto(), 5, 5, TechnologyType.Rare, SP.Sentient_Hull)
    Interceptor_Bay = TechnologyAttributes(auto(), 9, 7, TechnologyType.Rare, SP.Interceptor_Bay)
    Flux_Missile = TechnologyAttributes(auto(), 11, 8, TechnologyType.Rare, SP.Flux_Missile)
    Zero_Point_Source = TechnologyAttributes(auto(), 15, 10, TechnologyType.Rare, SP.Zero_Point_Source)
    # From Shadow of the Rift
    Advanced_Genetics = TechnologyAttributes(auto(), 7, 6, TechnologyType.Rare, None)
    Metasynthesis = TechnologyAttributes(auto(), 17, 11, TechnologyType.Rare, None)
    Rift_Cannon = TechnologyAttributes(auto(), 9, 7, TechnologyType.Rare, SP.Rift_Cannon)
    Soliton_Cannon = TechnologyAttributes(auto(), 9, 7, TechnologyType.Rare, SP.Soliton_Cannon)
    Absorption_Shield = TechnologyAttributes(auto(), 7, 6, TechnologyType.Rare, SP.Absorption_Shield)
    Transition_Drive = TechnologyAttributes(auto(), 9, 7, TechnologyType.Rare, SP.Transition_Drive)
