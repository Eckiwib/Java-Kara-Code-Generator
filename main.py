import gui
import logic
import pyperclip
import json

# load settings
with open("settings.json","r") as file:
    settings = json.load(file)

# windows config
WIDTH = settings["window"]["width"]
HEIGHT = settings["window"]["height"]

# grid Settings
GS = settings["grid"]
ROWS = GS["rows"]
COLS = GS["columns"]
SCATTERING = GS["scattering"]
SIZE = GS["size"]
COLORS = GS["colors"]
kara = settings["kara"]

# List definition for saving grid states
STATES = [[0 for _ in range(ROWS)] for _ in range(COLS)]

java_commands = settings["Java_commands"]

# Function to run the generation of the code
def generate(states, kara):
    # Class initialisation
    generator = logic.generate(states, kara)
    # fac for facing to check
    fac = 0
    # Create empty list for the commands
    cmds = []
    # Main loop: stops when all three squares have been checked
    while fac < 3:
        # check all surrounding squares
        for fac in range(4):
            check = generator.check(fac)
            if check > 0:
                fac_cmd = generator.fac_cmd()
                if fac_cmd == "r":
                    cmds.append(java_commands["Turn right"])
                elif fac_cmd == "l":
                    cmds.append(java_commands["Turn left"])
                elif fac_cmd == "ll":
                    cmds.append(java_commands["Turn left"])
                    cmds.append(java_commands["Turn left"])

                cmds.append(java_commands["Move"])

                generator.updatekara()
                break
    
    print(cmds)
    pyperclip.copy("\n".join(cmds))

window = gui.window(w_size_x=WIDTH, w_size_y=HEIGHT, size=SIZE,rows=ROWS, cols=COLS, scattering=SCATTERING, states=STATES, colors=COLORS, kara=kara, generate=generate)
window.run()