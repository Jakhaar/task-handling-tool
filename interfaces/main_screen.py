# Import necessary libraries and modules
import time
import customtkinter as ctk
import _color_palette as cp
import os
import sys
import initialization_screen as ini
from datetime import datetime

# Set the path for custom modules
sys.path.append(os.getcwd() + r"/data/logic/")
import screen_logic as sl

# Create the main application window
class MainScreen:
    def __init__(self):
        # Initialize the main window
        self.window = ctk.CTk()
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        window_width = 1200  
        window_height = 680  

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.window.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.window.title('EXCHANGE')
        self.window.configure(bg=cp.background_color)

        # Initialize the task list and maximum task count
        self.task_list = []
        self.max_task = 13
        
        # Create buttons for various actions
        run_button = ctk.CTkButton(
            self.window, 
            text='Run Task',
            width=180,
            height=32,
            fg_color=cp.main_color, 
            text_color=cp.accent_color,
            hover_color=cp.second_color,
            command=lambda: sl.insert_text(self.text_widget, f'{datetime.now().strftime("%H:%M:%S")} Beginne mit iAgent Sync..'))
        run_button.place(x=8, y=100)

        add_button = ctk.CTkButton(
            self.window, 
            text='Add Task',
            width=180,
            height=32,
            fg_color=cp.main_color, 
            text_color=cp.accent_color,
            hover_color=cp.second_color,
            command=lambda: self.add_task(toggle_frame=toggle_frame))
        add_button.place(x=8, y=140)

        del_button = ctk.CTkButton(
            self.window, 
            text='Delete Task',
            width=180,
            height=32,
            fg_color=cp.main_color, 
            text_color=cp.accent_color,
            hover_color=cp.second_color,
            command=lambda: self.delete_task(toggle_frame=toggle_frame))
        del_button.place(x=8, y=180)
        
        reset_button = ctk.CTkButton(
            self.window, 
            text='Restart Service',
            width=180,
            height=32,
            fg_color=cp.main_color, 
            text_color=cp.accent_color,
            hover_color=cp.second_color,
            command=lambda:sl.restart_service(ini.InitializationScreen))
        reset_button.place(x=8, y=540)

        term_button = ctk.CTkButton(
            self.window, 
            text='Stop Service',
            width=180,
            height=32,
            fg_color=cp.delete_color, 
            text_color='#000',
            hover_color=cp.delete_color_addition,
            command=lambda: sl.terminate_service(self.window))
        term_button.place(x=8, y=590)

        # Create a frame for task toggles
        toggle_frame = ctk.CTkFrame(self.window)
        toggle_frame.place(x=8, y=220)

        logger_frame = ctk.CTkFrame(self.window, width=900, height=600)
        logger_frame.place(x=250, y=50)

        self.text_widget = ctk.CTkTextbox(logger_frame, wrap='none', width=900, height=600)
        self.text_widget.pack(fill='both', expand=True)

        # Disable text editing if needed
        self.text_widget.configure(state='disabled')

        # Make the window non-resizable and start the main loop
        self.window.resizable(False, False)

    # Function to add a new task
    def add_task(self, toggle_frame):
        try:
            if self.max_task > 0:
                task_path = sl.open_file_dialog()
                sl.add_task(frame=toggle_frame, task_name=os.path.basename(task_path))
                self.max_task -= 1
        except:
            pass
        
    # Function to delete a task
    def delete_task(self, toggle_frame):
        self.max_task += sl.delete_task(toggle_frame)


if __name__ == '__main__':
    obj = MainScreen()
    obj.window.mainloop()