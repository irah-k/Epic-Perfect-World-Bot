# Epic Perfect World Bot

Scrappy script that automates attacking, collecting coins, and depositing automatically at the nearest banker.

The script only interacts with keyboard and mouse inputs, and doesn't snoop with internal game memory like conventional bots. It uses OCR to interpret targets that are visible from the character pov.

Specifically works for the Epic Perfect World Server for farming bronze coins (at the NightScream Island), but targets can be modified to farm any mob and drops in the game.


Requirements:
Python 3+
Tesseract OCR (pytesseract)
win32gui (requires windows, can be substituted with some changes)

Game Settings:
Set the first auto rally point to somewhere on NightScream Island with crystals
Set the second to the banker on the island

Some values are hardcoded for the screen resolution, so use the Position.py script to determine cursor position

There are some tunable factors that can be customized, like the number of coins to collect before triggering the deposit at banker.

Gameplay:
-Best performed with a Duskblade since cooldowns on dashes is instant with kills, and picking drops requires melee range.
-The script automates the selection of only the crystals (using OCR to detect the text), and avoids any players or other mobs.
-Since it's a pk area, it's best to deposit at the banker often
-The deposit sequence uses town portals each time, so be sure to stock up on those before starting the bot
-The script uses mouse clicks and keyboard inputs, and EPW needs to be on the screen so that targets can be interpreted. The script is automatically paused if the game is not in the foreground.
