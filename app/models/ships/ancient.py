from random import shuffle

from app.models.ships.ship import SP, ShipBlueprint
from app.models.world import WorldType


class AncientInterceptor(ShipBlueprint):
    """
    Ancient Interceptors are the "regular Ancients".
    """

    reputationDraws = 1
    cost = 1000  # Player can't build them
    baseInitiative = 1
    basePower = 1000  # High enough to never be an issue
    initialBlueprint = {
        ShipBlueprint.LM: SP.Ion_Cannon,
        ShipBlueprint.LD: SP.Hull,
        ShipBlueprint.RM: SP.Ion_Cannon,
        ShipBlueprint.RD: SP.Electron_Computer,
        ShipBlueprint.MD: SP.Nuclear_Drive,
    }
    overlayBlueprint = {}


class AncientCruiser(ShipBlueprint):
    """
    Ancient Cruisers are the "Ancient Homeworld ships".
    """

    reputationDraws = 2
    cost = 1000  # Player can't build them
    vpValue = 1
    basePower = 1000  # High enough to never be an issue
    canHaveDrive = False
    styles = [1, 2, 3, 4, 5, 6, 7, 8]

    def __init__(self):
        self.overlayBlueprint = {}
        # Choose a random style and pop it so it can't be re-created.
        shuffle(self.styles)
        self.style = self.styles.pop()

        if self.style == 1:
            self.initialBlueprint = {
                self.LU: SP.Antimatter_Cannon,
                self.LM: SP.Axion_Computer,
                self.LD: SP.Improved_Hull,
                self.MU: SP.Improved_Hull,
            }
        elif self.style == 2:
            self.initialBlueprint = {
                self.LU: SP.Ion_Turret,
                self.LM: SP.Ion_Turret,
                self.LD: SP.Improved_Hull,
                self.MU: SP.Electron_Computer,
                self.MM: SP.Gauss_Shield,
            }
        elif self.style == 3:
            self.baseInitiative = 3
            self.initialBlueprint = {
                self.LU: SP.Ion_Turret,
                self.LM: SP.Ion_Cannon,
                self.LD: SP.Positron_Computer,
                self.MU: SP.Improved_Hull,
            }
        elif self.style == 4:
            self.initialBlueprint = {
                self.LU: SP.Plasma_Missile,
                self.LM: SP.Ion_Turret,
                self.LD: SP.Hull,
                self.MU: SP.Positron_Computer,
            }
        elif self.style == 5:
            self.baseInitiative = 1
            self.hasDistortionShield: True
            self.initialBlueprint = {
                self.LU: SP.Antimatter_Missile,
                self.LM: SP.Plasma_Cannon,
                self.LD: SP.Positron_Computer,
                self.MU: SP.Hull,
            }
        elif self.style == 6:
            self.baseInitiative = 1
            self.hasPointDefence = True
            self.initialBlueprint = {
                self.LU: SP.Ion_Turret,
                self.LM: SP.Positron_Computer,
                self.LD: SP.Improved_Hull,
                self.MU: SP.Improved_Hull,
            }
        elif self.style == 7:
            self.baseInitiative = 3
            self.initialBlueprint = {
                self.LU: SP.Improved_Hull,
                self.LM: SP.Plasma_Cannon,
                self.LD: SP.Plasma_Cannon,
                self.MU: SP.Electron_Computer,
            }
        else:  # 8
            self.initialBlueprint = {
                self.LU: SP.Improved_Hull,
                self.LM: SP.Ion_Turret,
                self.LD: SP.Ion_Cannon,
                self.MU: SP.Electron_Computer,
                self.MM: SP.Flux_Shield,
            }


class AncientDreadnought(ShipBlueprint):
    """
    Ancient Dreadnoughts are the "Galactic Center Defence System" ships, including the GCDS itself.
    """

    reputationDraws = 3
    cost = 1000  # Player can't build them
    basePower = 1000  # High enough to never be an issue
    canHaveDrive = False
    styles = ["GCDS", "A", "B"]

    def __init__(self, style: str = None):
        if not style:
            shuffle(self.styles)
            style = self.styles.pop()

        self.style = style
        if style == "GCDS":
            self.vpValue = 0
            self.initialBlueprint = {
                self.LU: SP.Improved_Hull,
                self.LM: SP.Improved_Hull,
                self.LD: SP.Hull,
                self.MU: SP.Plasma_Cannon,
                self.MM: SP.Plasma_Cannon,
                self.MD: SP.Ancient_Shield,
                self.LU: SP.Positron_Computer,
            }
        elif style == "A":
            self.vpValue = 1
            self.baseInitiative = 2  # positron computer adds one
            self.initialBlueprint = {
                self.LU: SP.Improved_Hull,
                self.LM: SP.Hull,
                self.LD: SP.Flux_Missile,
                self.MU: SP.Flux_Missile,
                self.MM: SP.Positron_Computer,
                self.MD: SP.Antimatter_Cannon,
            }
        else:  # B
            self.vpValue = 1
            self.baseInitiative = -1  # two flux missiles and a positron computer would be 5, need 4
            self.initialBlueprint = {
                self.LU: SP.Improved_Hull,
                self.LM: SP.Improved_Hull,
                self.LD: SP.Improved_Hull,
                self.MU: SP.Hull,
                self.MM: SP.Ion_Turret,
                self.MD: SP.Ion_Turret,
                self.LU: SP.Electron_Computer,
            }


class Anomaly(ShipBlueprint):
    """
    Anomalies are the planet-destroying ships.
    """

    reputationDraws = 3
    cost = 1000  # Player can't build them
    vpValue = 1
    basePower = 1000  # High enough to never be an issue
    styles = [1, 2, 3, 4, 5, 6]
    isMobile: bool
    color: WorldType

    def __init__(self, isMobile: bool):
        self.overlayBlueprint = {}
        self.isMobile = isMobile
        # Choose a random style and pop it so it can't be re-created.
        shuffle(self.styles)
        self.style = self.styles.pop()

        self.initialBlueprint = {
            self.LU: SP.Improved_Hull,
            self.LM: SP.Improved_Hull,
            self.LD: SP.Improved_Hull,
            self.MU: SP.Rift_Turret,
            self.MM: SP.Rift_Cannon,
        }

        if isMobile:
            self.initialBlueprint[self.MD] = SP.Nuclear_Drive
            self.initialBlueprint[self.RU] = SP.Anomoly_Cannon
            self.initialBlueprint[self.RM] = SP.Improved_Hull

        if self.style in (1, 2):
            self.color = WorldType.PINK
            self.baseInitiative = -1  # negate nuclear drive
            self.initialBlueprint[self.RD] = SP.Rift_Cannon
        elif self.style in (3, 4):
            self.color = WorldType.ORANGE
            self.initialBlueprint[self.RD] = SP.Improved_Hull
        else:  # 5 or 6
            self.color = WorldType.BROWN
            self.baseInitiative = 1
            self.initialBlueprint[self.MM] = SP.Improved_Hull  # replace rift cannon with hull
            self.initialBlueprint[self.RD] = SP.Improved_Hull

    @property
    def canHaveDrive(self):
        return self.isMobile
