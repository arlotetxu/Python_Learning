import schedule
import time

num_prints = 0

def printing():
    global num_prints
    print(f"Print: {num_prints}")
    num_prints += 1

schedule.every(3).seconds.do(printing)

while True:
    schedule.run_pending()
    # time.sleep(1)
