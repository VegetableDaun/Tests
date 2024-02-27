from multiprocessing.pool import ThreadPool
from random import randint
from time import time


def calculator(n):
    ans = 0
    for i in range(10_000_000):
        ans += randint(0, 9)

    ans /= n
    return ans


theads = []
ans = []
if __name__ == '__main__':
    t0 = time()
    # pool = ThreadPool(processes=4)
    #
    # for i in range(4):
    #     theads.append(pool.apply_async(calculator, (i + 1,)))
    #
    # # for i in range(4):
    # #     thead = threading.Thread(target=calculator)
    # #     theads.append(thead)
    # #
    # # for i in theads:
    # #     i.start()
    # #
    # # for i in theads:
    # #     i.join()
    #
    # for i in theads:
    #     ans.append(i.get())
    # 
    # ans_1, ans_2, ans_3, ans_4 = ans

    ans_1 = calculator(1)
    print(f'Done! ans_1 = {ans_1}')

    ans_2 = calculator(2)
    print(f'Done! ans_2 = {ans_2}')

    ans_3 = calculator(3)
    print(f'Done! ans_3 = {ans_3}')

    ans_4 = calculator(4)
    print(f'Done! ans_4 = {ans_4}')

    print('result', ans_1 + ans_2 + ans_3 + ans_4)
    print(time() - t0)
