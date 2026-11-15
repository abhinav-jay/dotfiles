import subprocess
import time

start = time.time()
i = 1
subprocess.run(["notify-send", "The program to keep track of the number of hours spent on the computer has started."])

while 1:
    if time.time() - start > 3600 * i:
        if i == 1:
            subprocess.run(["notify-send", "It has been an hour that you have been using the computer"])
            i += 1
        else:
            subprocess.run(["notify-send", f"It has been {i} hours that you have been using the computer"])
            i += 1
