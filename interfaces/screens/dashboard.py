
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Joao.Antonio\Desktop\Neuer Ordner\build\assets\frame2")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("797x432")
window.configure(bg = "#F6FFF8")


canvas = Canvas(
    window,
    bg = "#F6FFF8",
    height = 432,
    width = 797,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    115.0,
    81.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#CCE3DE",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=55.0,
    y=30.0,
    width=120.0,
    height=100.0
)

canvas.create_text(
    56.0,
    45.0,
    anchor="nw",
    text="Tables Synced",
    fill="#6B9080",
    font=("Montserrat Bold", 13 * -1)
)

canvas.create_text(
    84.0,
    63.0,
    anchor="nw",
    text="350",
    fill="#6B9080",
    font=("Montserrat Bold", 48 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    299.0,
    81.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#CCE3DE",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=239.0,
    y=30.0,
    width=120.0,
    height=100.0
)

canvas.create_text(
    240.0,
    45.0,
    anchor="nw",
    text="Tasks Completed",
    fill="#6B9080",
    font=("Montserrat Bold", 13 * -1)
)

canvas.create_text(
    266.0,
    63.0,
    anchor="nw",
    text="856",
    fill="#6B9080",
    font=("Montserrat Bold", 48 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    177.0,
    286.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#CCE3DE",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=55.0,
    y=175.0,
    width=244.0,
    height=220.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    481.0,
    286.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#CCE3DE",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=358.0,
    y=175.0,
    width=246.0,
    height=220.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    221.0,
    207.5,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#5E95FF",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=219.5,
    y=202.0,
    width=3.0,
    height=9.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    221.0,
    230.5,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#777777",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=219.5,
    y=225.0,
    width=3.0,
    height=9.0
)

canvas.create_text(
    235.0,
    200.0,
    anchor="nw",
    text="Booked",
    fill="#5E95FF",
    font=("Montserrat Bold", 13 * -1)
)

canvas.create_text(
    235.0,
    222.0,
    anchor="nw",
    text="Vacant",
    fill="#5E95FF",
    font=("Montserrat Bold", 13 * -1)
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    483.0,
    81.0,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#CCE3DE",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=423.0,
    y=30.0,
    width=120.0,
    height=100.0
)

canvas.create_text(
    424.0,
    45.0,
    anchor="nw",
    text="Last Sync",
    fill="#6B9080",
    font=("Montserrat Bold", 13 * -1)
)

canvas.create_text(
    420.0,
    63.0,
    anchor="nw",
    text="14:35",
    fill="#6B9080",
    font=("Montserrat Bold", 48 * -1)
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    667.0,
    81.0,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#CCE3DE",
    fg="#000716",
    highlightthickness=0
)
entry_8.place(
    x=607.0,
    y=30.0,
    width=120.0,
    height=100.0
)

canvas.create_text(
    608.0,
    45.0,
    anchor="nw",
    text="Average Runtime",
    fill="#6B9080",
    font=("Montserrat Bold", 13 * -1)
)

canvas.create_text(
    601.0,
    63.0,
    anchor="nw",
    text="31 m.",
    fill="#6B9080",
    font=("Montserrat Bold", 48 * -1)
)

entry_image_9 = PhotoImage(
    file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(
    391.0,
    150.0,
    image=entry_image_9
)
entry_9 = Entry(
    bd=0,
    bg="#EFEFEF",
    fg="#000716",
    highlightthickness=0
)
entry_9.place(
    x=41.0,
    y=149.0,
    width=700.0,
    height=0.0
)

canvas.create_text(
    56.0,
    191.0,
    anchor="nw",
    text="Lorem",
    fill="#6B9080",
    font=("Montserrat Bold", 26 * -1)
)

canvas.create_text(
    56.0,
    223.0,
    anchor="nw",
    text="Status",
    fill="#6B9080",
    font=("Montserrat Bold", 18 * -1)
)

canvas.create_text(
    359.0,
    223.0,
    anchor="nw",
    text="By Type",
    fill="#6B9080",
    font=("Montserrat Bold", 18 * -1)
)

canvas.create_text(
    359.0,
    191.0,
    anchor="nw",
    text="Lorem",
    fill="#6B9080",
    font=("Montserrat Bold", 26 * -1)
)

canvas.create_rectangle(
    57.0,
    250.0,
    276.0,
    383.0,
    fill="#CCE3DE",
    outline="")

canvas.create_rectangle(
    359.0,
    250.0,
    577.0,
    383.0,
    fill="#CCE3DE",
    outline="")

canvas.create_rectangle(
    74.306396484375,
    234.8228759765625,
    245.517578125,
    404.38720703125,
    fill="#000000",
    outline="")

entry_image_10 = PhotoImage(
    file=relative_to_assets("entry_10.png"))
entry_bg_10 = canvas.create_image(
    251.0,
    218.5,
    image=entry_image_10
)
entry_10 = Entry(
    bd=0,
    bg="#CCE3DE",
    fg="#000716",
    highlightthickness=0
)
entry_10.place(
    x=219.0,
    y=186.0,
    width=64.0,
    height=63.0
)

entry_image_11 = PhotoImage(
    file=relative_to_assets("entry_11.png"))
entry_bg_11 = canvas.create_image(
    221.0,
    207.5,
    image=entry_image_11
)
entry_11 = Entry(
    bd=0,
    bg="#6B9080",
    fg="#000716",
    highlightthickness=0
)
entry_11.place(
    x=219.5,
    y=202.0,
    width=3.0,
    height=9.0
)

entry_image_12 = PhotoImage(
    file=relative_to_assets("entry_12.png"))
entry_bg_12 = canvas.create_image(
    221.0,
    230.5,
    image=entry_image_12
)
entry_12 = Entry(
    bd=0,
    bg="#777777",
    fg="#000716",
    highlightthickness=0
)
entry_12.place(
    x=219.5,
    y=225.0,
    width=3.0,
    height=9.0
)

canvas.create_text(
    235.0,
    200.0,
    anchor="nw",
    text="Lorem",
    fill="#6B9080",
    font=("Montserrat Bold", 13 * -1)
)

canvas.create_text(
    235.0,
    222.0,
    anchor="nw",
    text="Ipsum",
    fill="#6B9080",
    font=("Montserrat Bold", 13 * -1)
)

entry_image_13 = PhotoImage(
    file=relative_to_assets("entry_13.png"))
entry_bg_13 = canvas.create_image(
    555.693603515625,
    218.5,
    image=entry_image_13
)
entry_13 = Entry(
    bd=0,
    bg="#CCE3DE",
    fg="#000716",
    highlightthickness=0
)
entry_13.place(
    x=523.693603515625,
    y=186.0,
    width=64.0,
    height=63.0
)

canvas.create_rectangle(
    376.036376953125,
    232.19482421875,
    551.39892578125,
    407.55731201171875,
    fill="#000000",
    outline="")

entry_image_14 = PhotoImage(
    file=relative_to_assets("entry_14.png"))
entry_bg_14 = canvas.create_image(
    525.693603515625,
    207.5,
    image=entry_image_14
)
entry_14 = Entry(
    bd=0,
    bg="#6B9080",
    fg="#000716",
    highlightthickness=0
)
entry_14.place(
    x=524.193603515625,
    y=202.0,
    width=3.0,
    height=9.0
)

entry_image_15 = PhotoImage(
    file=relative_to_assets("entry_15.png"))
entry_bg_15 = canvas.create_image(
    525.693603515625,
    230.5,
    image=entry_image_15
)
entry_15 = Entry(
    bd=0,
    bg="#777777",
    fg="#000716",
    highlightthickness=0
)
entry_15.place(
    x=524.193603515625,
    y=225.0,
    width=3.0,
    height=9.0
)

canvas.create_text(
    539.693603515625,
    200.0,
    anchor="nw",
    text="Lorem",
    fill="#6B9080",
    font=("Montserrat Bold", 13 * -1)
)

canvas.create_text(
    539.693603515625,
    222.0,
    anchor="nw",
    text="Normal",
    fill="#6B9080",
    font=("Montserrat Bold", 13 * -1)
)
window.resizable(False, False)
window.mainloop()
