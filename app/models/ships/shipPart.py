from enum import Enum, auto
from typing import NamedTuple

from app.models.die import Die


class ShipPartAttributes(NamedTuple):
    id: int
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


def _attr_generator(
    id: int,
    *,
    power: int = 0,
    initiative: int = 0,
    hull: int = 0,
    computers: int = 0,
    shields: int = 0,
    driveThrust: int = 0,
    regeneration: int = 0,
    interceptorBays: int = 0,
    guns: list[Die] = [],
    missiles: list[Die] = [],
):
    return (
        id,
        power,
        initiative,
        hull,
        computers,
        shields,
        driveThrust,
        regeneration,
        interceptorBays,
        guns,
        missiles,
    )


class ShipPart(ShipPartAttributes, Enum):
    Empty = _attr_generator(auto())
    Non_Existent = _attr_generator(auto())
    Hull = _attr_generator(auto(), hull=1)
    Improved_Hull = _attr_generator(auto(), hull=2)
    Shard_Hull = _attr_generator(auto(), hull=3)
    Conifold_Field = _attr_generator(auto(), power=2, hull=3)
    Electron_Computer = _attr_generator(auto(), computers=1)
    Sentient_Hull = _attr_generator(auto(), hull=1, computers=1)
    Positron_Computer = _attr_generator(auto(), power=1, initiative=1, computers=2)
    Gluon_Computer = _attr_generator(auto(), power=2, initiative=2, computers=3)
    Axion_Computer = _attr_generator(auto(), computers=3)
    Nuclear_Source = _attr_generator(auto(), power=-3)
    Fusion_Source = _attr_generator(auto(), power=-6)
    Tachyon_Source = _attr_generator(auto(), power=-9)
    Zero_Point_Source = _attr_generator(auto(), power=-12)
    Hypergrid_Source = _attr_generator(auto(), power=-11)
    Muon_Source = _attr_generator(auto(), power=-2, initiative=1)
    Nuclear_Drive = _attr_generator(auto(), power=1, initiative=1, driveThrust=1)
    Fusion_Drive = _attr_generator(auto(), power=2, initiative=2, driveThrust=2)
    Tachyon_Drive = _attr_generator(auto(), power=3, initiative=3, driveThrust=3)
    Conformal_Drive = _attr_generator(auto(), power=2, initiative=2, driveThrust=4)
    Jump_Drive = _attr_generator(auto(), power=2, driveThrust=1)
    Gauss_Shield = _attr_generator(auto(), shields=1)
    Phase_Shield = _attr_generator(auto(), power=1, shields=2)
    Flux_Shield = _attr_generator(auto(), power=2, shields=3)
    Ancient_Shield = _attr_generator(auto(), regeneration=2)  # only found on Ancient Dreadnaught
    Morph_Shield = _attr_generator(auto(), initiative=2, shields=1, regeneration=1)
    Ion_Cannon = _attr_generator(auto(), power=1, guns=[Die.Yellow])
    Ion_Disruptor = _attr_generator(auto(), initiative=3, guns=[Die.Yellow])
    Ion_Turret = _attr_generator(auto(), power=1, guns=[Die.Yellow, Die.Yellow])
    Plasma_Cannon = _attr_generator(auto(), power=2, guns=[Die.Orange])
    Antimatter_Cannon = _attr_generator(auto(), power=4, guns=[Die.Red])
    Flux_Missile = _attr_generator(auto(), initiative=2, missiles=[Die.Yellow, Die.Yellow])
    Plasma_Missile = _attr_generator(auto(), missiles=[Die.Orange, Die.Orange])
    Antimatter_Missile = _attr_generator(auto(), missiles=[Die.Red])  # only found on Ancient Cruiser
    Interceptor_Bay = _attr_generator(auto(), power=2, hull=1, interceptorBays=2)
    # From Shadow of the Rift
    Soliton_Cannon = _attr_generator(auto(), power=3, guns=[Die.Blue])
    Rift_Cannon = _attr_generator(auto(), power=1, guns=[Die.Pink])
    Anomoly_Cannon = _attr_generator(auto(), guns=[Die.Grey])  # only found on mobile Anomalies, plannet killer gun
    Plasma_Turret = _attr_generator(auto(), power=3, guns=[Die.Orange, Die.Orange])
    Soliton_Turret = _attr_generator(auto(), power=2, initiative=-2, guns=[Die.Blue, Die.Blue])
    Rift_Turret = _attr_generator(auto(), guns=[Die.Pink, Die.Pink])
    Antimatter_Accelerator = _attr_generator(auto(), power=1, guns=[Die.Red])  # only found on Pyxis Deathmoon
    Absorption_Shield = _attr_generator(auto(), power=4, shields=1)
    Inversion_Shield = _attr_generator(auto(), power=2, shields=2)
    Transition_Drive = _attr_generator(auto(), initiative=-1, driveThrust=3)
