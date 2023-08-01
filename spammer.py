from time import sleep
import sys
try:
    import pip
except ImportError:
    from pip._internal import main as pip
print("Installing required libraries...")
pip.main(["install", "--user", "pynput"])
from pynput.mouse import Controller, Button
from pynput import keyboard
from pynput.keyboard import Key
keyboard = keyboard.Controller()
mouse = Controller()
spamword = input("Enter the text that you would like to spam:")
spamtimes = int(input("Enter the number of times you would like to spam the text:"))
app = input("Select the app that you are using to spam (type max ONLY if you know what you are doing):")
if app == "Teams" or app == "Microsoft Teams" or app == "MS Teams":
    appspeed = 0.6
elif app == "WhatsApp" or app == "WA" or app == "Whatsapp" or app == "wa" or app=="Discord" or app=="discord":
    appspeed = 0.2
elif app == 'max' or 'MAX':
    appspeed = 0.0
else:
    print("Invalid/unsupported app. Make an issue on GitHub (AetherYT) to suggest new app support.")
    sys.exit()
input("PLACE YOUR MOUSE ON TYPING AREA AND PRESS ENTER:")
cursorpos = Controller().position
print("MOUSE POSITION LOGGED!")
sleep(1.0)
print("MAKE SURE THAT YOU DON'T MOVE THE MOUSE!")
sleep(1.0)
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
print("Credits to SpookySec for original and AetherYT for improved version.")
sleep(2.0)
close = input("Press Enter to close this script.")
