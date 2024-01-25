import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
from datetime import timedelta, datetime
from daily_work_logger import DailyWorkLogger  # Import DailyWorkLogger class from daily_work_logger.py
from database_manager import DatabaseManager  # Import DatabaseManager class

class PomodoroTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("Pomodoro Timer")

        # Time durations for Pomodoro and break
        self.pomodoro_time = timedelta(minutes=25)
        self.break_time = timedelta(minutes=5)
        self.time_remaining = self.pomodoro_time
        self.timer_running = False

        # Set a background color for the window
        self.master.configure(bg="#F0F0F0")

        # Label with larger and bold font for the timer
        self.label = tk.Label(master, font=('Arial', 60, 'bold'), text=self.format_time(self.time_remaining), fg="#2E4057", bg="#F0F0F0")
        self.label.pack(pady=20)

        # Progressbar with a different color
        self.progressbar = ttk.Progressbar(master, variable=tk.DoubleVar(), maximum=self.pomodoro_time.seconds, length=400, mode='determinate', orient=tk.HORIZONTAL, style="TProgressbar")
        self.progressbar.pack(pady=10)

        # Define a custom style for the ttk.Progressbar
        self.master.style = ttk.Style()
        self.master.style.theme_use('default')
        self.master.style.configure("TProgressbar", thickness=30, troughcolor="#F0F0F0", background="#2E4057")

        # Stylish start button
        self.start_button = tk.Button(master, text="Start Pomodoro", command=self.start_pomodoro, bg="green", fg="white", font=('Arial', 14, 'bold'), relief=tk.FLAT)
        self.start_button.pack(pady=10)

        # Stylish break button
        self.break_button = tk.Button(master, text="Start Break", command=self.start_break, state=tk.DISABLED, bg="blue", fg="white", font=('Arial', 14, 'bold'), relief=tk.FLAT)
        self.break_button.pack(pady=10)

        # Stop button to stop the current timer
        self.stop_button = tk.Button(master, text="Stop", command=self.stop_timer, state=tk.DISABLED, bg="red", fg="white", font=('Arial', 14, 'bold'), relief=tk.FLAT)
        self.stop_button.pack(pady=10)

        # # Button to log daily work with date and day
        # self.log_button = tk.Button(master, text="Log Daily Work", command=self.log_daily_work, bg="#34495e", fg="white", font=('Arial', 14, 'bold'), relief=tk.FLAT)
        # self.log_button.pack(pady=10)

        # Display current date and day
        self.date_label = tk.Label(master, text=self.get_current_date(), font=('Arial', 12), fg="#2E4057", bg="#F0F0F0")
        self.date_label.pack()

        # Initialize the clock function
        self.clock()

        # Create an instance of DailyWorkLogger
        self.daily_work_logger = DailyWorkLogger(master)

        # Create an instance of DatabaseManager
        self.database_manager = DatabaseManager()

        # Button to show all logs
        self.show_logs_button = tk.Button(master, text="Show All Logs", command=self.show_all_logs, bg="#3498db",
                                          fg="white", font=('Arial', 14, 'bold'), relief=tk.FLAT)
        self.show_logs_button.pack(pady=10)

    # Show all logs : date and description with sequence
    def show_all_logs(self):
        # Fetch all logs from the database
        logs = self.database_manager.fetch_all_logs()

        if not logs:
            messagebox.showinfo("No Logs", "No daily work logs available.")
            return

        # Create a new window to display the logs
        log_window = tk.Toplevel(self.master)
        log_window.title("Daily Work Logs")

        # Create a text widget to display logs
        log_text = tk.Text(log_window, height=20, width=50, wrap=tk.WORD)
        log_text.pack(padx=10, pady=10)

        # Insert logs into the text widget
        for log in logs:
            log_text.insert(tk.END,
                            f"{log[0]} {log[1]}: {log[2]}\n")  # Assuming column 1 is id, column 2 is date, column 3 is time, and column 4 is work_description

    def clock(self):
        # Function to update the timer every second
        if self.timer_running:
            self.time_remaining -= timedelta(seconds=1)
            self.progressbar["value"] = self.pomodoro_time.seconds - self.time_remaining.seconds

            if self.time_remaining <= timedelta(0):
                # Pomodoro or break completed
                self.timer_running = False
                self.start_button.config(state=tk.NORMAL, bg="#4CAF50")
                self.break_button.config(state=tk.NORMAL, bg="#3498db")
                self.stop_button.config(state=tk.DISABLED, bg="#e74c3c")
                self.label.config(text="Pomodoro Completed!", fg="#4CAF50")
                self.master.bell()  # Beep to alert user
                self.master.after(1000, self.reset_timer)
            else:
                # Update the timer display
                self.label.config(text=self.format_time(self.time_remaining))
        self.master.after(1000, self.clock)

    def start_pomodoro(self):
        # Function to start the Pomodoro timer
        if not self.timer_running:
            self.timer_running = True
            self.start_button.config(state=tk.DISABLED, bg="#95a5a6")
            self.break_button.config(state=tk.NORMAL, bg="#3498db")
            self.stop_button.config(state=tk.NORMAL, bg="#e74c3c")
            self.time_remaining = self.pomodoro_time
            self.label.config(text=self.format_time(self.time_remaining), fg="#2E4057")

    def start_break(self):
        # Function to start the break timer
        if not self.timer_running:
            self.timer_running = True
            self.start_button.config(state=tk.DISABLED, bg="#95a5a6")
            self.break_button.config(state=tk.DISABLED, bg="#95a5a6")
            self.stop_button.config(state=tk.NORMAL, bg="#e74c3c")
            self.time_remaining = self.break_time
            self.label.config(text=self.format_time(self.time_remaining), fg="#3498db")
            self.master.after(self.break_time.seconds * 1000, self.break_completed)

    def stop_timer(self):
        # Function to stop the current timer
        self.timer_running = False
        self.start_button.config(state=tk.NORMAL, bg="#4CAF50")
        self.break_button.config(state=tk.NORMAL, bg="#3498db")
        self.stop_button.config(state=tk.DISABLED, bg="#e74c3c")
        self.master.after(1000, self.reset_timer)

    def break_completed(self):
        # Function called when the break is completed
        self.timer_running = False
        self.start_button.config(state=tk.NORMAL, bg="#4CAF50")
        self.label.config(text="Break Completed!", fg="#3498db")
        self.master.bell()  # Beep to alert user
        self.master.after(1000, self.reset_timer)

    def reset_timer(self):
        # Function to reset the timer for the next Pomodoro
        self.time_remaining = self.pomodoro_time
        self.label.config(text=self.format_time(self.time_remaining), fg="#2E4057")
        self.progressbar["value"] = 0

    def log_daily_work(self):
        # Call the log_daily_work method from DailyWorkLogger
        # self.daily_work_logger.log_daily_work()

        # Call the save_daily_work_log method from DatabaseManager
        work_description = simpledialog.askstring("Daily Work Log", "Enter your daily work:")
        if work_description:
            self.database_manager.save_daily_work_log(work_description)

    @staticmethod
    def format_time(time_delta):
        # Helper function to format time in MM:SS
        minutes, seconds = divmod(time_delta.seconds, 60)
        return f"{minutes:02}:{seconds:02}"

    def get_current_date(self):
        # Helper function to get the current date and day
        current_datetime = datetime.now()
        current_date = current_datetime.strftime("%Y-%m-%d")
        current_day = current_datetime.strftime("%A")
        return f"Date: {current_date} | Day: {current_day}"


root = tk.Tk()
app = PomodoroTimer(root)
root.mainloop()