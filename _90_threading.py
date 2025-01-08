'''
IMPORTED METHODS
'''

from icecream import ic # To substituted print function giving more information
from time import sleep
import threading
import random

'''
The concurrecy is the ability to run multiple pieces of code at the same time.
You can use processes or threads. The main difference between both is that
in threads, the memory is shared among the threads while in processes, each
process has their own portion of memory.
Threads are more difficult to understand and write properly and linked to them
is the risk of "race condition", where each thread could access to the same
variable (memory shared) and get wrong values because at the same time,
another thread is modifying the variable value.
﻿A race condition happens when you have a computer program that depends on
a certain order of events to happen for it to execute correctly.
If your threads execute something out of order, then the next thread may not
work and your application can crash or behave in unexpected ways.
Look for Global Interpreter Lock (GIL) to control this circumstance.
'''


'''
=========================FIRST ATTEMPT TO CREATE THREADS=======================
'''
test = 0
def worker(id: str) -> None:
    global test
    print(f"Started working --> {id}")
    working_time = random.choice(range(1, 20))
    sleep(working_time)
    print(f"Work {id} finished in {working_time} seconds!!")
    test += 1
    print(f"test value: {test}")

# if __name__ == "__main__":
#     for id in range (1, 5):
#         thread = threading.Thread(
#             target = worker,
#             args = (str(id),)
#         )
#         thread.start()

'''
﻿The last block of code creates 5 worker threads. To create a thread, you pass in your worker() function as the target function for the thread to call. The other argument you pass to thread is a tuple of arguments that thread will pass to the target function. Then you call thread.start() to start running that thread.
When the function stops executing, Python will delete your thread.
'''


'''
==========================SUBCLASSING THREAD MODULE============================
To get more control over the threads creation and manipulation. In this case,
the threads are created in each instance of the class workThreads in the
__init__ method.
﻿When you call start() in the last line of the code snippet, it will call run() for you itself. The start() method is a method that is a part of the threading.Thread class and you did not override it in your
code.
'''

class workThreads(threading.Thread):

    def __init__(self, id_):
        threading.Thread.__init__(self)
        self.instance_id = id(self)
        self.id_ = id_

    def run(self):
        '''
        Running the function worker_2. The function name must be 'run' to be
        executable as it is defined in the thread class. What we are doing here
        is overwritting it.
        '''
        worker_2(self.id_, self.instance_id)

def worker_2(id: str, instance_id: int) -> None:
    print(f"Started working: {id} - {instance_id}")
    working_time = random.choice(range(1, 15))
    sleep(working_time)
    print(f"{id} - {instance_id} finished in {working_time} seconds")


if __name__ == "__main__":
    for i in range (1, 6):
        thread = workThreads(i)
        thread.start()
