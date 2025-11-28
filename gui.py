import tkinter as tk
import time
import logic

#windows config
w_size_x = 600
w_size_y = 700

root = tk.Tk()
root.geometry(f"{w_size_x}x{w_size_y}")
root.title("Java Kara Skript Generator")

#grid Settings
rows = 10
cols = 10
scattering = 30
size = 30

def toggle_bg():
    grid_button.config(bg="red")
def Generate():
    pass

button = tk.Button(root, text="Generate")
button.pack()

#center alignment for the grid
x_align = (w_size_x-size*rows)/2
y_align = (w_size_y-size*cols)/2

for r in range(rows):
    for c in range(cols):
        grid_button = tk.Button(root, command=toggle_bg)
        grid_button.place(x=r*scattering+x_align, y=c*scattering+y_align, width=size, height=size)

root.mainloop()