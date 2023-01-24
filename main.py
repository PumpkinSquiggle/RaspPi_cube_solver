from time import time

start = time()
print("START")

from piservo import Servo
import sys
from os import devnull
from color_extraction import cubestring_to_formatted_inst_testing, verbose_input, main
from movement import main_movements, computer_instructions
from instToServo import inst_to_servo
import servo_functions
DELAY_TIME = 1

FLIP_SERVO_DEFAULT_ANGLE = 10
FLIP_SERVO_END_ANGLE = 100

LOCKING_SERVO_DEFAULT_ANGLE = 20
LOCKING_SERVO_END_ANGLE = 110

HOLDER_SERVO_DEFAULT_ANGLE = 0

is_verbose = True

# TODO set up GPIO pinout on RasbPi
# TODO make all rgb_to_color statements ranges
# flip_servo = Servo(17)
# holder_servo = Servo(22)
# locking_servo = Servo(27)

if __name__ == '__main__':

    input_start = time()
    is_verbose = verbose_input()
    input_end = time()

    raw_inst = main(is_verbose)

    computer_formatted_inst = computer_instructions(raw_inst)
    command_list = inst_to_servo(computer_formatted_inst)
    for i in range(len(command_list)):
        if is_verbose:
            # remove 'print' when GPIO and RasbPi are set up
            exec('print(command_list[i])')
        else:
            # remove 'print' when GPIO and RasbPi are set up
            # using sys and os to enable and disable print for less verbose run
            sys.stdout = open(devnull, 'w')
            exec('print(command_list[i])')
            sys.stdout = sys.__stdout__
        i += 1

    main_movements(raw_inst)

    end = time()
    print("\n" + str((end - start) - (input_end - input_start)) + ' Seconds')
    if is_verbose:
        cubestring_to_formatted_inst_testing()
