import os
import sys
from pathlib import Path
from tkinter import messagebox
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

max_task = 13

def check_service() -> None:
    pass

def terminate_service(window):
    msg = CTkMessagebox(title="Dienst Beenden?", message="Soll der Dienst wirklich beendet werden?", icon='warning', option_1="Nein", option_2="Ja")
    response = msg.get()
    
    if response=="Ja":
        window.destroy()
    else:
        pass

def restart_service(window):
    msg = CTkMessagebox(title="Dienst Neustarten?", message="Soll der Dienst neugestartet werden?", icon='question', option_1="Nein", option_2="Ja")
    response = msg.get()
    
    if response=="Ja":
        window.destroy()
        #TODO: Call Service initialization Window
    else:
        pass

def relative_to_assets(self, path: str) -> Path:
    ASSETS_PATH = Path(os.getcwd() + r"/data/assets/main_screen")
    return ASSETS_PATH / Path(path)

def add_task(frame, task):
    task_checkbox = ctk.CTkCheckBox(frame, text=task)
    task_checkbox.pack(fill='x')

def delete_task(frame) -> int:
    selected_checkboxes = []

    for widget in frame.winfo_children():
        if isinstance(widget, ctk.CTkCheckBox) and widget.get() == 1:
            selected_checkboxes.append(widget)

    for checkbox in selected_checkboxes:
        checkbox.destroy()

    return len(selected_checkboxes)