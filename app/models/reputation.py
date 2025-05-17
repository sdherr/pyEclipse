from enum import StrEnum, auto

from config import config


class ReputationTileType(StrEnum):
    Points = auto()
    Re_Roll = auto()
    Resource_Gain = auto()
    Double_Action = auto()
    Priority_Action = auto()
    Advanced_Reaction = auto()
    Bonus_Targeting = auto()
    Bonus_Move = auto()
    Bonus_Upgrade = auto()
    Bonus_Build = auto()


class ReputationTile:
    type: ReputationTileType
    vpValue: int

    def __init__(self, type: ReputationTileType, vpValue: int):
        self.type, self.vpValue = type, vpValue

    @classmethod
    def init_reputation(cls) -> list["ReputationTile"]:
        ret = []
        many_players = config.number_of_players > 6
        for _ in range(6 if many_players else 4):
            ret.append(ReputationTile(ReputationTileType.Points, 4))
        for _ in range(10 if many_players else 7):
            ret.append(ReputationTile(ReputationTileType.Points, 3))
        for _ in range(11 if many_players else 9):
            ret.append(ReputationTile(ReputationTileType.Points, 2))
        for _ in range(14 if many_players else 12):
            ret.append(ReputationTile(ReputationTileType.Points, 1))

        if config.rota_special_reputation:
            ret.add(ReputationTile(ReputationTileType.Advanced_Reaction, 0))
            ret.add(ReputationTile(ReputationTileType.Bonus_Build, 0))
            ret.add(ReputationTile(ReputationTileType.Bonus_Move, 0))
            ret.add(ReputationTile(ReputationTileType.Bonus_Targeting, 0))
            ret.add(ReputationTile(ReputationTileType.Bonus_Upgrade, 0))
            ret.add(ReputationTile(ReputationTileType.Double_Action, 0))
            ret.add(ReputationTile(ReputationTileType.Priority_Action, 0))
            ret.add(ReputationTile(ReputationTileType.Re_Roll, 0))
            ret.add(ReputationTile(ReputationTileType.Resource_Gain, 0))

        return ret
