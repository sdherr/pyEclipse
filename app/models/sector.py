from enum import Enum

from app.models.discovery import DiscoveryTile
from app.models.player import Player
from app.models.ships.ancient import AncientCruiser, AncientDreadnought, AncientInterceptor, Anomaly
from app.models.ships.ship import Ship
from app.models.table import Table
from app.models.world import World, WorldType


class Sector:
    id: int
    vpValue: int
    wormholes: str
    discovery: DiscoveryTile | None = None
    artifacts: int = 0  # Can potentially have 2 because of Orbital Discovery
    worlds: list[World]
    ships: list[Ship]
    controllingPlaoyer: Player
    centerWormhole: bool = False
    deepWarp: bool = False
    monolith: bool = False
    adjacentSectors: set["Sector"]
    connectedSectors: set["Sector"]
    halfConnectedSectors: set["Sector"]
    nebula: dict[int, "Sector"]  # Map of which wormhole connects to which subsector
    # Axial Coordinates: https://www.redblobgames.com/grids/hexagons/#coordinates-axial
    q: int
    r: int

    def __init__(
        self,
        id: int,
        vpValue: int,
        wormholes: str,
        discovery: bool,
        artifact: bool,
        brown: int,
        advBrown: int,
        pink: int,
        advPink: int,
        orange: int,
        advOrange: int,
        white: int,
        advWhite: int,
        ancientInterceptors: int,
    ):
        self.id = id
        self.vpValue = vpValue
        self.wormholes = wormholes
        if discovery:
            self.discovery = DiscoveryTile.Accelerated_Evolution  # TODO: random one
        self.artifacts = int(artifact)
        self.worlds = []
        for type, reg, adv in (
            (WorldType.BROWN, brown, advBrown),
            (WorldType.PINK, pink, advPink),
            (WorldType.ORANGE, orange, advOrange),
            (WorldType.WHITE, white, advWhite),
        ):
            if reg or adv:
                self.worlds.append(World(type, reg, adv))

        self.ships = []
        if id == 1:  # Galactic Center
            self.ships.append(AncientDreadnought())
        for _ in range(ancientInterceptors):
            self.ships.append(AncientInterceptor())
        # Ancient Homeworlds
        if id >= 271 and id <= 274:
            self.ships.add(AncientCruiser())

        self.centerWormhole = id in (281, 381, 382)

        # Exile's Homeworld
        if id == 234:
            self.worlds.add(WorldType.ORBITAL, 1, 0)

        # TODO: Something else for Hive sectors? 212 and 319

        if id == 295 or id == 395:  # Nebulas are basically three mini sectors in one. Init the mini sectors.
            self.init_nebula()

        # Deep Warp Sectors
        self.deepWarp = id in (189, 289, 389)

        # Warp Nexus
        if id == 989:
            self.ships.append(Anomaly(False))  # TODO: allow choice about mobility
            self.ships.append(Anomaly(False))
            self.ships.append(Anomaly(False))
            self.ships.append(Anomaly(False))

    def place(self, q: int, r: int, rotation: int):
        """
        Q and R are our axial coordinate representation.
        https://www.redblobgames.com/grids/hexagons/#coordinates-axial

        rotation represents how the wormholes need to rotate, 0 = None, -1 = 1 to the left, 2 = 2 to the right
        """
        self.q, self.r = q, r
        while rotation < 0:  # normalize to only rotating one direction
            rotation += 6

        while rotation > 0:
            self.wormholes = self.wormholes[5] + self.wormholes[0:5]
            if self.nebula:
                self.nebula = {
                    0: self.nebula[5],
                    1: self.nebula[0],
                    2: self.nebula[1],
                    3: self.nebula[2],
                    4: self.nebula[3],
                    5: self.nebula[4],
                }
            rotation -= 1

    def connect_to_center_wormholes(self):
        for sector in Table.placedSectors:
            if sector.centerWormhole:
                self.connectedSectors.add(sector)
                sector.connectedSectors.add(self)

    def calculate_connections(self):
        if self.deepWarp:
            self.connectedSectors.add(Table.deepWarpNexus)
            Table.deepWarpNexus.connectedSectors.add(self)

        if self.centerWormhole:
            self.connect_to_center_wormholes()

        q, r = self.q, self.r
        left = Table.map[q - 1][r]
        leftDown = Table.map[q - 1][r + 1]
        leftUp = Table.map[q][r - 1]
        rightDown = Table.map[q][r + 1]
        rightUp = Table.map[q + 1][r - 1]
        right = Table.map[q + 1][r]
        for neighbor, my_idx in ((rightUp, 0), (right, 1), (rightDown, 2), (leftDown, 3), (left, 4), (leftUp, 5)):
            if neighbor is not None:
                neighbor_idx = my_idx + 3  # whichever side I'm connecting on, he's connecting in the opposite direction
                if neighbor_idx > 5:
                    neighbor_idx -= 6  # normalize

                # If one of us is a nebula we want to connect to the subsector
                me = self
                if self.nebula:
                    me = self.nebula[my_idx]
                if neighbor.nebula:
                    neighbor = neighbor.nebula[neighbor_idx]

                # finally connect them
                if me.wormholes[my_idx] == "1" and neighbor.wormholes[neighbor_idx] == "1":
                    me.connectedSectors.add(neighbor)
                    neighbor.connectedSectors.add(me)
                elif me.wormholes[my_idx] == "0" and neighbor.wormholes[neighbor_idx] == "0":
                    me.adjacentSectors.add(neighbor)
                    neighbor.adjacentSectors.add(me)
                else:  # One is and one aint
                    me.halfConnectedSectors.add(neighbor)
                    neighbor.halfConnectedSectors.add(me)

    def init_nebula(self):
        """
        Nebulas are basically three mini sectors squished into one. Init those mini sectors, and init a mapping of which
        "outer" wormhole they connect to. The actual "outer" sector will never connect to anything.
        """
        if self.id == 295:
            a, b, c = Sectors._Nebula_Sub_A, Sectors._Nebula_Sub_B, Sectors._Nebula_Sub_E
        else:
            a, b, c = Sectors._Nebula_Sub_C, Sectors._Nebula_Sub_D, Sectors._Nebula_Sub_F
        a.connectedSectors.update((b, c))
        b.connectedSectors.update((a, c))
        c.connectedSectors.update((a, b))
        self.nebula = {0: a, 1: c, 2: c, 3: b, 4: b, 5: a}

    def add_warp_portal_development(self):
        self.centerWormhole = True
        self.vpValue += 1
        self.connect_to_center_wormholes()

    def add_warp_portal_discovery(self):
        self.centerWormhole = True
        self.vpValue += 2
        self.connect_to_center_wormholes()

    def add_shell_world(self):
        self.vpValue += 5
        self.worlds.append(World(WorldType.PINK, 1, 0))

    def add_orbital_discovery(self):
        self.artifacts += 1
        self.add_orbital()

    def add_orbital(self):
        self.worlds.append(World(WorldType.ORBITAL, 1, 0))

    def add_monolith(self):
        self.monolith = True


