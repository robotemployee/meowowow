import time

from XRPLib.defaults import *

board: Board = Board.get_default_board()
gamepad: Gamepad = Gamepad.get_default_gamepad()

while True:
    board.set_rgb_led(255,255,0)
    
    time.sleep(0.05)
