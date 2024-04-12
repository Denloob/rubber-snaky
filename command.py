import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

import time

sleep_time_sec: int = 5 # The amount of time to wait before running the snaky script

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

sleep = time.sleep
write = keyboard_layout.write
press = keyboard.press
release = keyboard.release
release_all = keyboard.release_all
send = keyboard.send


def run():
    # Here goes the rubber snaky code
    # Default available functions:
    #   sleep(seconds: int) - stop script execution for `seconds` seconds
    #   write(text: str) - type in text. Use `\n` for new line
    #   press(keycode1: Keycode, ...) - press keys at the same time (without releasing it)
    #   release(keycode1: Keycode, ...) - release keys
    #   release_all() - release all keys
    #   send(keycode1: Keycode, ...) - press keys at the same time and then release them
    return

    # Example rubber snaky script for updating and installing some software in ubuntu
    send(Keycode.CTRL, Keycode.SHIFT, Keycode.T) # Open the terminal using the CTRL+SHIFT+T shortcut

    sleep(0.5) # Let the terminal start
    write("sudo apt update && sudo apt upgrade && sudo apt install git build-essential neovim firefox") # Write the command to perform the update
