'''WIP! Time complexity tester.'''
import numpy as np
import time
import sys
sys.path.insert(0, '../Formatter')
import minipy_formatter as MPF

def tictac(lower_bound, upper_bound, step=1,
           total_tests=4, show=True):
    '''Complexity test.'''
    TIC = time()
    for k in range(total_tests):
        n, times = [], []
        if show:
            TAC = time() - TIC
            print(f"\nTest time: {round(TAC, 2)}s", f"k = {k}", f"n | t",
                  "------------", sep="\n")
        for i in range(lower_bound, upper_bound, step):
            coeff = np.random.uniform(-100, 100, (i, 1))
            P = Polynomial(coeff)
            
            tic = time()
            P.FFT()
            tac = time() - tic
            
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

help(MPF)
