from abc import ABC
from enum import StrEnum, auto

from sector import Sector

from app.models.player import Player
from app.models.player import Species as S
from app.models.ships.shipPart import ShipPart as SP


class ShipType(StrEnum):
    Interceptor = auto()
    Cruiser = auto()
    Dreadnought = auto()
    Starbase = auto()
    Orbital = auto()
    Monolith = auto()
    Deathmoon = auto()
    AncientInterceptor = auto()
    AncientCruiser = auto()
    AncientDreadnought = auto()
    Anomaly = auto()


class Ship:
    type: ShipType
    location: Sector
    owner: Player
    damage: int = 0

    def __init__(self, location: Sector, type: ShipType, owner: Player):
        self.location, self.type, self.owner = location, type, owner
        location.ships.append(self)


class ShipBlueprint(ABC):
    reputationDraws: int
    cost: int
    initialBlueprint: dict[int, SP]
    overlayBlueprint: dict[int, SP]
    baseInitiative: int = 0
    basePower: int = 0
    baseComputers: int = 0
    baseShields: int = 0
    baseHull: int = 1
    canHaveDrive: bool = True
    hasDistortionShield: bool = False
    hasPointDefence: bool = False
    vpValue: int = 0
    # Some constants to use to define blueprint positions
    LU = 1  # Left Up
    LM = 2
    LD = 3
    MU = 4
    MM = 5
    MD = 6
    RU = 7
    RM = 8
    RD = 9


class Interceptor(ShipBlueprint):
    reputationDraws = 1

    def __init__(self, species: S):
        initiative_map: dict[S, int] = {S.Orion: 3, S.Planta: 0, S.Rho_Indi: 3, S.Shapers: 1}
        self.baseInitiative: int = initiative_map.get(species, 2)

        power_map = {S.Orion: 1, S.Planta: 2, S.Shapers: 5}
        self.basePower: int = power_map.get(species, 0)

        self.baseComputers = 1 if species == S.Planta else 0
        self.baseShields = 1 if species == S.Rho_Indi else 0

        cost_map = {S.Mechanema: 2, S.Rho_Indi: 4, S.Unity: 2}
        self.cost: int = cost_map.get(species, 3)

        left_part = {
            S.Orion: SP.Gauss_Shield,
            S.Planta: SP.Non_Existent,
            S.Shapers: SP.Electron_Computer,
        }
        down_part = SP.Non_Existent if species == S.Shapers else SP.Nuclear_Source
        self.initialBlueprint = {
            self.LM: left_part.get(species, SP.Empty),
            self.MU: SP.Ion_Cannon,
            self.MD: down_part,
            self.RM: SP.Nuclear_Drive,
        }
        self.overlayBlueprint = {}


class Cruiser(ShipBlueprint):
    reputationDraws = 2

    def __init__(self, species: S):
        initiative_map = {S.Orion: 2, S.Planta: 0, S.Rho_Indi: 2, S.Shapers: 0}
        self.baseInitiative: int = initiative_map.get(species, 1)

        power_map = {S.Orion: 2, S.Planta: 2, S.Shapers: 5}
        self.basePower: int = power_map.get(species, 0)

        self.baseComputers = 1 if species == S.Planta else 0
        self.baseShields = 1 if species == S.Rho_Indi else 0

        cost_map = {S.Mechanema: 4, S.Rho_Indi: 6, S.Unity: 4}
        self.cost: int = cost_map.get(species, 5)

        ld_part_map = {
            S.Orion: SP.Gauss_Shield,
            S.Planta: SP.Non_Existent,
            S.Shapers: SP.Non_Existent,
        }
        lu_part = SP.Empty if species == S.Shapers else SP.Hull
        md_part = SP.Hull if species == S.Shapers else SP.Nuclear_Source
        self.initialBlueprint = {
            self.LM: lu_part,
            self.LD: ld_part_map.get(species, SP.Empty),
            self.MU: SP.Ion_Cannon,
            self.MD: md_part,
            self.RM: SP.Electron_Computer,
            self.RD: SP.Nuclear_Drive,
        }
        self.overlayBlueprint = {}


