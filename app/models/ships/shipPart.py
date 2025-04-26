from enum import Enum, auto

from app.models.die import Die


class ShipPartAttributes:
    power: int
    initiative: int
    hull: int
    computers: int
    shields: int
    driveThrust: int
    regeneration: int
    interceptorBays: int
    guns: list[Die]
    missiles: list[Die]

    def __init__(self, name: str, power: int = 0, initiative: int = 0, hull: int = 0, computers: int = 0,
                 shields: int = 0, driveThrust: int = 0 , regeneration: int = 0, interceptorBays: int = 0,
                 guns: list[Die] = [], missiles: list[Die] = []):
        self.name = name
        self.power = power
        self.initiative = initiative
        self.hull = hull
        self.computers = computers
        self.shields = shields
        self.driveThrust = driveThrust
        self.regeneration = regeneration
        self.interceptorBays = interceptorBays
        self.guns = guns
        self.missiles = missiles


class ShipPart(ShipPartAttributes, Enum):
    Empty = ShipPartAttributes(auto())
    Non_Existent = ShipPartAttributes(auto())
    Hull = ShipPartAttributes(auto(), hull=1)
    Improved_Hull = ShipPartAttributes(auto(), hull=2)
    Shard_Hull = ShipPartAttributes(auto(), hull=3)
    Conifold_Field = ShipPartAttributes(auto(), power=2, hull=3)
    Electron_Computer = ShipPartAttributes(auto(), computers=1)
    Sentient_Hull = ShipPartAttributes(auto(), hull=1, computers=1)
    Positron_Computer = ShipPartAttributes(auto(), power=1, initiative=1, computers=2)
    Gluon_Computer = ShipPartAttributes(auto(), power=2, initiative=2, computers=3)
    Axion_Computer = ShipPartAttributes(auto(), computers=3)
    Nuclear_Source = ShipPartAttributes(auto(), power=-3)
    Fusion_Source = ShipPartAttributes(auto(), power=-6)
    Tachyon_Source = ShipPartAttributes(auto(), power=-9)
    Zero_Point_Source = ShipPartAttributes(auto(), power=-12)
    Hypergrid_Source = ShipPartAttributes(auto(), power=-11)
    Muon_Source = ShipPartAttributes(auto(), power=-2, initiative=1)
    Nuclear_Drive = ShipPartAttributes(auto(), power=1, initiative=1, driveThrust=1)
    Fusion_Drive = ShipPartAttributes(auto(), power=2, initiative=2, driveThrust=2)
    Tachyon_Drive = ShipPartAttributes(auto(), power=3, initiative=3, driveThrust=3)
    Conformal_Drive = ShipPartAttributes(auto(), power=2, initiative=2, driveThrust=4)
    Jump_Drive = ShipPartAttributes(auto(), power=2, driveThrust=1)
    Gauss_Shield = ShipPartAttributes(auto(), shields=1)
    Phase_Shield = ShipPartAttributes(auto(), power=1, shields=2)
    Flux_Shield = ShipPartAttributes(auto(), power=2, shields=3)
    Ancient_Shield = ShipPartAttributes(auto(), regeneration=2) # only found on Ancient Dreadnaught
    Morph_Shield = ShipPartAttributes(auto(), initiative=2, shields=1, regeneration=1)
    Ion_Cannon = ShipPartAttributes(auto(), power=1, guns=[Die.Yellow])
    Ion_Disruptor = ShipPartAttributes(auto(), initiative=3, guns=[Die.Yellow])
    Ion_Turret = ShipPartAttributes(auto(), power=1, guns=[Die.Yellow, Die.Yellow])
    Plasma_Cannon = ShipPartAttributes(auto(), power=2, guns=[Die.Orange])
    Antimatter_Cannon = ShipPartAttributes(auto(), power=4, guns=[Die.Red])
    Flux_Missile = ShipPartAttributes(auto(), initiative=2, missiles=[Die.Yellow, Die.Yellow])
    Plasma_Missile = ShipPartAttributes(auto(), missiles=[Die.Orange, Die.Orange])
    Antimatter_Missile = ShipPartAttributes(auto(), missiles=[Die.Red]) # only found on Ancient Cruiser
    Interceptor_Bay = ShipPartAttributes(auto(), power=2, hull=1, interceptorBays=2)
    # From Shadow of the Rift
    Soliton_Cannon = ShipPartAttributes(auto(), power=3, guns=[Die.Blue])
    Rift_Cannon = ShipPartAttributes(auto(), power=1, guns=[Die.Pink])
    Anomoly_Cannon = ShipPartAttributes(auto(), guns=[Die.Grey]) # only found on mobile Anomalies, plannet killer gun
    Plasma_Turret = ShipPartAttributes(auto(), power=3, guns=[Die.Orange, Die.Orange])
    Soliton_Turret = ShipPartAttributes(auto(), power=2, initiative=-2, guns=[Die.Blue, Die.Blue])
    Rift_Turret = ShipPartAttributes(auto(), guns=[Die.Pink, Die.Pink])
    Antimatter_Accelerator = ShipPartAttributes(auto(), power=1, guns=[Die.Red]) # only found on Pyxis Deathmoon
    Absorption_Shield = ShipPartAttributes(auto(), power=4, shields=1)
    Inversion_Shield = ShipPartAttributes(auto(), power=2, shields=2)
    Transition_Drive = ShipPartAttributes(auto(), initiative=-1, driveThrust=3)
