from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
import _color_palette as cp

class Dashboard:
    def __init__(self, parent):
        self.parent = parent
        
        self.window = Toplevel(self.parent.window)
        self.fix_width = 1200
        self.fix_height = 680

        self.window.geometry(f"{self.fix_width}x{self.fix_height}")
        self.window.configure(bg=cp.main_color)


        self.canvas = Canvas(
            self.window,
            bg = "#F6FFF8",
            height = 432,
            width = 797,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            115.0,
            81.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#CCE3DE",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=55.0,
            y=30.0,
            width=120.0,
            height=100.0
        )

        self.canvas.create_text(
            56.0,
            45.0,
            anchor="nw",
            text="Tables Synced",
            fill="#6B9080",
            font=("Montserrat Bold", 13 * -1)
        )

        self.canvas.create_text(
            84.0,
            63.0,
            anchor="nw",
            text="350",
            fill="#6B9080",
            font=("Montserrat Bold", 48 * -1)
        )

        self.entry_image_2 = PhotoImage(
            file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            299.0,
            81.0,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#CCE3DE",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(
            x=239.0,
            y=30.0,
            width=120.0,
            height=100.0
        )

        self.canvas.create_text(
            240.0,
            45.0,
            anchor="nw",
            text="Tasks Completed",
            fill="#6B9080",
            font=("Montserrat Bold", 13 * -1)
        )

        self.canvas.create_text(
            266.0,
            63.0,
            anchor="nw",
            text="856",
            fill="#6B9080",
            font=("Montserrat Bold", 48 * -1)
        )

        self.entry_image_3 = PhotoImage(
            file=self.relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            177.0,
            286.0,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            bd=0,
            bg="#CCE3DE",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_3.place(
            x=55.0,
            y=175.0,
            width=244.0,
            height=220.0
        )

        self.entry_image_4 = PhotoImage(
            file=self.relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(
            481.0,
            286.0,
            image=self.entry_image_4
        )
        self.entry_4 = Entry(
            bd=0,
            bg="#CCE3DE",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_4.place(
            x=358.0,
            y=175.0,
            width=246.0,
            height=220.0
        )

        self.entry_image_5 = PhotoImage(
            file=self.relative_to_assets("entry_5.png"))
        self.entry_bg_5 = self.canvas.create_image(
            221.0,
            207.5,
            image=self.entry_image_5
        )
        self.entry_5 = Entry(
            bd=0,
            bg="#5E95FF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_5.place(
            x=219.5,
            y=202.0,
            width=3.0,
            height=9.0
        )

        self.entry_image_6 = PhotoImage(
            file=self.relative_to_assets("entry_6.png"))
        self.entry_bg_6 = self.canvas.create_image(
            221.0,
            230.5,
            image=self.entry_image_6
        )
        self.entry_6 = Entry(
            bd=0,
            bg="#777777",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_6.place(
            x=219.5,
            y=225.0,
            width=3.0,
            height=9.0
        )

        self.canvas.create_text(
            235.0,
            200.0,
            anchor="nw",
            text="Booked",
            fill="#5E95FF",
            font=("Montserrat Bold", 13 * -1)
        )

        self.canvas.create_text(
            235.0,
            222.0,
            anchor="nw",
            text="Vacant",
            fill="#5E95FF",
            font=("Montserrat Bold", 13 * -1)
        )

        self.entry_image_7 = PhotoImage(
            file=self.relative_to_assets("entry_7.png"))
        self.entry_bg_7 = self.canvas.create_image(
            483.0,
            81.0,
            image=self.entry_image_7
        )
        self.entry_7 = Entry(
            bd=0,
            bg="#CCE3DE",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_7.place(
            x=423.0,
            y=30.0,
            width=120.0,
            height=100.0
        )

        self.canvas.create_text(
            424.0,
            45.0,
            anchor="nw",
            text="Last Sync",
            fill="#6B9080",
            font=("Montserrat Bold", 13 * -1)
        )

        self.canvas.create_text(
            420.0,
            63.0,
            anchor="nw",
            text="14:35",
            fill="#6B9080",
            font=("Montserrat Bold", 48 * -1)
        )

        self.entry_image_8 = PhotoImage(
            file=self.relative_to_assets("entry_8.png"))
        self.entry_bg_8 = self.canvas.create_image(
            667.0,
            81.0,
            image=self.entry_image_8
        )
        self.entry_8 = Entry(
            bd=0,
            bg="#CCE3DE",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_8.place(
            x=607.0,
            y=30.0,
            width=120.0,
            height=100.0
        )

        self.canvas.create_text(
            608.0,
            45.0,
            anchor="nw",
            text="Average Runtime",
            fill="#6B9080",
            font=("Montserrat Bold", 13 * -1)
        )

        self.canvas.create_text(
            601.0,
            63.0,
            anchor="nw",
            text="31 m.",
            fill="#6B9080",
            font=("Montserrat Bold", 48 * -1)
        )

        self.entry_image_9 = PhotoImage(
            file=self.relative_to_assets("entry_9.png"))
        self.entry_bg_9 = self.canvas.create_image(
            391.0,
            150.0,
            image=self.entry_image_9
        )
        self.entry_9 = Entry(
            bd=0,
            bg="#EFEFEF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_9.place(
            x=41.0,
            y=149.0,
            width=700.0,
            height=0.0
        )

        self.canvas.create_text(
            56.0,
            191.0,
            anchor="nw",
            text="Lorem",
            fill="#6B9080",
            font=("Montserrat Bold", 26 * -1)
        )

        self.canvas.create_text(
            56.0,
            223.0,
            anchor="nw",
            text="Status",
            fill="#6B9080",
            font=("Montserrat Bold", 18 * -1)
        )

        self.canvas.create_text(
            359.0,
            223.0,
            anchor="nw",
            text="By Type",
            fill="#6B9080",
            font=("Montserrat Bold", 18 * -1)
        )

        self.canvas.create_text(
            359.0,
            191.0,
            anchor="nw",
            text="Lorem",
            fill="#6B9080",
            font=("Montserrat Bold", 26 * -1)
        )

        self.canvas.create_rectangle(
            57.0,
            250.0,
            276.0,
            383.0,
            fill="#CCE3DE",
            outline="")

        self.canvas.create_rectangle(
            359.0,
            250.0,
            577.0,
            383.0,
            fill="#CCE3DE",
            outline="")

        self.canvas.create_rectangle(
            74.306396484375,
            234.8228759765625,
            245.517578125,
            404.38720703125,
            fill="#000000",
            outline="")

        self.entry_image_10 = PhotoImage(
            file=self.relative_to_assets("entry_10.png"))
        self.entry_bg_10 = self.canvas.create_image(
            251.0,
            218.5,
            image=self.entry_image_10
        )
        self.entry_10 = Entry(
            bd=0,
            bg="#CCE3DE",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_10.place(
            x=219.0,
            y=186.0,
            width=64.0,
            height=63.0
        )

        self.entry_image_11 = PhotoImage(
            file=self.relative_to_assets("entry_11.png"))
        self.entry_bg_11 = self.canvas.create_image(
            221.0,
            207.5,
            image=self.entry_image_11
        )
        self.entry_11 = Entry(
            bd=0,
            bg="#6B9080",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_11.place(
            x=219.5,
            y=202.0,
            width=3.0,
            height=9.0
        )

        self.entry_image_12 = PhotoImage(
            file=self.relative_to_assets("entry_12.png"))
        self.entry_bg_12 = self.canvas.create_image(
            221.0,
            230.5,
            image=self.entry_image_12
        )
        self.entry_12 = Entry(
            bd=0,
            bg="#777777",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_12.place(
            x=219.5,
            y=225.0,
            width=3.0,
            height=9.0
        )

        self.canvas.create_text(
            235.0,
            200.0,
            anchor="nw",
            text="Lorem",
            fill="#6B9080",
            font=("Montserrat Bold", 13 * -1)
        )

        self.canvas.create_text(
            235.0,
            222.0,
            anchor="nw",
            text="Ipsum",
            fill="#6B9080",
            font=("Montserrat Bold", 13 * -1)
        )

        self.entry_image_13 = PhotoImage(
            file=self.relative_to_assets("entry_13.png"))
        self.entry_bg_13 = self.canvas.create_image(
            555.693603515625,
            218.5,
            image=self.entry_image_13
        )
        self.entry_13 = Entry(
            bd=0,
            bg="#CCE3DE",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_13.place(
            x=523.693603515625,
            y=186.0,
            width=64.0,
            height=63.0
        )

        self.canvas.create_rectangle(
            376.036376953125,
            232.19482421875,
            551.39892578125,
            407.55731201171875,
            fill="#000000",
            outline="")

        self.entry_image_14 = PhotoImage(
            file=self.relative_to_assets("entry_14.png"))
        self.entry_bg_14 = self.canvas.create_image(
            525.693603515625,
            207.5,
            image=self.entry_image_14
        )
        self.entry_14 = Entry(
            bd=0,
            bg="#6B9080",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_14.place(
            x=524.193603515625,
            y=202.0,
            width=3.0,
            height=9.0
        )

        self.entry_image_15 = PhotoImage(
            file=self.relative_to_assets("entry_15.png"))
        self.entry_bg_15 = self.canvas.create_image(
            525.693603515625,
            230.5,
            image=self.entry_image_15
        )
        self.entry_15 = Entry(
            bd=0,
            bg="#777777",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_15.place(
            x=524.193603515625,
            y=225.0,
            width=3.0,
            height=9.0
        )

        self.canvas.create_text(
            539.693603515625,
            200.0,
            anchor="nw",
            text="Lorem",
            fill="#6B9080",
            font=("Montserrat Bold", 13 * -1)
        )

        self.canvas.create_text(
            539.693603515625,
            222.0,
            anchor="nw",
            text="Normal",
            fill="#6B9080",
            font=("Montserrat Bold", 13 * -1)
        )
        self.window.resizable(False, False)

    def relative_to_assets(self, path: str) -> Path:
        ASSETS_PATH = Path(r"C:\Users\Joao.Antonio\Desktop\Projekte\task-handling-tool\data\assets\frame0")
        return ASSETS_PATH / Path(path)
    