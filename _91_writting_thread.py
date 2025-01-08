'''
IMPORTED METHODS
'''
from icecream import ic # To substituted print function giving more information
from threading import Thread
import time
import random

'''
=========================WRITTING FILES WITH THREADS=======================
'''

class   writting_files(Thread):
    def __init__(self, filename: str, lines: int, work_time:int)-> None:
        Thread.__init__(self)
        self.filename = filename
        self.lines = lines
        self.work_time = work_time
        self.initial_time = time.perf_counter()

    def run(self)->None:
        print(f"Starting the writting of file {self.filename} with {self.lines} lines.")
        with open(f"_91_files/{self.filename}", 'w') as f:
            for line in range(self.lines):
                f.write(f"This is the {line + 1} line.\n")
                time.sleep(self.work_time)
        final_time = time.perf_counter()
        total_time = final_time - self.initial_time
        print(f"Writting process in file {self.filename} finished in {total_time} seconds!! - working_time: {self.work_time}.")

if __name__ == '__main__':
    for file in range(1, 6):
        filename = f"__{file}__.txt"
        lines = random.choice(range(1, 20))
        working_time = random.choice(range(1, 5))
        thread = writting_files(filename, lines, working_time)
        thread.start()
