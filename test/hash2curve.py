from pyecc.sm2 import *
import os
import time

if __name__ == '__main__':
    plaint_text = [os.urandom(32).hex() for i in range(10000)]
    time_start = time.time()
    points = list2curve(plaint_text)
    time_end = time.time()
    print(f"Time used: {time_end - time_start} s")
    print("average time used: ", (time_end - time_start) / len(plaint_text))
