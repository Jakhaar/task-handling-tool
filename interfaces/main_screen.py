from pathlib import Path
import random
from tkinter import Tk
import customtkinter as ctk
import os
import _color_palette as cp
import math

class MainScreen:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.geometry("1200x680")
        self.window.title('EXCHANGE')
        self.window.configure(bg=cp.background_color)

        self.task_list = ['task1', 'task2', 'task3', 'task4','sdgf']
        
        # Buttons layout
        run_button = ctk.CTkButton(
            self.window, 
            text = 'Task Ausführen',
            width=180,
            height=32,
            fg_color = cp.main_color, 
            text_color = cp.accent_color,
            hover_color = cp.second_color,
            command = lambda: print('Run'))
        run_button.place(x=8,y=100)

        add_button = ctk.CTkButton(
            self.window, 
            text = 'Hizufügen',
            width=180,
            height=32,
            fg_color = cp.main_color, 
            text_color = cp.accent_color,
            hover_color = cp.second_color,
            command = lambda: self.add_task(frame = toggle_frame, task=random.randrange(1, 50)))
        add_button.place(x=8,y=140)

        del_button = ctk.CTkButton(
            self.window, 
            text = 'Löschen',
            width=180,
            height=32,
            fg_color = cp.main_color, 
            text_color = cp.accent_color,
            hover_color = cp.second_color,
            command = lambda: self.delete_task(toggle_frame))
        del_button.place(x=8,y=180)
        
        reset_button = ctk.CTkButton(
            self.window, 
            text = 'Dienst Neustart',
            width=180,
            height=32,
            fg_color = cp.main_color, 
            text_color = cp.accent_color,
            hover_color = cp.second_color,
            command = lambda: print('Dienst Neustart'))
        reset_button.place(x=8,y=540)

        term_button = ctk.CTkButton(
            self.window, 
            text = 'Dienst Beenden',
            width=180,
            height=32,
            fg_color = cp.delete_color, 
            text_color = '#000',
            hover_color = cp.delete_color_addition,
            command = lambda: print('Dienst Beenden'))
        term_button.place(x=8,y=590)

        # Toggle layout
        toggle_frame = ctk.CTkFrame(self.window)
        task_toggle = ctk.CTkCheckBox(toggle_frame, text = 'task1')

        toggle_frame.place(x=8, y=220)

        self.window.mainloop()

    def relative_to_assets(self, path: str) -> Path:
        ASSETS_PATH = Path(os.getcwd() + r"/data/assets/main_screen")
        return ASSETS_PATH / Path(path)

    def add_task(self, frame, task):
        menu_toggle = ctk.CTkCheckBox(frame, text=task)
        menu_toggle.pack(fill='x')
    
    def delete_task(self, frame):
        if frame.winfo_children():
            last_toggle = frame.winfo_children()[-1]
            last_toggle.destroy()
