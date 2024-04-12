# Rubber Snaky
CircuitPython scripts for easy HID script programming

## Requirements
- A microcontroller with HID support (like the Samd21)
- CircuitPython 9 - You can follow [this](https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython) for instructions

## Install
Drag and drop the files (all python scripts and the `lib/` directory) to the mounted drive from CircuitPython.
> [!NOTE]
> The snaky will immediately start running after the installation.

## Changing the HID script
Open [command.py](command.py) and change the contents of the `run()` function.

And valid CircuitPython code works. You can use the aliased function names
for easier programming

## Preventing script execution
To stop the snaky from executing, it's possible to ground the A0 pin in the first
5 seconds. If the execution was stopped, the led on the board will turn on.

It's possible to change the delay time in [command.py](command.py).