class Dreadnought(ShipBlueprint):
    reputationDraws = 3

    def __init__(self, species: S):
        if species == S.Rho_Indi:
            return  # Cannot build. TODO: something better?

        self.baseInitiative = 1 if species == S.Orion else 0

        power_map = {S.Orion: 3, S.Planta: 2, S.Eridani: 1, S.Shapers: 5}
        self.basePower = power_map.get(species, 0)

        self.baseComputers = 1 if species == S.Planta else 0
        self.baseShields = 0

        self.cost = 7 if species == S.Mechanema else 8

        self.initialBlueprint = {
            self.LU: SP.Ion_Cannon,
            self.LM: SP.Hull,
            self.LD: SP.Empty,
            self.MU: SP.Hull,
            self.MD: SP.Nuclear_Drive,
            self.RU: SP.Ion_Cannon,
            self.RM: SP.Electron_Computer,
            self.RD: SP.Nuclear_Drive,
        }
        if species == S.Orion:
            self.initialBlueprint[self.LD] = SP.Gauss_Shield
        elif species == S.Planta:
            self.initialBlueprint[self.RM] = SP.Empty
            self.initialBlueprint[self.MU] = SP.Nuclear_Source
            self.initialBlueprint[self.MD] = SP.Non_Existent
            self.initialBlueprint[self.LD] = SP.Hull
        elif species == S.Shapers:
            self.initialBlueprint[self.RU] = SP.Soliton_Cannon
            self.initialBlueprint[self.LU] = SP.Non_Existent
            self.initialBlueprint[self.LM] = SP.Ion_Cannon
        self.overlayBlueprint = {}


class Starbase(ShipBlueprint):
    reputationDraws = 1
    canHaveDrive = False

    def __init__(self, species: S):
        initiative_map = {S.Orion: 5, S.Planta: 2, S.Shapers: 3}
        self.baseInitiative = initiative_map.get(species, 4)

        self.basePower = 5 if species in (S.Planta, S.Shapers) else 3
        self.baseComputers = 1 if species == S.Planta else 0
        self.baseShields = 1 if species == S.Rho_Indi else 0

        cost_map = {S.Mechanema: 2, S.Rho_Indi: 4}
        self.cost = cost_map.get(species, 3)

        dp_map = {S.Orion: SP.Gauss_Shield, S.Planta: SP.Non_Existent, S.Shapers: SP.Non_Existent}
        dp = dp_map.get(species, SP.Empty)
        up = SP.Soliton_Cannon if species == S.Shapers else SP.Ion_Cannon
        self.initialBlueprint = {
            self.LM: SP.Hull,
            self.MU: up,
            self.MM: SP.Hull,
            self.MD: dp,
            self.RM: SP.Electron_Computer,
        }
        self.overlayBlueprint = {}


class Deathmoon(ShipBlueprint):
    baseHull = 2
    reputationDraws = 3
    vpValue = 4
    cost = 1000  # cannot be directly built

    def __init__(self, species: S):
        if species != S.Unity:
            return  # Cannot build. TODO: something better?

        self.initialBlueprint = {
            self.LU: SP.Electron_Computer,
            self.LM: SP.Nuclear_Source,
            self.LD: SP.Nuclear_Drive,
            self.MU: SP.Antimatter_Accelerator,
            self.MM: SP.Hull,
            self.MD: SP.Hull,
        }
        self.overlayBlueprint = {}


class Monolith(ShipBlueprint):
    # Not a ship, but buildable, so close enough.
    reputationDraws = 0
    initialBlueprint = {}
    overlayBlueprint = {}

    def __init__(self, species: S):
        self.cost = 8 if species == S.Mechanema else 10


class Orbital(ShipBlueprint):
    # Not really a ship except for exiles, but buildable, so close enough.
    canHaveDrive = False

    def __init__(self, species: S):
        self.overlayBlueprint = {}
        if species != S.Exiles:
            self.reputationDraws = 0
            self.cost = 4 if species == S.Mechanema else 5
            self.initialBlueprint = {
                self.MU: SP.Non_Existent,
                self.LD: SP.Non_Existent,
                self.RD: SP.Non_Existent,
            }
            return

        self.reputationDraws = 1
        self.basePower = 4
        self.cost = 6
        self.initialBlueprint = {self.MU: SP.Ion_Turret, self.LD: SP.Hull, self.RD: SP.Hull}
