import tkinter as tk
from tkinter import simpledialog
from datetime import datetime
from database_manager import DatabaseManager

class DailyWorkLogger:
    def __init__(self, master):
        self.master = master
        self.master.title("Daily Work Log")

        # Set a background color for the window
        self.master.configure(bg="#F0F0F0")

        # Button to log daily work with date and day
        self.log_button = tk.Button(master, text="Log Daily Work", command=self.log_daily_work, bg="#34495e", fg="white", font=('Arial', 14, 'bold'), relief=tk.FLAT)
        self.log_button.pack(pady=10)

        # Create an instance of DatabaseManager
        self.database_manager = DatabaseManager()

    def log_daily_work(self):
        # Function to get user input for daily work log
        work_description = simpledialog.askstring("Daily Work Log", "Enter your daily work:")

        ## This create text file
        # if work_description:
        #     self.save_daily_work_log(work_description)

        ## This store into the database
        if work_description:
            self.database_manager.save_daily_work_log(work_description)

    def save_daily_work_log(self, work_description):
        # Function to save daily work log to a file
        current_date = datetime.now().strftime("%Y-%m-%d")
        log_entry = f"{current_date}: {work_description}\n"

        with open("daily_work_log.txt", "a") as log_file:
            log_file.write(log_entry)


if __name__ == "__main__":
    root = tk.Tk()
    app = DailyWorkLogger(root)
    root.mainloop()