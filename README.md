# StudySync App 📚🔄

Welcome to StudySync, your study companion for efficient time management and collaboration. This application, built using Python and Tkinter, offers a Pomodoro Timer to help you focus during study sessions and breaks. Additionally, StudySync allows you to log your daily study activities with timestamps.

## How to Use StudySync

1. **Pomodoro Timer:**
   - Click the "Start Pomodoro" button to initiate a Pomodoro study session (25 minutes).
   - Track your progress with a countdown timer and progress bar.
   - Upon completion, receive an alert, and the timer resets for the next session.

2. **Break Timer:**
   - After a Pomodoro session, click the "Start Break" button for a 5-minute break.
   - Countdown timer and progress bar guide your break.
   - Receive an alert when the break ends, and the timer resets.

3. **Stop Timer:**
   - Click "Stop" to pause the current timer, useful for interruptions.

4. **Log Daily Study:**
   - Click "Log Daily Study" to record your study activities.
   - Enter a description in the dialog box and click "OK."
   - Daily study logs are stored in a database for reference.

5. **Show All Logs:**
   - Click "Show All Logs" to view a list of all your study logs.
   - The new window displays logs with dates and study descriptions.

## Daily Study Logger

StudySync features a Daily Study Logger to track your daily study sessions efficiently.

## Database Manager

Utilizing SQLite, StudySync stores study logs securely. The Database Manager handles table creation, saving study logs, and fetching all logs.

## How to Run StudySync

1. Ensure Python is installed.
2. Run `PomodoroTimer.py` to start the StudySync app.
3. Follow on-screen instructions for the timer and daily study logging.

Feel free to contribute, report issues, or suggest improvements to enhance StudySync!
