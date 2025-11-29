import tkinter as tk
import logic

#windows config
w_size_x = 600
w_size_y = 700

root = tk.Tk()
root.geometry(f"{w_size_x}x{w_size_y}")
root.title("Java Kara Skript Generator")

max = 3

#grid Settings
rows = 15
cols = 15
scattering = 30
size = 30
states = [[0 for _ in range(rows)] for _ in range(cols)]
colors = ["white","gray","green"]

kara = [7,14,"up"]
facings = ("up","right","down","left")

def toggle_bg(btn, row, col):
    states[row][col] = (states[row][col]+1)%max
    btn.config(bg=colors[states[row][col]])
    print(f"Button: ({row}|{col}) is currently at state: {states[row][col]}")

def generate():
    logic.generate(states, kara)

def setkara(btn, row, col):
    global kara_l, kara
    try:
        kara_l.config(bg="white")
    except:
        pass
    kara_l = btn
    kara_l.config(bg="red")

    kara[0] = row
    kara[1] = col

    print(kara)

def rotkara(key):
    kara[2] = key
    print(key)

root.bind("<Up>", lambda event:rotkara("up"))
root.bind("<Right>", lambda event:rotkara("right"))
root.bind("<Down>", lambda event:rotkara("down"))
root.bind("<Left>", lambda event:rotkara("left"))

gen_button = tk.Button(root, text="Generate", command=generate)
gen_button.pack()
rot_button = tk.Button(root, text="Rotate")
rot_button.pack()

#center alignment for the grid
x_align = (w_size_x-size*rows)/2
y_align = (w_size_y-size*cols)/2

for r in range(rows):
    for c in range(cols):
        grid_button = tk.Button(root, bg="white")
        grid_button.bind("<Button-3>", lambda event, b=grid_button, x=r, y=c:setkara(b,x,y))
        grid_button.config(command=lambda b=grid_button, x=r, y=c: toggle_bg(b, x, y))
        grid_button.place(x=r*scattering+x_align, y=c*scattering+y_align, width=size, height=size)

root.mainloop()