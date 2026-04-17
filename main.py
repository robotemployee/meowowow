import colorsys
from typing import Tuple, cast, TypeAlias

from XRPLib.defaults import *
import time

board: Board = Board.get_default_board()

hue: float = 0

Vec3Float: TypeAlias = tuple[float, float, float]
Vec3Int: TypeAlias = tuple[int, int, int]

while True:
    outputRgbFloat: Vec3Float = cast(Vec3Float, colorsys.hsv_to_rgb(hue, 1, 1))
    outputRgb: Vec3Int = Vec3Int(int(x * 255) for x in outputRgbFloat)
    board.set_rgb_led(*outputRgb)
    hue += 0.01
    if (hue > 1): hue = 0
    time.sleep(0.01)
