from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage
import _color_palette as cp
import main_screen as ms
import os
import sys
import customtkinter as ctk

# setting path
sys.path.append(os.getcwd() + r"/data/logic/")

import screen_logic as sl

code = 'aaa'

class LoginScreen:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.geometry("568x308")
        self.window.title('EXCHANGE')
        self.window.configure(bg=cp.background_color)

        label = ctk.CTkLabel(self.window, text="Passwort eingeben zum entsperren")
        label.place(x = 90, y = 70)

        eingabe = ctk.CTkEntry(self.window, width=420, height=55)
        eingabe.place(x = 90, y = 100)

        self.login_button = ctk.CTkButton(
            self.window, 
            text = 'Entsperren',
            width = 420,
            height = 55,
            fg_color = cp.main_color, 
            text_color = cp.accent_color,
            hover_color = cp.second_color,
            command = lambda: self.openMainScreen(eingabe.get()))
        self.login_button.place(x = 90,y = 170)

        self.window.resizable(False, False)
   
    def relative_to_assets(self, path: str) -> Path:
        ASSETS_PATH = Path(os.getcwd() + r"/data/assets/login")
        return ASSETS_PATH / Path(path)
        
    def openMainScreen(self, login):
        if login:
            #TODO: checken ob der Service überhaupt aktiv ist
            self.window.destroy()
            
            obj = ms.MainScreen()
            obj.window.mainloop()        