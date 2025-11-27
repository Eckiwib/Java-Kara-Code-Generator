import tkinter as tk

root = tk.Tk()
root.geometry("600x700")
root.title("Java Kara Skript Generator")

rows = 10
cols = 10

def test():
    print("kara.move()")

button = tk.Button(root, text="Generate", command=test)
button.pack()

gridtest = tk.Button(root, text="Test")
gridtest.pack

root.mainloop()