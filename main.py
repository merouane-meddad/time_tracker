import subprocess
import time
from datetime import datetime

from app.database import create_database, save_session


def get_focused_window():
    return subprocess.check_output(
        ["xdotool", "getwindowfocus", "getwindowname"]
    ).decode().strip()

create_database()


previous_window = None
start_time = None

while True:
    current_window = get_focused_window()

    if current_window != previous_window:
        now = datetime.now()

        if previous_window is not None :
            duration =  now - start_time 
            duration_seconds = int(duration.total_seconds())

            save_session(
                previous_window,
                start_time.isoformat(),
                now.isoformat(),
                duration_seconds
            )



        previous_window = current_window
        start_time = now

    time.sleep(3)