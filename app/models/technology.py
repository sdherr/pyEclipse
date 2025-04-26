from enum import Enum, StrEnum, auto


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


class Technology(Enum, TechnologyAttributes):
    Neutron_Bombs = TechnologyAttributes(auto(), 2, 2, TechnologyType.Military)
    Starbase = TechnologyAttributes(auto(), 4, 3, TechnologyType.Military)
    Plasma_Cannon = TechnologyAttributes(auto(), 6, 4, TechnologyType.Military)
    Phase_Shield = TechnologyAttributes(auto(), 8, 5, TechnologyType.Military)
    Advanced_Mining = TechnologyAttributes(auto(), 10, 6, TechnologyType.Military)
    Tachyon_Source = TechnologyAttributes(auto(), 12, 6, TechnologyType.Military)
    Plasma_Missile = TechnologyAttributes(auto(), 14, 7, TechnologyType.Military)
    Gluon_Computer = TechnologyAttributes(auto(), 16, 8, TechnologyType.Military)
    Gauss_Shield = TechnologyAttributes(auto(), 2, 2, TechnologyType.Grid)
    Improved_Hull = TechnologyAttributes(auto(), 4, 3, TechnologyType.Grid)
    Fusion_Source = TechnologyAttributes(auto(), 6, 4, TechnologyType.Grid)
    Positron_Computer = TechnologyAttributes(auto(), 8, 5, TechnologyType.Grid)
    Advanced_Economy = TechnologyAttributes(auto(), 10, 6, TechnologyType.Grid)
    Tachyon_Drive = TechnologyAttributes(auto(), 12, 6, TechnologyType.Grid)
    Antimatter_Cannon = TechnologyAttributes(auto(), 14, 7, TechnologyType.Grid)
    Quantum_Grid = TechnologyAttributes(auto(), 16, 8, TechnologyType.Grid)
    Nanorobots = TechnologyAttributes(auto(), 2, 2, TechnologyType.Nano)
    Fusion_Drive = TechnologyAttributes(auto(), 4, 3, TechnologyType.Nano)
    Advanced_Robotics = TechnologyAttributes(auto(), 6, 4, TechnologyType.Nano)
    Orbital = TechnologyAttributes(auto(), 8, 5, TechnologyType.Nano)
    Advanced_Labs = TechnologyAttributes(auto(), 10, 6, TechnologyType.Nano)
    Monolith = TechnologyAttributes(auto(), 12, 6, TechnologyType.Nano)
    Artifact_Key = TechnologyAttributes(auto(), 14, 7, TechnologyType.Nano)
    Wormhole_Generator = TechnologyAttributes(auto(), 16, 8, TechnologyType.Nano)
    # From Rise of the Ancients
    Antimatter_Splitter = TechnologyAttributes(auto(), 5, 5, TechnologyType.Rare)
    Neutron_Absorber = TechnologyAttributes(auto(), 5, 5, TechnologyType.Rare)
    Distortion_Shield = TechnologyAttributes(auto(), 7, 6, TechnologyType.Rare)
    Cloaking_Device = TechnologyAttributes(auto(), 7, 6, TechnologyType.Rare)
    Point_Defence = TechnologyAttributes(auto(), 11, 8, TechnologyType.Rare)
    Conifold_Field = TechnologyAttributes(auto(), 5, 5, TechnologyType.Rare)
    Sentient_Hull = TechnologyAttributes(auto(), 5, 5, TechnologyType.Rare)
    Interceptor_Bay = TechnologyAttributes(auto(), 9, 7, TechnologyType.Rare)
    Flux_Missile = TechnologyAttributes(auto(), 11, 8, TechnologyType.Rare)
    Zero_Point_Source = TechnologyAttributes(auto(), 15, 10, TechnologyType.Rare)
    # From Shadow of the Rift
    # TODO: these
    Advanced_Genetics = TechnologyAttributes(auto(), 7, 6, TechnologyType.Rare)
    Metasynthesis = TechnologyAttributes(auto(), 17, 11, TechnologyType.Rare)
    Rift_Cannon = TechnologyAttributes(auto(), 9, 7, TechnologyType.Rare)
    Soliton_Cannon = TechnologyAttributes(auto(), 9, 7, TechnologyType.Rare)
    Absorption_Shield = TechnologyAttributes(auto(), 7, 6, TechnologyType.Rare)
    Transition_Drive = TechnologyAttributes(auto(), 9, 7, TechnologyType.Rare)
