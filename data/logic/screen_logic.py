import os
from pathlib import Path
from tkinter import messagebox
import customtkinter as ctk

max_task = 13

def logout(window):
    confirm = messagebox.askyesno(
        "Confirm log-out", "Do you really want to log out?"
    )
    if confirm == True:
        window.destroy()
        # window = ls.LoginScreen()
        # window.window.mainloop()

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