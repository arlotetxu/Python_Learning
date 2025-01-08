'''
IMPORTED METHODS
'''
import multiprocessing
import multiprocessing.process
import time
from icecream import ic
import random

'''
========================FIRST ATTEMPT TO CREATE PROCESSES======================
'''
def worker(name: str) -> None:
    st_time = time.time()
    print(f"Starting the work - {name}...")
    waiting = random.choice(range(1, 10))
    time.sleep(waiting)
    fn_time = time.time()
    total_time = fn_time - st_time
    print(f"The work {name} finished after {total_time} seconds!!")


# if __name__ == '__main__':
#     processes = []
#     for i in range(1, 6):
#         process = multiprocessing.Process(
#             target = worker,
#             args = (i,)
#         )
#         processes.append(process)
#         process.start()

#     for proc in processes:
#         proc.join()
    '''The join() functions tells python to wait the code execution till the process proc has finished their work'''


'''
=====================SUBCLASSING MULTIPROCESSING MODULE========================
'''

class Worker_Process(multiprocessing.Process):

    def __init__(self, name: str) -> None:
        multiprocessing.Process.__init__(self)
        self.name = name

    def run(self)-> None:
        '''
        Run the processes
        '''
        worker_2(self.name)

def worker_2(name: str) ->None:
    st_time2 = time.time()
    print(f"Starting the process nb: {name}...")
    waiting_Time = random.choice(range(1, 10))
    time.sleep(waiting_Time)
    fn_time2 = time.time()
    proc_time = fn_time2 - st_time2
    print(f"The process nb {name} has finished after {proc_time} seconds!!")


# if __name__ == '__main__':
#     processes_2 = []
#     for i in range (1, 9):
#         process2 = Worker_Process(str(i))
#         processes_2.append(process2)
#         process2.start()

#     for each in processes_2:
#         each.join()

#     print("print at the end")


'''
===========================CREATING A PROCESS POOL=============================
This process pool is used to limitate the number of processes than can be working at the same time...
Imagine you have a CPU with only 4 cores but you need to create a program that uses 20 processes... with this option it is possible such limitation.
'''
def worker_3(name: str) -> None:
    st_time = time.time()
    print(f"Starting the work - {name}...")
    waiting = random.choice(range(1, 10))
    time.sleep(waiting)
    fn_time = time.time()
    total_time = fn_time - st_time
    print(f"The work {name} finished after {total_time} seconds!!")


if __name__ == '__main__':
    processes_3 = [str(i) for i in range(1, 16)]
    pool = multiprocessing.Pool(processes=5)
    pool.map(worker_3, processes_3)
    pool.terminate() #If terminate is not called, python shows an error msg confirming leaks
'''﻿Python will now run 5 processes (or less) at a time until all the processes have finished'''
