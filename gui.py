import tkinter as tk
import time
import logic

#windows config
w_size_x = 600
w_size_y = 700

root = tk.Tk()
root.geometry(f"{w_size_x}x{w_size_y}")
root.title("Java Kara Skript Generator")

max = 3

#grid Settings
rows = 11
cols = 11
scattering = 30
size = 30
states = [[0 for _ in range(rows)] for _ in range(cols)]
colors = ["white","gray","green"]

def toggle_bg(btn, row, col):
    states[row][col] = (states[row][col]+1)%max
    btn.config(bg=colors[states[row][col]%max])
    print(f"Button: ({row}|{col}) is currently at state: {states[row][col]}")

def Generate():
    pass

button = tk.Button(root, text="Generate")
button.pack()

#center alignment for the grid
x_align = (w_size_x-size*rows)/2
y_align = (w_size_y-size*cols)/2

for r in range(1,rows):
    for c in range(1,cols):
        grid_button = tk.Button(root, bg="white")
        grid_button.config(command=lambda b=grid_button, x=r, y=c: toggle_bg(b, x, y))
        grid_button.place(x=r*scattering+x_align, y=c*scattering+y_align, width=size, height=size)

root.mainloop()