"""
setup for light module using a 74hc595 shift resistor 

yes brake lights and tail lights are seperate bulbs apparently 
"""
import board
import digitalio
import adafruit_74hc595

osr_latch_pin = digitalio.DigitalInOut(board.D5)

SHIFT_REGISTERS_NUM = 1

osr = adafruit_74hc595.ShiftRegister74HC595(board.SPI(), osr_latch_pin, SHIFT_REGISTERS_NUM)

# pins = [sr.get_pin(0), sr.get_pin(1), sr.get_pin(2), sr.get_pin(3),
#         sr.get_pin(4), sr.get_pin(5), sr.get_pin(6), sr.get_pin(7)]
def change_single_outputs():
    # Output pin definitions (pin references)
    led_0 = osr.get_pin(0)
    led_1 = osr.get_pin(1)
    led_2 = osr.get_pin(2)
    led_3 = osr.get_pin(3)
    led_4 = osr.get_pin(4)
    led_5 = osr.get_pin(5)
    led_6 = osr.get_pin(6)
    led_7 = osr.get_pin(7)


headLights = {
    "front_left" : osr.get_pin(0),
    "front_right": osr.get_pin(1)
    
    }

brakeLights = {
    "brakelight_left": osr.get_pin(3),
    "brakelight_right": osr.get_pin(4),

}

tailLight = {
    "taillight_left": osr.get_pin(5),
    "taillight_right": osr.get_pin(6),

}


tailLight = {
    "taillight_left": osr.get_pin(5),
    "taillight_right": osr.get_pin(6),

}

# hazardLights ={
#     "hazardlight_left":osr.get_pin(7)
#     "hazardlght_right": osr.get_pin(8)
# } 