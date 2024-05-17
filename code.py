import board
import digitalio
import command
import time

def execute_snaky():
    print() # fix newline output
    command.run()

safety_pin = digitalio.DigitalInOut(board.A0)
safety_pin.direction = digitalio.Direction.INPUT
safety_pin.pull = digitalio.Pull.UP

led = digitalio.DigitalInOut(board.LED_INVERTED)
led.direction = digitalio.Direction.OUTPUT
led.value = True

counter = command.sleep_time_sec * 2
safety_flag = command.NO_RUN # if NO_RUN is enabled, safety_flag automatically is on.
while counter > 0 and not safety_flag:
    time.sleep(0.5)
    counter -= 1

    if command.DEBUG:
        led.value = counter % 2 # flash the led at 1 HZ


    safety_flag = not safety_pin.value # safety button pressed => flag is True

if not safety_flag:
    execute_snaky()
else:
    led.value = False
    while True:
        pass
