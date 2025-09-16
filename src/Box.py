import numpy as np
import random as rnd

class Box:
    def __init__(self, shape:tuple[int,int], init_flipped:int=1) -> None:

        self.box = np.zeros(shape=shape[0] * shape[1])

        flipped = np.array(rnd.sample(range(shape[0] * shape[1]), init_flipped))

        self.box[flipped] = 1.

        self.box = np.reshape(self.box, shape)     

