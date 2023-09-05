# Import necessary libraries and modules
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage
import _color_palette as cp
import main_screen as ms
import os
import sys
import customtkinter as ctk

# Set the path for custom modules
sys.path.append(os.getcwd() + r"/data/logic/")

# Import the screen logic module
import screen_logic as sl

# Initialize an empty password
code = ''

# Create the login screen class
class LoginScreen:
    def __init__(self):
        # Initialize the login window
        self.window = ctk.CTk()
        self.window.geometry("568x308")
        self.window.title('EXCHANGE')
        self.window.configure(bg=cp.background_color)

        # Create a label for entering the password
        label = ctk.CTkLabel(self.window, text="Enter the password to unlock")
        label.place(x=90, y=70)

        # Create an input field for password entry
        eingabe = ctk.CTkEntry(self.window, width=420, height=55)
        eingabe.place(x=90, y=100)

        # Create a login button
        self.login_button = ctk.CTkButton(
            self.window, 
            text='Unlock',
            width=420,
            height=55,
            fg_color=cp.main_color, 
            text_color=cp.accent_color,
            hover_color=cp.second_color,
            command=lambda: self.openMainScreen(eingabe.get()))
        self.login_button.place(x=90, y=170)

        # Make the window non-resizable
        self.window.resizable(False, False)
   
    # Function to determine the path relative to assets
    def relative_to_assets(self, path: str) -> Path:
        ASSETS_PATH = Path(os.getcwd() + r"/data/assets/login")
        return ASSETS_PATH / Path(path)
        
    # Function to open the main screen if the password is correct
    def openMainScreen(self, password):
        if password == code:
            # TODO: Check if the service is active
            self.window.destroy()
            
            obj = ms.MainScreen()
            obj.window.mainloop()
