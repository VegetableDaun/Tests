import os
from random import randint
from time import time, sleep
from multiprocessing import Process, Pool, Lock


def create_file(name):
    with open(name, "w") as file:
        for i in range(10_000_000):
            file.write(f'{randint(0, 9)}\n')


def reading(name):
    ans = 0
    with open(name, 'r') as file:
        for s in file:
            ans += randint(0, int(s))

    print(os.getpid(), ans)

def sq(x):
    return x ** 2


if __name__ == "__main__":
    t0 = time()
    L = Lock()

    with Pool(4) as p:
        # p.map(reading, [('numbers'), ('numbers'), ('numbers'), ('numbers')])
        # ans = p.map(sq, [1, 2, 3, 4])
        # ans = p.apply(sq, (1, ))
        HMM = p.map_async(reading, [('numbers'), ('numbers'), ('numbers'), ('numbers')])

        print(HMM)

        ans_0 = HMM.get()
        ans_1 = HMM.ready()

        print("MDA")

    print(ans_0, ans_1)
    print(time() - t0, 'Code was running!')
