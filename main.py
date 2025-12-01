import gui
import logic
import pyperclip
import json

#windows config
w_size_x = 600
w_size_y = 700

max = 3

#grid Settings
rows = 15
cols = 15
scattering = 30
size = 30
states = [[0 for _ in range(rows)] for _ in range(cols)]
colors = ["white","gray","green"]

kara = [7,14,0]

pyperclip("\n".join(logic.generate(gui.states, gui.kara)))