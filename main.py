#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.parameters import Button, Color
from pybricks.tools import wait

# Initialize the EV3 Brick
ev3 = EV3Brick()

# Set volume to 100% and make a beep to signify program has started
ev3.speaker.set_volume(100)
ev3.speaker.beep()

# Turn off the light
ev3.light.off()

# Output the current battery status
print("Current battery voltage: ", ev3.battery.voltage())
print("Current battery current: ", ev3.battery.current())

# Set the starting values of each button
leftButton = "Off"
rightButton = "Off"
upButton = "Off"
downButton = "Off"
centerButton = "Off"

# Create a loop to react to buttons
while True:

    # Check for left button events
    if Button.LEFT in ev3.buttons.pressed() and leftButton == "Off":
        leftButton = "On"
        ev3.light.on(Color.RED)
    elif Button.LEFT not in ev3.buttons.pressed() and leftButton == "On":
        leftButton = "Off"

    # Check for right button events
    if Button.RIGHT in ev3.buttons.pressed() and rightButton == "Off":
        rightButton = "On"
        ev3.light.on(Color.GREEN)
    elif Button.RIGHT not in ev3.buttons.pressed() and leftButton == "On":
        rightButton = "Off"

    # Check for up button events
    if Button.UP in ev3.buttons.pressed() and upButton == "Off":
        upButton = "On"
        ev3.light.on(Color.YELLOW)
    elif Button.UP not in ev3.buttons.pressed() and upButton == "On":
        upButton = "Off"

    # Check for up button events
    if Button.DOWN in ev3.buttons.pressed() and downButton == "Off":
        downButton = "On"
        ev3.light.on(Color.ORANGE)
    elif Button.DOWN not in ev3.buttons.pressed() and downButton == "On":
        downButton = "Off"

    # Check for center button events
    if Button.CENTER in ev3.buttons.pressed() and centerButton == "Off":
        centerButton = "On"
        ev3.light.off()
        break

    wait(20)

# Use the speech tool to signify the program has finished
ev3.speaker.say("Program complete")
