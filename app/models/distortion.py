from enum import Enum, StrEnum, auto
from typing import NamedTuple


class FutureEffect(StrEnum):
    PayForLater = auto()
    SendTo = auto()


class DistortionAttributes(NamedTuple):
    value_: int
    futureEffect: FutureEffect
    vpPenalty: int
    turns: int


class Distortion(DistortionAttributes, Enum):
    To_Ship_1 = DistortionAttributes(auto(), FutureEffect.SendTo, 1, 1)
    To_Ship_2 = DistortionAttributes(auto(), FutureEffect.SendTo, 1, 2)
    To_Ships_1 = DistortionAttributes(auto(), FutureEffect.SendTo, 1, 1)
    To_Ships_2 = DistortionAttributes(auto(), FutureEffect.SendTo, 1, 2)
    To_Starbase_1 = DistortionAttributes(auto(), FutureEffect.SendTo, 2, 1)
    To_Starbase_2 = DistortionAttributes(auto(), FutureEffect.SendTo, 2, 2)
    To_Explore_1 = DistortionAttributes(auto(), FutureEffect.SendTo, 1, 2)
    To_Explore_2 = DistortionAttributes(auto(), FutureEffect.SendTo, 1, 3)
    From_Action_1 = DistortionAttributes(auto(), FutureEffect.PayForLater, 2, 1)
    From_Action_2 = DistortionAttributes(auto(), FutureEffect.PayForLater, 2, 2)
    From_Orbital_1 = DistortionAttributes(auto(), FutureEffect.PayForLater, 2, 3)
    From_Orbital_2 = DistortionAttributes(auto(), FutureEffect.PayForLater, 2, 3)
    From_Starbase_1 = DistortionAttributes(auto(), FutureEffect.PayForLater, 1, 2)
    From_Starbase_2 = DistortionAttributes(auto(), FutureEffect.PayForLater, 1, 2)
    From_Cruiser_1 = DistortionAttributes(auto(), FutureEffect.PayForLater, 2, 2)
    From_Cruiser_2 = DistortionAttributes(auto(), FutureEffect.PayForLater, 2, 3)
    From_Dreadnought_1 = DistortionAttributes(auto(), FutureEffect.PayForLater, 3, 2)
    From_Dreadnought_2 = DistortionAttributes(auto(), FutureEffect.PayForLater, 3, 3)
    From_Five_Six_Pink = DistortionAttributes(auto(), FutureEffect.PayForLater, 2, 1)
    From_Five_Seven_Pink = DistortionAttributes(auto(), FutureEffect.PayForLater, 2, 2)
    From_Five_Eight_Brown = DistortionAttributes(auto(), FutureEffect.PayForLater, 2, 3)
    From_Five_Eight_Orange = DistortionAttributes(auto(), FutureEffect.PayForLater, 2, 3)
    From_Plasma_Missile = DistortionAttributes(auto(), FutureEffect.PayForLater, 2, 3)
    From_Gluon_Computer = DistortionAttributes(auto(), FutureEffect.PayForLater, 2, 3)
    From_Positron_Computer = DistortionAttributes(auto(), FutureEffect.PayForLater, 1, 1)
    From_Tachyon_Drive = DistortionAttributes(auto(), FutureEffect.PayForLater, 1, 3)
    From_Tachyon_Source = DistortionAttributes(auto(), FutureEffect.PayForLater, 1, 2)

    @classmethod
    def init_distortions(cls) -> list["Distortion"]:
        return list(Distortion)
