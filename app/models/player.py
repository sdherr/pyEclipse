from enum import StrEnum, auto

from app.models.development import Development
from app.models.sector import Sector
from app.models.ships.ship import (
    Cruiser,
    Deathmoon,
    Dreadnought,
    Interceptor,
    Monolith,
    Orbital,
    Ship,
    ShipBlueprint,
    ShipType,
    Starbase,
)
from app.models.ships.shipPart import ShipPart as SP
from app.models.technology import Technology, TechnologyType


class Species(StrEnum):
    Terran = auto()
    Planta = auto()
    Mechanema = auto()
    Eridani = auto()
    Hydran = auto()
    Enlightened = auto()
    Rho_Indi = auto()
    # from Rise of Ancients
    Descendants = auto()
    Orion = auto()
    Exiles = auto()
    Magellan = auto()
    # from Shadow of Rift
    Octantis = auto()
    Shapers = auto()
    Unity = auto()


class Color(StrEnum):
    Blue = auto()
    Green = auto()
    Red = auto()
    White = auto()
    Black = auto()
    Yellow = auto()
    Purple = auto()
    Natural = auto()
    Grey = auto()


class TechTrack:
    class Slot:
        discount: int
        vpValue: int
        tech: Technology | None

        def __init__(self, discount: int, vpValue: int):
            self.discount, self.vpValue, self.tech = discount, vpValue, None

    slots: list[Slot]
    type: TechnologyType

    def __init__(self, type: TechnologyType):
        self.type = type
        slots: list[TechTrack.Slot] = []
        for discount, vpValue in ((0, 0), (1, 0), (2, 0), (3, 1), (4, 2), (6, 3), (8, 5)):
            slots.append(TechTrack.Slot(discount, vpValue))

    def vpValue(self) -> int:
        for slot in self.slots[::-1]:
            if slot.tech is not None:
                return slot.vpValue
        raise Exception("TechTrack.vpValue: This can't happen, but things whine if it's possible to return None.")

    def next(self) -> "TechTrack.Slot | None":
        for slot in self.slots:
            if slot.tech is None:
                return slot


class Ambassador:
    player: "Player"

    def __init__(self, player: "Player"):
        self.player = player


class RepAmbSlot:
    reputationAllowed: bool
    ambassadorAllowed: bool
    ambassador: Ambassador | None = None
    reputation: int = 0

    def __init__(self, reputationAllowed: bool, ambassadorAllowed: bool):
        self.reputationAllowed, self.ambassadorAllowed = reputationAllowed, ambassadorAllowed

    def vpValue(self):
        if self.ambassador is not None:
            return 1
        return self.reputation


class RepAmbTrack:
    slots: list[RepAmbSlot]

    def __init__(self):
        self.slots = []


class PopulationTrack:
    slots = [28, 24, 21, 18, 15, 12, 10, 8, 6, 4, 3, 2]
    population = 11


class InfluenceTrack:
    slots = [30, 25, 21, 17, 13, 10, 7, 5, 3, 2, 1, 0, 0]
    disks = 13


