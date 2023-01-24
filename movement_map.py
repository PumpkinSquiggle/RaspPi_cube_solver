movement_map = {
    'R': {
        0: 'holder_servo.write(HOLDER_SERVO_COUNTER_CLOCKWISE)'
           '\ndelay(HOLDER_SERVO_90_TIME)'
           '\nholder_servo.write(HOLDER_SERVO_STOP)'
           '\ndelay(DELAY_TIME)' 
           '\nflip()' 
           '\ndelay(DELAY_TIME)',
        1: 'holder_servo.write(HOLDER_SERVO_CLOCKWISE)'
           '\ndelay(HOLDER_SERVO_90_TIME)'
           '\nholder_servo.write(HOLDER_SERVO_STOP)'
           '\ndelay(DELAY_TIME)'
           '\nholder_servo.write(HOLDER_SERVO_CLOCKWISE)'
           '\ndelay(HOLDER_SERVO_90_TIME)'
           '\nholder_servo.write(HOLDER_SERVO_STOP)'
           '\ndelay(DELAY_TIME)'
           '\nflip()'
           '\ndelay(DELAY_TIME)'
           '\nholder_servo.write(HOLDER_SERVO_COUNTER_CLOCKWISE)'
           '\ndelay(HOLDER_SERVO_90_TIME)'
           '\nholder_servo.write(HOLDER_SERVO_STOP)'
           '\ndelay(DELAY_TIME)'
    },
    'L': {
        0: 'holder_servo.write(HOLDER_SERVO_CLOCKWISE)'
           '\ndelay(HOLDER_SERVO_90_TIME)'
           '\nholder_servo.write(HOLDER_SERVO_STOP)'
           '\ndelay(DELAY_TIME)'
           '\nflip()'
           '\ndelay(DELAY_TIME)',
        1: 'holder_servo.write(HOLDER_SERVO_CLOCKWISE)'
           '\ndelay(HOLDER_SERVO_90_TIME)'
           '\nholder_servo.write(HOLDER_SERVO_STOP)'
           '\ndelay(DELAY_TIME)'
           '\nholder_servo.write(HOLDER_SERVO_CLOCKWISE)'
           '\ndelay(HOLDER_SERVO_90_TIME)'
           '\nholder_servo.write(HOLDER_SERVO_STOP)'
           '\ndelay(DELAY_TIME)'
           '\nflip()'
           '\ndelay(DELAY_TIME)'
           '\nholder_servo.write(HOLDER_SERVO_CLOCKWISE)'
           '\ndelay(HOLDER_SERVO_90_TIME)'
           '\nholder_servo.write(HOLDER_SERVO_STOP)'
           '\ndelay(DELAY_TIME)'
    },
    'F': {
        0: 'holder_servo.write(HOLDER_SERVO_CLOCKWISE)'
           '\ndelay(HOLDER_SERVO_90_TIME)'
           '\nholder_servo.write(HOLDER_SERVO_STOP)'
           '\ndelay(DELAY_TIME)'
           '\nholder_servo.write(HOLDER_SERVO_CLOCKWISE)'
           '\ndelay(HOLDER_SERVO_90_TIME)'
           '\nholder_servo.write(HOLDER_SERVO_STOP)'
           '\ndelay(DELAY_TIME)'
           '\nflip()'
           '\ndelay(DELAY_TIME)',
        1: 'holder_servo.write(HOLDER_SERVO_CLOCKWISE)'
           '\ndelay(HOLDER_SERVO_90_TIME)'
           '\nholder_servo.write(HOLDER_SERVO_STOP)'
           '\ndelay(DELAY_TIME)'
           '\nholder_servo.write(HOLDER_SERVO_CLOCKWISE)'
           '\ndelay(HOLDER_SERVO_90_TIME)'
           '\nholder_servo.write(HOLDER_SERVO_STOP)'
           '\ndelay(DELAY_TIME)'
           '\nflip()'
           '\ndelay(DELAY_TIME)'
    },
    'U': {
        0: 'flip()'
           '\ndelay(DELAY_TIME)'
           '\nflip()'
           '\ndelay(DELAY_TIME)',
        1: 'flip()'
           '\ndelay(DELAY_TIME)'
           '\nflip()'
           '\ndelay(DELAY_TIME)'
    },
    'D': {
        0: "print('rotate to D (nothing required)')",
        1: "print('rotate from D (nothing required)')"
    },
    'B': {
        0: 'flip()'
           '\ndelay(DELAY_TIME)',
        1: 'flip()'
           '\ndelay(DELAY_TIME)'
           '\nflip()'
           '\ndelay(DELAY_TIME)'
           '\nflip()'
           '\ndelay(DELAY_TIME)'
    }
}
