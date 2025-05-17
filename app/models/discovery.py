from enum import StrEnum, auto

from config import config


class DiscoveryTile(StrEnum):
    Money = auto()
    Science = auto()
    Materials = auto()
    Ancient_Technology = auto()
    Ancient_Cruiser = auto()
    Axon_Computer = auto()
    Hypergrid_Source = auto()
    Shard_Hull = auto()
    Ion_Turret = auto()
    Conformal_Drive = auto()
    Flux_Shield = auto()
    # From Rise of the Ancients
    Money_Science_Materials = auto()
    Ancient_Warp_Portal = auto()
    Ancient_Orbital = auto()
    Jump_Drive = auto()
    Muon_Source = auto()
    Morph_Shield = auto()
    Ion_Disruptor = auto()
    # From Nebula
    Ancient_Monolith = auto()
    # From Shadow of the Rift
    Plasma_Turret = auto()
    Soliton_Turret = auto()
    Rift_Turret = auto()
    Inversion_Shield = auto()
    Rapid_Mutation = auto()
    Accelerated_Evolution = auto()
    Transmatter_Quantifier = auto()
    Rift_Orbital = auto()
    Rift_Movement = auto()

    @classmethod
    def init_discoveries(cls) -> list["DiscoveryTile"]:
        ret = [cls.Axon_Computer, cls.Hypergrid_Source, cls.Shard_Hull, cls.Ion_Turret]
        ret.extend([cls.Conformal_Drive, cls.Flux_Shield])
        for _ in range(3):  # 3 each of these
            ret.extend([cls.Money, cls.Science, cls.Materials, cls.Ancient_Cruiser, cls.Ancient_Technology])

        if config.rota_discoveries:
            ret.extend([cls.Morph_Shield, cls.Ion_Disruptor, cls.Muon_Source, cls.Jump_Drive])
            for _ in range(2):  # 2 each of these
                ret.extend([cls.Money_Science_Materials, cls.Ancient_Orbital])

        if config.nebula_discoveries:
            ret.add(cls.Ancient_Monolith)

        if config.sotr_discoveries:
            ret.extend([cls.Plasma_Turret, cls.Soliton_Turret, cls.Rift_Turret, cls.Inversion_Shield])
            ret.extend([cls.Transmatter_Quantifier, cls.Rift_Movement, cls.Rift_Orbital])
        if config.sotr_evolution:
            ret.extend([cls.Rapid_Mutation, cls.Accelerated_Evolution])
        return ret
