import tkinter as tk

max = 3

class window:
    def __init__(self, w_size_x, w_size_y, states, colors, size, rows, cols, scattering, kara, generate) -> None:
        
        self.states = states
        self.colors = colors
        self.size = size
        self.scattering = scattering
        self.generate = generate
        self.w_size_x = w_size_x
        self.w_size_y = w_size_y
        self.rows = rows
        self.cols = cols
        self.kara = kara

        self.root = tk.Tk()
        self.root.geometry(f"{w_size_x}x{w_size_y}")
        self.root.title("Java Kara Skript Generator")

        self.arrow_binding()
        self.g_button()
        self.grid()

    def toggle_bg(self, btn, row, col):
        self.states[row][col] = (self.states[row][col]+1)%max
        btn.config(bg=self.colors[self.states[row][col]])
        print(f"Button: ({row}|{col}) is currently at state: {self.states[row][col]}")

    def setkara(self, btn, row, col):
        try:
            self.kara_last.config(bg="white")
        except:
            pass
        self.kara_last = btn
        self.kara_last.config(bg="red")
        self.kara[0] = row
        self.kara[1] = col

        print(self.kara)

    def rotkara(self, key):
        self.kara[2] = key
        print(key)

    def arrow_binding(self):
        self.root.bind("<Up>", lambda event:self.rotkara(0))
        self.root.bind("<Right>", lambda event:self.rotkara(1))
        self.root.bind("<Down>", lambda event:self.rotkara(2))
        self.root.bind("<Left>", lambda event:self.rotkara(3))

    def g_button(self):
        gen_button = tk.Button(self.root, text="Generate", command=lambda:self.generate(self.states, self.kara))
        gen_button.pack()

    def grid(self):
        #center alignment for the grid
        x_align = (self.w_size_x-self.size*self.rows)/2
        y_align = (self.w_size_y-self.size*self.cols)/2

        for r in range(self.rows):
            for c in range(self.cols):
                grid_button = tk.Button(self.root, bg="white")
                grid_button.bind("<Button-3>", lambda event, b=grid_button, x=r, y=c:self.setkara(b,x,y))
                grid_button.config(command=lambda b=grid_button, x=r, y=c: self.toggle_bg(b, x, y))
                grid_button.place(x=r*self.scattering+x_align, y=c*self.scattering+y_align, width=self.size, height=self.size)
    
    def run(self):
        self.root.mainloop()