from pathlib import Path
from tkinter import Tk
import customtkinter as ctk
import os
import _color_palette as cp

class MainScreen:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.geometry("1200x680")
        self.window.title('EXCHANGE')
        self.window.configure(bg=cp.background_color)

        string_var = ctk.StringVar(value = 'a custom string')
        
        add_button = ctk.CTkButton(
            self.window, 
            text = 'Hizufügen',
            width=180,
            height=32,
            fg_color = cp.main_color, 
            text_color = cp.accent_color,
            hover_color = cp.second_color,
            command = lambda: print('Added'))
        add_button.place(x=8,y=140)

        del_button = ctk.CTkButton(
            self.window, 
            text = 'Hizufügen',
            width=180,
            height=32,
            fg_color = cp.main_color, 
            text_color = cp.accent_color,
            hover_color = cp.second_color,
            command = lambda: print('Delete'))
        del_button.place(x=8,y=180)

        self.window.mainloop()


    def relative_to_assets(self, path: str) -> Path:
        ASSETS_PATH = Path(os.getcwd() + r"/data/assets/main_screen")
        return ASSETS_PATH / Path(path)
    





        # self.canvas = Canvas(
        #     self.window,
        #     bg="#6B9080",
        #     height=680,
        #     width=1200,
        #     bd=0,
        #     highlightthickness=0,
        #     relief="ridge"
        # )
        # self.canvas.place(x=0, y=0)

        # self.canvas.create_rectangle(
        #     215.0,
        #     0.0,
        #     1200.0,
        #     680.0,
        #     fill="#F6FFF8",
        #     outline=""
        # )

        # self.canvas.create_rectangle(
        #     317.0,
        #     108.0,
        #     1094.0,
        #     514.0,
        #     fill="#CCE3DE",
        #     outline=""
        # )

        # self.button_image_2 = PhotoImage(
        #     file=self.relative_to_assets("button_2.png"))
        # self.button_2 = Button(
        #     self.canvas,
        #     image=self.button_image_2,
        #     borderwidth=0,
        #     highlightthickness=0,
        #     command=lambda: print("button_2 clicked"),
        #     relief="flat"
        # )
        # self.button_2.place(
        #     x=8.0,
        #     y=141.0,
        #     width=183.0,
        #     height=32.0
        # )

        # self.button_image_3 = PhotoImage(
        #     file=self.relative_to_assets("button_3.png"))
        # self.button_3 = Button(
        #     self.canvas,
        #     image=self.button_image_3,
        #     borderwidth=0,
        #     highlightthickness=0,
        #     command=lambda: print("button_3 clicked"),
        #     relief="flat"
        # )
        # self.button_3.place(
        #     x=8.0,
        #     y=188.0,
        #     width=180.0,
        #     height=32.0
        # )

        # self.button_image_logout = PhotoImage(
        #     file=self.relative_to_assets("button_4.png"))
        # self.button_logout = Button(
        #     self.canvas,
        #     image=self.button_image_logout,
        #     borderwidth=0,
        #     highlightthickness=0,
        #     command=lambda: print("button_4 clicked"),
        #     relief="flat"
        # )
        # self.button_logout.place(
        #     x=8.0,
        #     y=387.0,
        #     width=180.0,
        #     height=40.0
        # )

        # self.canvas.create_text(
        #     255.0,
        #     33.0,
        #     anchor="nw",
        #     text="Dashboard",
        #     fill="#6B9080",
        #     font=("Montserrat Bold", 26 * -1)
        # )

        # self.canvas.create_rectangle(
        #     60.0,
        #     18.0,
        #     150.0,
        #     108.0,
        #     fill="#FFFFFF",
        #     outline=""
        # )
        # self.window.resizable(False, False)
