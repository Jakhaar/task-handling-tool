import os
import random
import sys
from pathlib import Path
from tkinter import messagebox
from CTkMessagebox import CTkMessagebox
import customtkinter as ctk
import time

max_task = 13
random_texts = ["Text 1", "Text 2", "Text 3", "Random Text"]

def insert_text(text_widget, new_text): 
    # Get the current text from the text widget
    current_text = text_widget.get('1.0', 'end')

    # Append the new text with a newline character
    updated_text = new_text + '\n' + current_text

    # Clear the text widget and insert the updated text
    text_widget.configure(state='normal')
    text_widget.delete('1.0', 'end')
    text_widget.insert('1.0', updated_text)
    text_widget.configure(state='disabled')


def check_service() -> None:
    pass

def terminate_service(window) -> None:
    msg = CTkMessagebox(title="Dienst Beenden?", message="Soll der Dienst wirklich beendet werden?", icon='warning', option_1="Nein", option_2="Ja")
    response = msg.get()
    
    if response=="Ja":
        window.destroy()
    else:
        pass

def restart_service(window) -> None:
    msg = CTkMessagebox(title="Dienst Neustarten?", message="Soll der Dienst neugestartet werden?", icon='question', option_1="Nein", option_2="Ja")
    response = msg.get()
    
    if response=="Ja":
        #TODO: Delete the Service
        window("Der Dienst wird Beendet...").window.mainloop()

        #TODO: Call Service initialization Window
        # window("Der Dienst wird Initialisiert...").window.mainloop()

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
