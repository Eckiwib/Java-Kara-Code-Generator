# JavaKara Code Generator

This is a small python tool in development to simplify the creation of walking paths for the ladybug "Kara".

## Features (planned and already included)
- [x] Select boxes
- [x] Set Kara's position
- [x] Toggle through 3 different states, depending on if Kara should just walk over it or put a leaf too
- [ ] Select tool to directly set boxes to a certain state
- [x] define custom function names for the default functions: `kara.move()`, `kara.turnLight()`, `kara.turnLeft()`, `kara.putLeaf()`,`kara.removeLeaf()`
- [x] Copy Java code to clipboard

## How to run
1. Python: Download at <https://www.python.org/>
2. Donwload all Python files and the settings.json
3. Start main.py
4. Left click box to toggle through states, set Kara by right-clicking, press an arrow key to make kara face this direction and finally press Generate to copy the Java code to your clipboard. You can edit the default Java commands in the settings.json if you defined own function names.
