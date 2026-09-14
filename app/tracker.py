import subprocess
import time
from datetime import datetime


def get_focused_window():
    return subprocess.check_output(
        ["xdotool", "getwindowfocus", "getwindowname"]
    ).decode().strip()


previous_window = None
start_time = None

while True:
    current_window = get_focused_window()

    if current_window != previous_window:
        now = datetime.now()

        if previous_window is not None:
            duration = now - start_time

            print(
                f"{previous_window} | "
                f"{start_time.strftime('%H:%M:%S')} → "
                f"{now.strftime('%H:%M:%S')} | "
                f"{duration}"
            )

        previous_window = current_window
        start_time = now

    time.sleep(3)