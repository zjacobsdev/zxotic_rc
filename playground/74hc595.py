from time import sleep
import board
import digitalio
import adafruit_74hc595

osr_latch_pin = digitalio.DigitalInOut(board.D5)

SHIFT_REGISTERS_NUM = 1

osr = adafruit_74hc595.ShiftRegister74HC595(board.SPI(), osr_latch_pin, SHIFT_REGISTERS_NUM)

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



    # Set individual LEDs
    led_0.value = True   # turn on LED 1 only
    sleep(3)
    led_0.value = False  # turn off LED 1 only
    sleep(3)
    led_1.value = True   # turn on LED 1 only
    sleep(3)
    led_1.value = False  # turn off LED 1 only
    sleep(3)
    led_2.value = True   # turn on LED 1 only
    sleep(3)
    led_2.value = False  # turn off LED 1 only
    sleep(3)
 
 
   
    # led_2.value = False  # turn off LED 1 only
    # led_3.value = True   # turn on LED 6 only
    # sleep(3)
    # led_3.value = False  # turn off LED 6 only
    # sleep(3)
    # led_4.value = True   # turn on LED 1 only
    # sleep(3)
    # led_4.value = False  # turn off LED 1 only
    # led_5.value = True   # turn on LED 6 only
    # sleep(3)
    # led_5.value = False  # turn off LED 6 only
    # led_6.value = True   # turn on LED 1 only
    # sleep(3)
    # led_6.value = False  # turn off LED 1 only
    # led_7.value = True   # turn on LED 6 only
    # sleep(3)
    # led_7.value = False  # turn off LED 6 only
    # sleep(3)

    # # Set multiple LEDs
    # led_0.value = True   # turn on even numbered LEDs
    # led_2.value = True
    # led_4.value = True
    # led_6.value = True
    # sleep(1)
    # led_0.value = False  # turn off even numbered LEDs
    # led_2.value = False
    # led_4.value = False
    # led_6.value = False
    # led_1.value = True   # turn on odd numbered LEDs
    # led_3.value = True
    # led_5.value = True
    # led_7.value = True
    # sleep(1)
    # led_1.value = False  # turn off odd numbered LEDs
    # led_3.value = False
    # led_5.value = False
    # led_7.value = False
    # sleep(1)

# Main
while True:
    change_single_outputs()