# Below imports all neccessary packages to make this Python Script run
import time
import board
from adafruit_motor import stepper
from adafruit_motorkit import MotorKit

# Below initialises the variable kit to be our I2C Connected Adafruit Motor HAT
kit = MotorKit(i2c=board.I2C())

#PAN SEMPRE NO 1
#TILT SEMPRE NO 2


def center_moon(dist_y,dist_x):
    ver_x = dist_x>0
    ver_y = dist_y>0
    kit.stepper1.onestep(style=stepper.MICROSTEP)
    kit.stepper2.onestep(style=stepper.MICROSTEP)
    if ver_x:
        kit.stepper1.release()
        kit.stepper2.onestep(style= stepper.MICROSTEP)

    if not ver_x:
        kit.stepper1.release()
        kit.stepper2.onestep(direction = stepper.BACKWARD, style= stepper.MICROSTEP)

    if not ver_y:
        kit.stepper1.onestep(style = stepper.MICROSTEP)

    if  ver_y:
        kit.stepper1.onestep(direction = stepper.BACKWARD, style = stepper.MICROSTEP)
        

