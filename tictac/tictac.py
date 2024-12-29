'''
Time complexity tester.
'''
import numpy as np
from time import time, sleep
from typing import Callable

def void(i):
    return

def tictac(lower_bound=0, upper_bound=100, step=1,
           code: Callable[[int], None] = void,
           precode: Callable[[int], None] = void,
           postcode: Callable[[int], None] = void,
           total_tests=4, show=True):
    '''Time complexity tests.'''
    
    print("\ntictac: Time Complexity Test")
    print("--------------------")
    print(f"Making {total_tests} time complexity tests witn n's for each test "
          f"in range({lower_bound}, {upper_bound}, {step}).")
    
    if show:
        print("Progress shown. Use show=False to hide it.")
    
    TIC = time()
    for k in range(total_tests):
        n, times = [], []
        if show:
            TAC = time() - TIC
            print(f"\nTest time: {round(TAC, 2)}s", f"k = {k}", f"n | t",
                  "------------", sep="\n")
        for i in range(lower_bound, upper_bound, step):
            precode(i)

            tic = time()
            code(i)
            tac = time() - tic
            
            postcode(i)

            n.append(i)
            times.append(tac)
            
            if show:
                print(f"{i} | {tac:.2f}s")
        n, times = np.array(n), np.array(times)
        if k == 0:
            times_avg = times
        times_avg += times / total_tests
    
    TAC = time() - TIC
    if show:
        print(f"\nFinished test! ({TAC:.2f}s)")
    return n, times_avg


#%% main()
def main():
    import matplotlib.pyplot as plt

    def precode(i):
        global A
        A = [a for a in range(i)]
        sleep(1)

    def code(i):
        print(A)

    n, t = tictac(upper_bound=int(1E5), precode=precode, code=code,
                  total_tests=3, step=10000)

    fig, ax = plt.subplots()
    ax.plot(n, t)

    plt.show()


#%% 呪い
if __name__ == '__main__':
    main()
