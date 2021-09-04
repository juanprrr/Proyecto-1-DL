import matplotlib.pyplot as plt
import numpy as np

class NZRI:
    def __init__(self, binNum):
        self.bits = binNum
        self.data = np.repeat(self.bits, 2)
        self.state = True
        self.nzri = []
        self.calcNzriArray()
        self.t = 0.5 * np.arange(len(self.data))

        self.my_lines('x', range(len(self.bits)), color='.5', linewidth=2)
        self.my_lines('y', [0], color='.5', linewidth=2)

        plt.step(range(len(self.bits)+1), self.nzri + [self.nzri[-1]], 'r', linewidth = 2, where='post')
        plt.ylim([-2,2])

        for tbit, bit in enumerate(self.bits):
            plt.text(tbit + 0.5, -0.5, str(bit))

        plt.gca().axis('off')
        plt.show()
        

    def calcNzriArray(self):
        for n in self.bits:
            if n == 1:
                self.state = not self.state
            else:
                pass
            if self.state == True:
                self.nzri = self.nzri + [1]
            else:
                self.nzri = self.nzri + [0]
                



    def my_lines(self, ax, pos, *args, **kwargs):
        if ax == 'x':
            for p in pos:
                plt.axvline(p, *args, **kwargs)
        else:
            for p in pos:
                plt.axhline(p, *args, **kwargs)
                
a = NZRI([1])
                


