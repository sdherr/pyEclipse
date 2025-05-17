from collections import defaultdict
from random import shuffle

from config import config
from development import Development
from discovery import DiscoveryTile
from distortion import Distortion
from evolution import Evolution
from reputation import ReputationTile
from sector import Sector, Sectors
from technology import Technology


class Table:
    map: dict[int, dict[int, Sector | None]]  # 2-d dict using our q and r Axial coordinates
    warpNexus = Sectors.SDSS_1133
    galacticCenter = Sectors.Galactic_Center

    unplacedRing1: list[Sector]
    unplacedRing2: list[Sector]
    unplacedRing3: list[Sector]
    placedSectors: list[Sector] = []

    reputationBag: list[ReputationTile]
    discoveryBag: list[DiscoveryTile]
    technologyBag: list[Technology]
    developmentBag: list[Development]
    evolutionBag: list[Evolution] = []
    distortionBag: list[Distortion] = []

    def __init__(self):
        self.map = defaultdict(defaultdict(None))

        self.discoveryBag = DiscoveryTile.init_discoveries()
        shuffle(self.discoveryBag)

        self.reputationBag = ReputationTile.init_reputation()
        shuffle(self.reputationBag)

        self.technologyBag = Technology.init_technologies()
        shuffle(self.technologyBag)

        self.developmentBag = Development.init_developments()
        shuffle(self.developmentBag)
        # Max 1 + number of players
        self.developmentBag = self.developmentBag[0 : config.number_of_players + 1]

        if config.sotr_evolution:
            self.evolutionBag = Evolution.init_evolution()
            shuffle(self.evolutionBag)

        if config.sotr_distortions:
            self.discoveryBag = Distortion.init_distortions()
            shuffle(self.distortionBag)

        self.unplacedRing1, self.unplacedRing2, self.unplacedRing3 = Sectors.init_sectors()
        shuffle(self.unplacedRing1)
        shuffle(self.unplacedRing2)
        shuffle(self.unplacedRing3)
        # TODO: look up how many ring3 to keep based on number of players
