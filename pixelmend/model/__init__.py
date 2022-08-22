from .lama import LaMa, AnimeLaMa
from .ldm import LDM
from .opencv2 import OpenCV2

models = {
    LaMa.name: LaMa,
    AnimeLaMa.name: AnimeLaMa,
    LDM.name: LDM,
    OpenCV2.name: OpenCV2,
}
