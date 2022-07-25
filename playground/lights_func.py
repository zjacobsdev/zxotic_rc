# from enum import Enum
from time import sleep
import board
import digitalio
import adafruit_74hc595

osr_latch_pin = digitalio.DigitalInOut(board.D5)

SHIFT_REGISTERS_NUM = 1

osr = adafruit_74hc595.ShiftRegister74HC595(board.SPI(), osr_latch_pin, SHIFT_REGISTERS_NUM)

light_signal = False


# class FrontLights(Enum):
#     TURN_ON = True
#     TURN_OFF= False

# driver_input ={
#     lights_on = True
#     lights_out 
# }

def light_controller(lights):
    if lights == True:
        front_lights_on()
    else:
        front_lights_turn_signal()




        


def front_lights_on():
    front_light_headlight_1 = osr.get_pin(6)
    front_light_headlight_2 = osr.get_pin(7)

    front_light_headlight_1.value = True;
    front_light_headlight_2.value  = True;
    sleep(5)
    front_light_headlight_1.value = False;
    front_light_headlight_2.value  = False;
    sleep(5)


 

def front_lights_turn_signal():
    front_light_left = osr.get_pin(4)
    front_light_right = osr.get_pin(5)

    front_light_left.value = True;
    front_light_right.value  = True;
    sleep(5)
    front_light_left.value = False;
    front_light_right.value = False;
    sleep(5)


while True:
    light_controller(light_signal)