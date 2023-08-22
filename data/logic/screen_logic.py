from tkinter import messagebox
import login_screen as ls

def logout(window):
    confirm = messagebox.askyesno(
        "Confirm log-out", "Do you really want to log out?"
    )
    if confirm == True:
        window.destroy()
        window = ls.LoginScreen()
        window.window.mainloop()

def handle_btn_press(window):
    # window.forget()

    # match screen:
    #     case 'dash':
    #         pass
    #     case 'dash':
    #         pass
    #     case 'dash':
    #         pass
    print(window)
    