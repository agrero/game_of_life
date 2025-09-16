from src.Box import Box

import numpy as np
from numpy.typing import ArrayLike

from scipy.signal import convolve2d


class Gol(Box):
    def __init__(self, box:np.typing.ArrayLike=None) -> None:

        super().__init__(box)

        self.kernel = np.array([[1,1,1],[1,0,1],[1,1,1]])

        self.count = float(sum(sum(self.box))) 

        self.neighbors = self.count_neighbors(self.box)

    def count_neighbors(self, box : ArrayLike):
        return convolve2d(box, self.kernel, mode='same')
    
    def iteration(self):

        # DEATH 
        self.box[self.neighbors >= 4] = 0
        self.box[self.neighbors <= 1] = 0
        # LIFE conditions 
        self.box[((self.neighbors == 3) & (self.box==0))] = 1

        # recheck neighbors
        self.neighbors = self.count_neighbors(self.box)
        
        # count the surivors
        self.count = float(sum(sum(self.box)))

    def simulate(self, n_loops:int):
        frames = []
        count = []
        for i in range(n_loops):            
            self.iteration()
            frames.append(self.box.copy())  # Make a copy of each frame
            count.append(self.count)

        return frames, count

    def sim_perf(self, n_loops:int):

        count = 0 
        for i in range(n_loops):
            self.iteration()
            count += self.count

        count /= n_loops

        return self.box, count