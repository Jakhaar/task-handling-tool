import sys
sys.path.append(r'C:\Users\Joao.Antonio\Desktop\Projekte\task-handling-tool\interfaces\screens')

from login_screen import LoginScreen as ls
from tkinter import Tk, Canvas, Entry, Button, PhotoImage

if __name__ == "__main__":
    login_app = ls.LoginScreen()
    login_app.window.mainloop()