class Sectors(Sector, Enum):
    Galactic_Center = 1, 4, "111111", True, True, 1, 1, 1, 1, 0, 0, 2, 0, 0
    Gastor = 101, 2, "011111", True, False, 1, 1, 0, 0, 1, 0, 0, 0, 1
    Pollux = 102, 3, "101101", False, True, 0, 0, 1, 1, 0, 0, 0, 0, 0
    Beta_Lenois = 103, 2, "111011", False, False, 0, 0, 0, 0, 0, 1, 1, 0, 0
    Arcturus = 104, 2, "110110", True, False, 0, 0, 1, 1, 1, 1, 0, 0, 2
    Zeta_Herculis = 105, 3, "110111", True, True, 0, 1, 1, 0, 1, 0, 0, 0, 1
    Capella = 106, 2, "111100", False, False, 1, 0, 1, 0, 0, 0, 0, 0, 0
    Aldebaran = 107, 2, "111101", False, False, 0, 1, 0, 1, 1, 0, 0, 0, 0
    Mu_Cassiopiae = 108, 2, "110110", True, False, 0, 0, 1, 0, 0, 1, 1, 0, 1
    Alpha_Centauri = 201, 1, "010101", False, False, 1, 0, 0, 0, 1, 0, 0, 0, 0
    Fomalhaut = 202, 1, "010101", False, False, 0, 0, 1, 1, 0, 0, 0, 0, 0
    Chi_Draconis = 203, 1, "110101", True, False, 1, 0, 1, 0, 1, 0, 0, 0, 2
    Vega = 204, 2, "110101", True, True, 0, 1, 0, 0, 0, 1, 1, 0, 1
    Mu_Herculis = 205, 1, "001110", False, False, 0, 0, 0, 1, 1, 1, 0, 0, 0
    Epsilon_Indi = 206, 1, "011101", True, False, 1, 0, 0, 0, 0, 0, 0, 0, 0
    Zeta_Reticuli = 207, 1, "110100", True, False, 0, 0, 0, 0, 0, 0, 0, 0, 0
    Iota_Persei = 208, 1, "101101", True, False, 0, 0, 0, 0, 0, 0, 0, 0, 0
    Delta_Eridani = 209, 1, "110101", False, False, 0, 0, 1, 0, 0, 1, 0, 0, 0
    Psi_Capricorni = 210, 1, "100101", False, False, 1, 0, 0, 0, 1, 0, 0, 0, 0
    Beta_Aquilae = 211, 2, "111100", True, True, 0, 1, 0, 0, 1, 0, 1, 0, 1
    Procyon = 221, 3, "110110", False, True, 1, 0, 1, 1, 1, 1, 0, 0, 0
    Epsilon_Eridani = 222, 3, "110110", False, True, 0, 0, 1, 1, 1, 1, 0, 0, 0
    Altair = 223, 3, "110110", False, True, 1, 0, 1, 1, 1, 1, 0, 0, 0
    Beta_Hydri = 224, 3, "110110", False, True, 0, 1, 1, 1, 1, 0, 0, 0, 0
    Eta_Cassiopeiae = 225, 3, "110110", False, True, 1, 0, 1, 1, 1, 1, 0, 0, 0
    S1_Cygni = 226, 3, "110110", False, True, 1, 0, 1, 0, 1, 0, 0, 0, 0
    Sirius = 227, 3, "110110", False, True, 1, 0, 1, 1, 1, 1, 0, 0, 0
    Sigma_Draconis = 228, 3, "110110", False, True, 0, 1, 1, 0, 1, 0, 0, 0, 0
    Tau_Ceti = 229, 3, "110110", False, True, 1, 0, 1, 1, 1, 1, 0, 0, 0
    Lambda_Aurigae = 230, 3, "110110", False, True, 0, 1, 1, 0, 1, 1, 0, 0, 0
    Delta_Pavonis = 231, 3, "110110", False, True, 1, 0, 1, 1, 1, 1, 0, 0, 0
    Rigel = 232, 3, "110110", False, True, 1, 1, 1, 0, 0, 1, 0, 0, 0
    Zeta_Draconis = 301, 2, "101100", True, True, 0, 1, 1, 0, 1, 0, 0, 0, 2
    Gamma_Serpentis = 302, 2, "100110", True, True, 1, 0, 0, 0, 0, 1, 0, 0, 1
    Eta_Cephei = 303, 2, "000101", True, True, 0, 0, 0, 0, 0, 0, 1, 0, 1
    Theta_Pegasi = 304, 1, "100100", False, False, 1, 0, 0, 0, 0, 1, 0, 0, 0
    Lambda_Serpentis = 305, 1, "110100", True, False, 1, 0, 1, 0, 0, 0, 0, 0, 1
    Beta_Centauri = 306, 1, "010100", False, False, 1, 0, 0, 0, 1, 0, 0, 0, 0
    Sigma_Sagittarii = 307, 1, "101100", False, False, 0, 0, 0, 1, 1, 0, 0, 0, 0
    Kappa_Scorpii = 308, 1, "001101", False, False, 0, 1, 1, 0, 0, 0, 0, 0, 0
    Phi_Piscium = 309, 1, "100101", False, False, 0, 0, 0, 1, 1, 0, 0, 0, 0
    Nu_Phoenicis = 310, 1, "100100", False, False, 1, 0, 1, 0, 0, 0, 0, 0, 0
    Canopus = 311, 1, "101100", True, False, 1, 0, 0, 0, 0, 0, 0, 0, 0
    Antares = 312, 1, "110100", True, False, 1, 0, 0, 0, 0, 0, 0, 0, 0
    Alpha_Ursae_Minoris = 313, 1, "100100", True, False, 0, 0, 0, 0, 0, 0, 1, 0, 0
    Spica = 314, 1, "001110", True, False, 0, 0, 0, 0, 0, 0, 1, 0, 0
    Epsilon_Aurigae = 315, 1, "100101", True, False, 0, 0, 0, 0, 0, 0, 0, 0, 0
    Iota_Carinae = 316, 1, "110100", True, False, 0, 0, 0, 0, 0, 0, 0, 0, 0
    Beta_Crucis = 317, 1, "000110", False, False, 0, 0, 0, 0, 1, 1, 0, 0, 0
    Gamma_Velorum = 318, 1, "001100", False, False, 0, 1, 0, 0, 0, 0, 1, 0, 0
    # Rise of the Ancients
    Lambda_Fornacis = 212, 2, "111111", True, False, 1, 0, 0, 1, 1, 0, 0, 0, 3
    Iota_Bootis = 213, 1, "110101", False, False, 1, 0, 1, 0, 0, 0, 0, 0, 0
    Ursae_Majois_47 = 233, 3, "110110", False, True, 1, 0, 1, 1, 1, 1, 0, 0, 0
    Eta_Geminorum = 234, 3, "110110", False, True, 1, 1, 0, 0, 0, 1, 0, 0, 0
    Mu_Arae = 235, 3, "110110", False, True, 1, 0, 1, 1, 1, 1, 0, 0, 0
    Rho_Indi = 236, 0, "110110", False, True, 1, 0, 0, 1, 1, 1, 0, 0, 0
    Cancri_55 = 237, 3, "110110", False, True, 1, 0, 1, 1, 1, 1, 0, 0, 0
    Beta_Lyrae = 238, 3, "110110", False, True, 1, 1, 1, 1, 1, 1, 0, 0, 0
    Omega_Fornacis = 271, 3, "110110", True, True, 0, 1, 1, 0, 1, 0, 0, 0, 0
    Sigma_Hydrae = 272, 3, "110110", True, True, 1, 0, 0, 1, 1, 0, 0, 0, 0
    Theta_Ophiuchi = 273, 3, "110110", True, True, 1, 1, 0, 0, 1, 0, 0, 0, 0
    Alpha_Lyncis = 274, 3, "110110", True, True, 0, 0, 1, 1, 1, 0, 0, 0, 0
    Delta_Corvi = 281, 2, "101101", True, False, 0, 0, 0, 0, 1, 0, 0, 0, 0
    Upsilon_Hydrae = 319, 2, "111111", True, False, 1, 1, 1, 0, 0, 1, 0, 0, 3
    Nu_Ophiuchi = 320, 1, "001110", True, False, 0, 0, 1, 0, 1, 0, 0, 0, 1
    Beta_Delphini = 321, 1, "100101", False, False, 0, 0, 0, 0, 1, 1, 0, 0, 0
    Lambda_Tauri = 322, 1, "110100", False, False, 0, 0, 1, 1, 0, 0, 0, 0, 0
    Zeta_Andromedae = 323, 1, "110101", True, False, 0, 0, 0, 0, 0, 0, 0, 0, 0
    Epsilon_Carinae = 324, 2, "101101", False, True, 0, 0, 0, 0, 0, 0, 1, 0, 0
    Delta_Sextantis = 381, 2, "100110", True, False, 0, 0, 1, 0, 0, 0, 0, 0, 0
    Zeta_Chamaeleontis = 382, 2, "101100", True, False, 1, 0, 0, 0, 0, 0, 0, 0, 0
    # Nebula
    NGC_5189 = 295, 0, "111111", False, False, 0, 0, 0, 0, 0, 0, 0, 0, 0
    NGC_1952 = 395, 0, "111111", False, False, 0, 0, 0, 0, 0, 0, 0, 0, 0
    _Nebula_Sub_A = -1, 0, "111111", True, False, 0, 0, 0, 0, 0, 0, 0, 0, 0
    _Nebula_Sub_B = -2, 0, "111111", True, False, 0, 0, 0, 0, 0, 0, 0, 0, 0
    _Nebula_Sub_C = -3, 0, "111111", True, False, 0, 0, 0, 0, 0, 0, 0, 0, 0
    _Nebula_Sub_D = -4, 0, "111111", True, False, 0, 0, 0, 0, 0, 0, 0, 0, 0
    _Nebula_Sub_E = -5, 0, "111111", False, False, 0, 0, 0, 0, 0, 0, 0, 0, 1
    _Nebula_Sub_F = -6, 0, "111111", False, False, 0, 0, 0, 0, 0, 0, 0, 0, 1
    # Shadow of the Rift
    Alpha_Lacertae = 109, 4, "011111", True, False, 0, 0, 0, 0, 1, 0, 0, 0, 2
    Gamma_Bootis = 110, 2, "101110", True, False, 0, 0, 0, 0, 0, 1, 0, 1, 0
    Alpha_Scuti = 189, 2, "110110", False, False, 1, 0, 0, 0, 1, 0, 0, 1, 0
    Beta_Monocerotis = 214, 1, "111011", True, False, 0, 1, 1, 0, 0, 0, 0, 1, 1
    Theta_Octantis = 241, 3, "110110", False, True, 1, 0, 0, 1, 1, 1, 0, 0, 0
    Kappa_Pyxidis = 242, 3, "110110", False, True, 0, 0, 0, 0, 0, 0, 1, 1, 0
    Nu_Octantis = 243, 3, "110110", False, True, 1, 0, 0, 1, 1, 1, 0, 0, 0
    Zeta_Doradus = 244, 3, "110110", False, True, 1, 0, 0, 1, 1, 1, 0, 0, 0
    Delta_Scuti = 289, 1, "010101", False, False, 1, 0, 1, 0, 0, 0, 0, 1, 0
    Epsilon_Scuti = 389, 1, "010100", False, False, 0, 0, 1, 0, 0, 1, 0, 1, 0
    SDSS_1133 = 989, 3, "000000", False, True, 0, 1, 0, 1, 0, 1, 1, 1, 0
