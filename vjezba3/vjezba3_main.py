""" created by stips on 23.11.18. using PyCharm , python_version = 3.5 """

import time

from vjezba3.medak_stipan_zadatak1 import *
from vjezba3.medak_stipan_zadatak2 import *
from vjezba3.medak_stipan_zadatak3 import *


if __name__ == '__main__':
    # zadatak1()
    # zadatak2(2006)
    # zadatak3()


    start = time.time()
    zadatak1()
    end = time.time()

    print(end-start)

    start = time.time()
    zadatak2(2006)
    end = time.time()
    print(end - start)

    start = time.time()
    zadatak3()
    end = time.time()
    print(end-start)