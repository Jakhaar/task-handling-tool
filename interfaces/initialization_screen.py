# Import necessary libraries and modules
from pathlib import Path
import time
from tkinter import Tk, Canvas, Entry, Button, PhotoImage
import _color_palette as cp
import main_screen as ms
import os
import sys
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

# Set the path for custom modules
sys.path.append(os.getcwd() + r"/data/logic/")

# Import the screen logic module
import screen_logic as sl

class InitializationScreen:
    def __init__(self, action_text):
        # Initialize the window
        self.window = ctk.CTk()
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        window_width = 500  
        window_height = 250  

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.window.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.window.title('EXCHANGE')
        self.window.configure(bg=cp.background_color)

        label = ctk.CTkLabel(self.window, text=action_text)
        label.place(x=90, y=70)

        # Make the window non-resizable
        self.window.resizable(False, False)

if __name__ == '__main__':
    obj = InitializationScreen("r")
    obj.window.mainloop()