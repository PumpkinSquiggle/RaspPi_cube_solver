from piservo import Servo
from time import sleep

DELAY_TIME = 1

FLIP_SERVO_DEFAULT_ANGLE = 10
FLIP_SERVO_END_ANGLE = 100

LOCKING_SERVO_DEFAULT_ANGLE = 190
LOCKING_SERVO_END_ANGLE = 108

HOLDER_SERVO_STOP = 90
HOLDER_SERVO_CLOCKWISE = 95
HOLDER_SERVO_COUNTER_CLOCKWISE = 85
HOLDER_SERVO_90_TIME = 0.392

flip_servo = Servo(2)
holder_servo = Servo(3)
locking_servo = Servo(9)


def init():
    activate_servo(FLIP_SERVO_DEFAULT_ANGLE, flip_servo)
    holder_servo.write(HOLDER_SERVO_STOP)
    activate_servo(LOCKING_SERVO_DEFAULT_ANGLE, locking_servo)
    sleep(DELAY_TIME)


def flip():
    activate_servo(FLIP_SERVO_END_ANGLE, flip_servo)
    sleep(DELAY_TIME)
    activate_servo(FLIP_SERVO_DEFAULT_ANGLE, flip_servo)


def locking_bar(b: bool):
    # Error Handling
    if locking_servo.read() == LOCKING_SERVO_DEFAULT_ANGLE and b is False:
        print("Error: moved to False which is where it already is")
        return
    # Error Handling
    if locking_servo.read() == LOCKING_SERVO_END_ANGLE and b is True:
        print("Error: moved to True which is where it already is")
        return

    # Movement Logic Below
    if b is False:
        activate_servo(LOCKING_SERVO_DEFAULT_ANGLE, locking_servo)
        sleep(DELAY_TIME)
        return

    if b is True:
        activate_servo(LOCKING_SERVO_END_ANGLE, locking_servo)
        sleep(DELAY_TIME)
        return


def activate_servo(end_angle: int, servo: Servo):
    if servo.read() == end_angle:
        return
    if servo.read() < end_angle:
        direction = 1
    if servo.read() > end_angle:
        direction = -1
    while servo.read() != end_angle:
        servo.write(servo.read() + direction)
        sleep(0.01)


