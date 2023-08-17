from pathlib import Path
import time
from tkinter import Tk, Canvas, Entry, Button, PhotoImage
import _color_palette as cp
import main_screen as ms
import os

class LoginScreen:
    def __init__(self):
        self.window = Tk()

        self.fix_width = 1200
        self.fix_height = 680

        self.window.geometry(f"{self.fix_width}x{self.fix_height}")
        self.window.configure(bg=cp.main_color)

        self.canvas = Canvas(
            self.window,
            bg=cp.main_color,
            height=self.fix_height,
            width=self.fix_width,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(
            195.0,
            86.0,
            1005.0,
            805.0,
            fill=cp.accent_color_addition,
            outline=""
        )

        self.entry_image = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        self.entry_bg = self.canvas.create_image(
            603.897216796875,
            339.72332763671875,
            image=self.entry_image
        )

        self.entry_password = Entry(
            bd=0,
            bg=cp.accent_color,
            fg="#000716",
            highlightthickness=0
        )
        self.entry_password.place(
            x=377.0,
            y=290.0,
            width=453.79443359375,
            height=97.4466552734375
        )

        self.canvas.create_text(
            389.2727355957031,
            308.814208984375,
            anchor="nw",
            text="Password",
            fill="#6B9080",
            font=("Montserrat Bold", 14 * -1)
        )

        self.canvas.create_text(
            357.0,
            164.0,
            anchor="nw",
            text="Entsperren",
            fill="#6B9080",
            font=("Montserrat Bold", 32 * -1)
        )

        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.checkLogin,
            relief="flat"
        )
        self.button_1.place(
            x=538.0,
            y=484.0,
            width=123.11282348632812,
            height=95.91534423828125
        )

        self.canvas.create_text(
            358.0,
            209.0,
            anchor="nw",
            text="um Ihre Aufgaben zu sehen",
            fill="#A4C3B2",
            font=("Montserrat SemiBold", 20 * -1)
        )

        self.canvas.create_text(
            389.522216796875,
            332.7003173828125,
            anchor="nw",
            text="123password",
            fill="#000000",
            font=("Montserrat SemiBold", 32 * -1)
        )
        self.window.resizable(False, False)
        # self.window.mainloop()

    def relative_to_assets(self, path: str) -> Path:
        ASSETS_PATH = Path(os.getcwd() + r"/data/assets/frame0")
        return ASSETS_PATH / Path(path)

    def checkLogin(self):
        if self.entry_password.get() == '':
            #checken ob der Service überhaupt aktiv ist
            self.window.destroy()
            self.openDashboard()
        

    def openDashboard(self):
        obj = ms.MainScreen()
        obj.window.mainloop()        