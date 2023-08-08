from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import _color_palette as cp

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Joao.Antonio\Desktop\Projekte\task-handling-tool\data\assets\frame0")
password = 'Ham'

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def checkLogin():
    if entry_password.get() == password:
        print('JA')
    else: print('ne')

window = Tk()
fix_width = 1200
fix_height = 680

window.geometry(f"{fix_width}x{fix_height}")
window.configure(bg = cp.main_color)

canvas = Canvas(
    window,
    bg = cp.main_color,
    height = 680,
    width = 1200,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    195.0,
    86.0,
    1005.0,
    805.0,
    fill=cp.accent_color_addition,
    outline="")

entry_image = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg = canvas.create_image(
    603.897216796875,
    339.72332763671875,
    image=entry_image
)
entry_password = Entry(
    bd=0,
    bg=cp.accent_color,
    fg="#000716",
    highlightthickness=0
)
entry_password.place(
    x=377.0,
    y=290.0,
    width=453.79443359375,
    height=97.4466552734375
)

canvas.create_text(
    389.2727355957031,
    308.814208984375,
    anchor="nw",
    text="Password",
    fill="#6B9080",
    font=("Montserrat Bold", 14 * -1)
)

canvas.create_text(
    357.0,
    164.0,
    anchor="nw",
    text="Entsperren",
    fill="#6B9080",
    font=("Montserrat Bold", 32 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=checkLogin,
    relief="flat"
)
button_1.place(
    x=538.0,
    y=484.0,
    width=123.11282348632812,
    height=95.91534423828125
)

canvas.create_text(
    358.0,
    209.0,
    anchor="nw",
    text="um Ihre Aufgaben zu sehen",
    fill="#A4C3B2",
    font=("Montserrat SemiBold", 20 * -1)
)

canvas.create_text(
    389.522216796875,
    332.7003173828125,
    anchor="nw",
    text="123password",
    fill="#000000",
    font=("Montserrat SemiBold", 32 * -1)
)
window.resizable(False, False)
window.mainloop()