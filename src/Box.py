import numpy as np
import random as rnd

class Box:
    def __init__(self, box:np.typing.ArrayLike=None) -> None:
        self.box = box

    def random_box(self, shape:tuple[int,int]=(100,100), init_flipped:int=1000) ->np.typing.ArrayLike:
        box = np.zeros(shape=shape[0] * shape[1])

        flipped = np.array(rnd.sample(range(shape[0] * shape[1]), init_flipped))

        box[flipped] = 1

        return np.reshape(box, shape)   