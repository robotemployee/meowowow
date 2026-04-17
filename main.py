from XRPLib.defaults import *
from XRPLib.gamepad import Gamepad
from machine import Pin
import time

board = Board.get_default_board()
gp = Gamepad.get_default_gamepad()

print("Ready! Left stick = forward/back, Right stick = turn. Press board button to stop.")

while not board.is_button_pressed():
    # Read left joystick Y axis for forward and backward movement
    # Value ranges from -1 (full back) to 1 (full forward)
    forward = gp.get_value(Gamepad.Y1)

    # Read right joystick X axis for turning left and right
    # Value ranges from -1 (full left) to 1 (full right)
    turn = gp.get_value(Gamepad.X2)

    # Combine forward and turn to get individual wheel efforts
    # Left wheel gets more effort when turning right, less when turning left
    left_effort  = forward - turn
    right_effort = forward + turn

    # Send effort values to the drivetrain
    drivetrain.set_effort(left_effort, right_effort)

    time.sleep(0.05)

drivetrain.set_effort(0, 0)
print("Stopped.")