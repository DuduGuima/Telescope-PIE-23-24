#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
class Stepper:
    def __init__(self, gpio_pins, min_delay=0.001, max_delay=0.01):
        self.out1 = gpio_pins[0]
        self.out2 = gpio_pins[1]
        self.out3 = gpio_pins[2]
        self.out4 = gpio_pins[3]
        self.actual_step = 0
        self.cw = True
        self.min_delay = min_delay
        self.max_delay = max_delay
        # setting up
        GPIO.setmode( GPIO.BCM )
        GPIO.setup( self.out1, GPIO.OUT )
        GPIO.setup( self.out2, GPIO.OUT )
        GPIO.setup( self.out3, GPIO.OUT )
        GPIO.setup( self.out4, GPIO.OUT )
        
        # initializing
        GPIO.output( self.out1, GPIO.LOW )
        GPIO.output( self.out2, GPIO.LOW )
        GPIO.output( self.out3, GPIO.LOW )
        GPIO.output( self.out4, GPIO.LOW )

    def cleanup(self):
        GPIO.output( self.out1, GPIO.LOW )
        GPIO.output( self.out2, GPIO.LOW )
        GPIO.output( self.out3, GPIO.LOW )
        GPIO.output( self.out4, GPIO.LOW )
        GPIO.cleanup()
    def set_direction(self, clockwise):
        self.cw=clockwise
    def fullstep(self):
        if self.actual_step==0:
            GPIO.output( self.out4, GPIO.HIGH )
            GPIO.output( self.out3, GPIO.LOW )
            GPIO.output( self.out2, GPIO.HIGH)
            GPIO.output( self.out1, GPIO.LOW )
        elif self.actual_step==1:
            GPIO.output( self.out4, GPIO.LOW )
            GPIO.output( self.out3, GPIO.HIGH)
            GPIO.output( self.out2, GPIO.HIGH )
            GPIO.output( self.out1, GPIO.LOW )
        elif self.actual_step==2:
            GPIO.output( self.out4, GPIO.LOW )
            GPIO.output( self.out3, GPIO.HIGH )
            GPIO.output( self.out2, GPIO.LOW )
            GPIO.output( self.out1, GPIO.HIGH )
        elif self.actual_step==3:
            GPIO.output( self.out4, GPIO.HIGH)
            GPIO.output( self.out3, GPIO.LOW )
            GPIO.output( self.out2, GPIO.LOW )
            GPIO.output( self.out1, GPIO.HIGH )
        if self.cw:
            self.actual_step=(self.actual_step+1)%4
        else:
            self.actual_step=(self.actual_step-1)%4
    def halfstep(self):
        if self.actual_step==0:
            GPIO.output( self.out4, GPIO.HIGH )
            GPIO.output( self.out3, GPIO.LOW )
            GPIO.output( self.out2, GPIO.HIGH)
            GPIO.output( self.out1, GPIO.LOW )
        elif self.actual_step==1:
            GPIO.output( self.out4, GPIO.LOW )
            GPIO.output( self.out3, GPIO.LOW )
            GPIO.output( self.out2, GPIO.HIGH )
            GPIO.output( self.out1, GPIO.LOW )
        elif self.actual_step==2:
            GPIO.output( self.out4, GPIO.LOW )
            GPIO.output( self.out3, GPIO.HIGH)
            GPIO.output( self.out2, GPIO.HIGH )
            GPIO.output( self.out1, GPIO.LOW )
        elif self.actual_step==3:
            GPIO.output( self.out4, GPIO.LOW )
            GPIO.output( self.out3, GPIO.HIGH )
            GPIO.output( self.out2, GPIO.LOW )
            GPIO.output( self.out1, GPIO.LOW )
        elif self.actual_step==4:
            GPIO.output( self.out4, GPIO.LOW )
            GPIO.output( self.out3, GPIO.HIGH )
            GPIO.output( self.out2, GPIO.LOW )
            GPIO.output( self.out1, GPIO.HIGH )
        elif self.actual_step==5:
            GPIO.output( self.out4, GPIO.LOW )
            GPIO.output( self.out3, GPIO.LOW )
            GPIO.output( self.out2, GPIO.LOW )
            GPIO.output( self.out1, GPIO.HIGH )
        elif self.actual_step==6:
            GPIO.output( self.out4, GPIO.HIGH)
            GPIO.output( self.out3, GPIO.LOW )
            GPIO.output( self.out2, GPIO.LOW )
            GPIO.output( self.out1, GPIO.HIGH )
        elif self.actual_step==7:
            GPIO.output( self.out4, GPIO.HIGH)
            GPIO.output( self.out3, GPIO.LOW )
            GPIO.output( self.out2, GPIO.LOW )
            GPIO.output( self.out1, GPIO.LOW )
        if self.cw:
            self.actual_step=(self.actual_step+1)%8
        else:
            self.actual_step=(self.actual_step-1)%8

    def motor_run(self, n_step, speed=100, clockwise=True , mode="half"):
        self.set_direction(clockwise)
        self.actual_step=0
        step_sleep = self.min_delay+(self.max_delay-self.min_delay)*(100-speed)/100
        try:
            i = 0
            for _ in range(n_step):
                if mode=="half":
                    self.halfstep()
                    time.sleep( step_sleep/2 )
                else:
                    self.fullstep()
                    time.sleep( step_sleep )
        
        except KeyboardInterrupt:
            self.cleanup()
            exit( 1 )

def main():

    gpio_pins = [17,18,27,22]

    myStepper = Stepper(gpio_pins)

    myStepper.motor_run(2000, clockwise=True, mode="half")
    time.sleep( 1 )
    myStepper.motor_run(1000, clockwise=False,mode="full")
    myStepper.cleanup()
    exit( 0 )

if __name__=="__main__":
    main()