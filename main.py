import time

from XRPLib.defaults import *
import colorsys
from typing import Tuple, cast

board: Board = Board.get_default_board()

hue: float = 0

while True:
    board.set_rgb_led(255,255,0)
    outputRgb: tuple[float, float, float] = cast(tuple[float, float, float], colorsys.hsv_to_rgb(hue, 1, 1))
    hue += 0.01
    if (hue > 1): hue = 0
    time.sleep(0.01)

