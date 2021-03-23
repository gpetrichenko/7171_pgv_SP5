from multiprocessing import Process, Lock
from time import sleep
import numpy as np
#from test2 import interval

def f(l, i):
    l.acquire()
    matrix = np.arange(100).reshape(10,10)
    try:
        for val in range(matrix[i][0], matrix[i][-1]+1):
           if val > 1:
               for n in range(2, val):
                   if (val % n) == 0:
                       break
               else:
                   print('Process :', i , 'Num:', val, ' ', l, end=" \n")
        sleep(0.5)
    finally:
        l.release()

if __name__ == "__main__":
    lock = Lock()
    for num in range(10):
        Process(target=f, args=(lock, num)).start()