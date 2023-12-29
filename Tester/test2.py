import time
import sys

frame = ["....", "."]

for i in frame:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.25)


def anm2():

    sys.stdout.write(frame[1])
    sys.stdout.flush()
    time.sleep(0.25)
    sys.stdout.write("\b \b")
    sys.stdout.flush()
    time.sleep(0.25)

for i in range(3):
    anm2()
