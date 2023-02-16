from pynput.mouse import Controller, Button
from pynput import keyboard
from pynput.keyboard import Key
from time import sleep
import sys
try:
    import pip
except ImportError:
    from pip._internal import main as pip
print("Installing pynput...")
pip.main(["install", "--user", "pynput"])
keyboard = keyboard.Controller()
mouse = Controller()
spamword = input("What would you like to spam?:")
spamtimes = int(input("How many times would you like to spam?:"))
app = input("Select app that you are using to spam:")
if app == "Teams" or app == "Microsoft Teams":
    appspeed = 0.6
elif app == "WhatsApp" or app == "WA" or app == "Whatsapp":
    appspeed = 0.2
else:
    print("Invalid/unsupported app.")
    sys.exit()
input("PLACE YOUR MOUSE ON TYPING AREA AND PRESS ENTER: ")
cursorpos = Controller().position
print("MOUSE POSITION LOGGED!")
print("MAKE SURE THAT YOU DON'T MOVE THE MOUSE!")
input("PRESS ENTER TO START SPAMMING!")
for i in range(spamtimes+1):
    word = spamword
    mouse.position = cursorpos
    mouse.click(Button.left)
    keyboard.type(word)
    keyboard.press(Key.enter)
    sleep(appspeed)
print("FINISHED SPAMMING!")
sleep(1.0)
print("Credits to SpookySec for original script and AetherYT for improved version")
sleep(1.0)
close = input("Press Enter to close this script.")
