# Import necessary libraries and modules
import customtkinter as ctk
import _color_palette as cp
import os
import sys

# Set the path for custom modules
sys.path.append(os.getcwd() + r"/data/logic/")

# Import the screen logic module
import screen_logic as sl

# Create the main application window
class MainScreen:
    def __init__(self):
        # Initialize the main window
        self.window = ctk.CTk()
        self.window.geometry("1200x680")
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
            command=lambda: print('Run'))
        run_button.place(x=8, y=100)

        add_button = ctk.CTkButton(
            self.window, 
            text='Add Task',
            width=180,
            height=32,
            fg_color=cp.main_color, 
            text_color=cp.accent_color,
            hover_color=cp.second_color,
            command=lambda: self.add(toggle_frame=toggle_frame))
        add_button.place(x=8, y=140)

        del_button = ctk.CTkButton(
            self.window, 
            text='Delete Task',
            width=180,
            height=32,
            fg_color=cp.main_color, 
            text_color=cp.accent_color,
            hover_color=cp.second_color,
            command=lambda: self.delete(toggle_frame=toggle_frame))
        del_button.place(x=8, y=180)
        
        reset_button = ctk.CTkButton(
            self.window, 
            text='Restart Service',
            width=180,
            height=32,
            fg_color=cp.main_color, 
            text_color=cp.accent_color,
            hover_color=cp.second_color,
            command=lambda: print('Service Restart'))
        reset_button.place(x=8, y=540)

        term_button = ctk.CTkButton(
            self.window, 
            text='Stop Service',
            width=180,
            height=32,
            fg_color=cp.delete_color, 
            text_color='#000',
            hover_color=cp.delete_color_addition,
            command=lambda: sl.logout())
        term_button.place(x=8, y=590)

        # Create a frame for task toggles
        toggle_frame = ctk.CTkFrame(self.window)
        toggle_frame.place(x=8, y=220)

        # Make the window non-resizable and start the main loop
        self.window.resizable(False, False)
        self.window.mainloop()

    # Function to add a new task
    def add(self, toggle_frame):
        if self.max_task > 0:
            sl.add_task(frame=toggle_frame, task=f'Transfer_Status_')
            self.max_task -= 1
        
    # Function to delete a task
    def delete(self, toggle_frame):
        self.max_task += sl.delete_task(toggle_frame)
