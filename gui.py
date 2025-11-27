import tkinter as tk

def output(command, time):
    for i in range(0, 10):
        print(f"{command:>10}{time:16.7f}")