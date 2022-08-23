from .lama import LaMa, AnimeLaMa
from .ldm import LDM
from .mat import MAT
from .opencv2 import OpenCV2
from .zits import ZITS

models = {
    LaMa.name: LaMa,
    AnimeLaMa.name: AnimeLaMa,
    LDM.name: LDM,
    ZITS.name: ZITS,
    MAT.name: MAT,
    OpenCV2.name: OpenCV2,
}
