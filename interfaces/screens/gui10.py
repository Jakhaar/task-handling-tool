
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Joao.Antonio\Desktop\Projekte\task_handler\build\build\assets\frame10")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("144x49")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 49,
    width = 144,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    1.0,
    144.0,
    49.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    0.0,
    0.0,
    144.0,
    48.0,
    fill="#6B9080",
    outline="")

canvas.create_text(
    47.0,
    13.0,
    anchor="nw",
    text="Update",
    fill="#FFFFFF",
    font=("Montserrat Bold", 20 * -1)
)

canvas.create_rectangle(
    17.0,
    15.0,
    37.0,
    35.0,
    fill="#FFFFFF",
    outline="")
window.resizable(False, False)
window.mainloop()
