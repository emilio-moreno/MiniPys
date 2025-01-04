'''
Time complexity tester.
'''
import numpy as np
import matplotlib.pyplot as plt
from time import time, sleep
from typing import Callable, Tuple
ndarray = np.ndarray

def void(i):
    return None

class TicTac:
    def __init__(self, name: str, low_bound: int = 0, up_bound: int = 100,
        step: int = 1, variable: str = "n",
        code: Callable[[int], None] = void,
        precode: Callable[[int], None] = void,
        postcode: Callable[[int], None] = void,
        total_tests=4, show=True) -> Tuple[ndarray, ndarray]:
        '''Time complexity tests.'''
        self.name = name
        self.low_bound = low_bound
        self.up_bound = up_bound
        self.step = step
        self.total_tests = total_tests
        self.variable = variable
        
        print(f"\nTicTac - Time Complexity Test")
        print(f"Name: {name}")
        if variable != "n":
            print(f"Testing (n): {variable}")
        print("")
        print(f"Making {total_tests} time complexity tests witn n's for each test "
              f"in range({low_bound}, {up_bound}, {step}).")
        if show:
            print("Progress shown. Use show=False to hide it.")

        TIC = time()
        for k in range(total_tests):
            n, times = [], []
            if show:
                TAC = time() - TIC
                print(f"\nTest time: {round(TAC, 2)}s", f"k = {k}", f"n | t",
                      "------------", sep="\n")
            for i in range(low_bound, up_bound, step):
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
            print(f"\nFinished test! (Total test time: {TAC:.2f}s)")

        self.n = np.array(n)
        self.t = np.array(times_avg)

    def plot(self) -> Tuple[plt.figure, plt.axis]:
        fig, ax = plt.subplots()
        ax.scatter(self.n, self.t, color='#5dd4d8')
        title = f"{self.name}"
        title += f"\nrange({self.low_bound}, {self.up_bound}, {self.step})"
        title += f"\nTotal tests = {self.total_tests}"
        ax.set(title=title, xlabel=self.variable, ylabel="Time taken (s)")
        ax.grid(linestyle='--', color='#c0c0c0')
        return fig, ax



#%% main()
def main():
    import matplotlib.pyplot as plt

    def precode(i):
        global A
        A = [a for a in range(i)]
        sleep(1)

    def code(i):
        print(A)

    test = TicTac(name='Print List', variable='List length (i)',
                up_bound=int(1E3) + 1, precode=precode, code=code,
                total_tests=3, step=100)
    test.plot()
    plt.show()


#%% 呪い
if __name__ == '__main__':
    main()