class Player:
    color: Color
    species: Species
    money: int
    science: int
    materials: int
    mutagen: int = 0
    tradeRate: int = 3  # "x to 1"
    colonyShips: int = 3
    usedColonyships: int = 0
    blueprints: dict[ShipType, ShipBlueprint]
    technologyTracks: dict[TechnologyType, TechTrack]
    sciencePopulationTrack: PopulationTrack
    economyPopulationTrack: PopulationTrack
    materialsPopulationTrack: PopulationTrack
    influenceTrack: InfluenceTrack
    repAmbTrack: RepAmbTrack
    scienceGraveyard: int = 0
    economyGraveyard: int = 0
    materialsGraveyard: int = 0
    sectorsToExplore: int = 1
    colonyShipsOnInflunence: int = 2
    technologiesOnResearch: int = 1
    shipPartsOnUpgrade: int = 2
    shipsOnBuild: int = 2
    activationsOnMove: int = 2
    availableAmbassadors: int = 4
    discoveryVPs: int = 0
    sectors: list[Sector]
    ships: list[Ship]
    nonagressionPact: set["Player"]
    allies: set["Player"]
    developments: set[Development]
    placableShipParts: set[SP]

    def __init__(self, color: Color, species: Species, sector: Sector):
        self.color, self.species = color, species
        # Standard initialization
        self.placableShipParts = set(
            (SP.Hull, SP.Ion_Cannon, SP.Nuclear_Drive, SP.Nuclear_Source, SP.Electron_Computer)
        )
        self.blueprints = {
            ShipType.Interceptor: Interceptor(species),
            ShipType.Cruiser: Cruiser(species),
            ShipType.Dreadnought: Dreadnought(species),
        }
        self.technologyTracks = {
            TechnologyType.Grid: TechTrack(TechnologyType.Grid),
            TechnologyType.Military: TechTrack(TechnologyType.Military),
            TechnologyType.Nano: TechTrack(TechnologyType.Nano),
        }
        self.repAmbTrack = RepAmbTrack()
        for _ in range(4):
            self.repAmbTrack.slots.append(RepAmbSlot(reputationAllowed=True, ambassadorAllowed=True))

        if species != Species.Orion:  # Just so we don't have to add the line in every case.
            self.ships.append(Ship(sector, ShipType.Interceptor, self))

        if species == Species.Terran:
            self.money, self.science, self.materials = 2, 3, 3
            self.tradeRate, self.activationsOnMove = 2, 3
            self.research(Technology.Starbase, free=True)
            self.repAmbTrack.slots.append(RepAmbSlot(reputationAllowed=False, ambassadorAllowed=True))
        elif species == Species.Descendants:
            self.money, self.science, self.materials = 2, 4, 3
        elif species == Species.Orion:
            self.money, self.science, self.materials = 3, 3, 5
            self.tradeRate = 4
            self.research(Technology.Neutron_Bombs, free=True)
            self.research(Technology.Gauss_Shield, free=True)
            self.ships.append(Ship(sector, ShipType.Cruiser, self))
            self.repAmbTrack.slots.append(RepAmbSlot(reputationAllowed=True, ambassadorAllowed=False))
        elif species == Species.Hydran:
            self.money, self.science, self.materials = 2, 5, 2
            self.technologiesOnResearch = 2
            self.research(Technology.Advanced_Labs, free=True)
            self.repAmbTrack.slots[0] = RepAmbSlot(reputationAllowed=False, ambassadorAllowed=True)
        elif species == Species.Planta:
            self.money, self.science, self.materials = 4, 4, 4
            self.colonyShips, self.sectorsToExplore = 4, 2
            self.research(Technology.Starbase, free=True)
            self.repAmbTrack.slots[0] = RepAmbSlot(reputationAllowed=False, ambassadorAllowed=True)
        elif species == Species.Mechanema:
            self.money, self.science, self.materials = 3, 3, 3
            self.shipPartsOnUpgrade, self.shipsOnBuild = 3, 3
            self.research(Technology.Positron_Computer, free=True)
        elif species == Species.Eridani:
            self.money, self.science, self.materials = 26, 2, 4
            self.influenceTrack.disks = 11
            self.research(Technology.Starbase, free=True)
            self.research(Technology.Gauss_Shield, free=True)
            self.research(Technology.Fusion_Drive, free=True)
        elif species == Species.Enlightened:
            self.money, self.science, self.materials = 2, 4, 3
            self.research(Technology.Distortion_Shield, free=True)
        elif species == Species.Rho_Indi:
            self.money, self.science, self.materials = 2, 3, 3
            self.colonyShips, self.activationsOnMove, self.availableAmbassadors = 2, 4, 2
            self.research(Technology.Starbase, free=True)
            self.research(Technology.Gauss_Shield, free=True)
            self.ships.append(Ship(sector, ShipType.Interceptor, self))  # A second one
            self.repAmbTrack.slots[2] = RepAmbSlot(reputationAllowed=True, ambassadorAllowed=False)
            self.repAmbTrack.slots[3] = RepAmbSlot(reputationAllowed=True, ambassadorAllowed=False)
            self.repAmbTrack.slots.append(RepAmbSlot(reputationAllowed=True, ambassadorAllowed=False))
            self.blueprints.pop(ShipType.Dreadnought)
        elif species == Species.Exiles:
            self.money, self.science, self.materials = 3, 2, 4
            self.research(Technology.Cloaking_Device, free=True)
            self.research(Technology.Orbital, free=True)
        elif species == Species.Magellan:
            self.money, self.science, self.materials = 2, 2, 3
            self.colonyShipsOnInflunence = 1
            self.research(Technology.Fusion_Source, free=True)
        elif species == Species.Unity:
            self.money, self.science, self.materials = 8, 0, 0
            self.colonyShips = 2
            self.research(Technology.Advanced_Robotics)
            self.blueprints.pop(ShipType.Dreadnought)
            self.blueprints[ShipType.Deathmoon] = Deathmoon(self.species)
        elif species == Species.Shapers:
            self.money, self.science, self.materials = 3, 4, 2
            self.research(Technology.Soliton_Cannon)
        elif species == Species.Octantis:
            self.money, self.science, self.materials = 2, 3, 3
            self.mutagen = 4
            self.research(Technology.Fusion_Drive)

    def research(self, tech: Technology, free: bool = False, chosenType: TechnologyType = TechnologyType.Rare):
        if tech.type == TechnologyType.Rare:
            if chosenType == TechnologyType.Rare:
                raise Exception("You must choose another type for Rare Technologies.")
            tech_type = chosenType
        else:
            tech_type = tech.type

        for slot in self.technologyTracks[tech_type].slots:
            if slot.tech is None:
                break
            elif slot.tech == tech:
                raise Exception("You can't research the same Technology twice.")
        else:
            raise Exception("That Technology Track is full!")

        if not free:
            cost = max(tech.minimum_cost, tech.default_cost - slot.discount)
            if self.science < cost:
                raise Exception("You don't have enough science to research that!")
            self.science -= cost

        slot.tech = tech
        # Do the technology effects
        if tech.ship_part is not None:
            self.placableShipParts.add(tech.ship_part)
        if tech == Technology.Advanced_Robotics:
            self.influenceTrack.disks += 1
        elif tech == Technology.Nanorobots:
            self.shipsOnBuild += 1
        elif tech == Technology.Quantum_Grid:
            self.influenceTrack.disks += 2
        elif tech == Technology.Orbital:
            self.blueprints[ShipType.Orbital] = Orbital(self.species)
        elif tech == Technology.Starbase:
            self.blueprints[ShipType.Starbase] = Starbase(self.species)
        elif tech == Technology.Monolith:
            self.blueprints[ShipType.Monolith] = Monolith(self.species)
        # TODO: The others that are neither ship-part techs nor one of the above.
