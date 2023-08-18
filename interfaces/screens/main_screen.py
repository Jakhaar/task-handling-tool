from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import os
import _color_palette as cp
import screen_logic as cs

class MainScreen:
    def __init__(self):
        self.window = Tk()

        self.fix_width = 1200
        self.fix_height = 680

        self.window.geometry(f"{self.fix_width}x{self.fix_height}")
        self.window.configure(bg=cp.main_color)

        self.canvas = Canvas(
            self.window,
            bg=cp.main_color,
            height=680,
            width=1200,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(
            215.0,
            0.0,
            1200.0,
            680.0,
            fill=cp.background_color,
            outline=""
        )

        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: cs.changeScreen(1),
            relief="flat"
        )
        self.button_1.place(
            x=8.0,
            y=141.0,
            width=207.0,
            height=32.0
        )

        self.button_image_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: cs.changeScreen(2),
            relief="flat"
        )
        self.button_2.place(
            x=8.0,
            y=188.0,
            width=207.0,
            height=32.0
        )

        self.button_image_3 = PhotoImage(file=self.relative_to_assets("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: cs.changeScreen(3),
            relief="flat"
        )
        self.button_3.place(
            x=8.0,
            y=235.0,
            width=207.0,
            height=32.0
        )

        self.button_image_4 = PhotoImage(file=self.relative_to_assets("button_4.png"))
        self.button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: cs.changeScreen(4),
            relief="flat"
        )
        self.button_4.place(
            x=8.0,
            y=562.0,
            width=207.0,
            height=32.0
        )

        self.canvas.create_text(
            255.0,
            33.0,
            anchor="nw",
            text="Dashboard",
            fill=cp.main_color,
            font=("Montserrat Bold", 26 * -1)
        )

        self.canvas.create_text(
            844.0,
            43.0,
            anchor="nw",
            text="Administrator",
            fill=cp.main_color,
            font=("Montserrat SemiBold", 16 * -1)
        )

        self.window.resizable(False, False)

    def relative_to_assets(self, path: str) -> Path:
        ASSETS_PATH = Path(os.getcwd() + r"/data/assets/frame1")
        return ASSETS_PATH / Path(path)
    


