from .lama import LaMa, AnimeLaMa
from .opencv2 import OpenCV2

models = {
    LaMa.name: LaMa,
    AnimeLaMa.name: AnimeLaMa,
    OpenCV2.name: OpenCV2,
}
