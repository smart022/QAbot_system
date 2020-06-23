from enum import Enum, unique

@unique
class LayerType(Enum):
    QU=0# QueryUnderstand
    BB=1# BusinessBase
    RG=2# ResponselGen

@unique
class BusinessType(Enum):
    Default=0#
    QABot=1 #
    ChatBot=2#