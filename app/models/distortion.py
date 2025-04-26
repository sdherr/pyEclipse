from enum import Enum, StrEnum, auto
from typing import NamedTuple


class FutureEffect(StrEnum):
    PayForLater = auto()
    SendTo = auto()


class DistortionAttributes(NamedTuple):
    value_: int
    futureEffect: FutureEffect
    vpPenalty: int


class DistortionType(DistortionAttributes, Enum):
    To_Ship = DistortionAttributes(auto(), FutureEffect.SendTo, 1)
    To_Ships = DistortionAttributes(auto(), FutureEffect.SendTo, 1)
    To_Starbase = DistortionAttributes(auto(), FutureEffect.SendTo, 2)
    To_Explore = DistortionAttributes(auto(), FutureEffect.SendTo, 1)
    From_Action = DistortionAttributes(auto(), FutureEffect.PayForLater, 2)
    From_Orbital = DistortionAttributes(auto(), FutureEffect.PayForLater, 2)
    From_Starbase = DistortionAttributes(auto(), FutureEffect.PayForLater, 1)
    From_Cruiser = DistortionAttributes(auto(), FutureEffect.PayForLater, 2)
    From_Dreadnought = DistortionAttributes(auto(), FutureEffect.PayForLater, 3)
    From_Five_Six_Pink = DistortionAttributes(auto(), FutureEffect.PayForLater, 2)
    From_Five_Seven_Pink = DistortionAttributes(auto(), FutureEffect.PayForLater, 2)
    From_Five_Eight_Brown = DistortionAttributes(auto(), FutureEffect.PayForLater, 2)
    From_Five_Eight_Orange = DistortionAttributes(auto(), FutureEffect.PayForLater, 2)
    From_Plasma_Missile = DistortionAttributes(auto(), FutureEffect.PayForLater, 2)
    From_Gluon_Computer = DistortionAttributes(auto(), FutureEffect.PayForLater, 2)
    From_Positron_Computer = DistortionAttributes(auto(), FutureEffect.PayForLater, 1)
    From_Tachyon_Drive = DistortionAttributes(auto(), FutureEffect.PayForLater, 1)
    From_Tachyon_Source = DistortionAttributes(auto(), FutureEffect.PayForLater, 1)
