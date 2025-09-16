import time
import pandas as pd
from src.Gol import Gol
import datetime

n_loops = 5
times = []
for i in range(n_loops):
    t1 = time.time()

    x_dim = 100 
    y_dim = 100
    p_flipped = 0.5

    n_flipped = int(x_dim*y_dim*p_flipped)
    n_loops = 1000
    gol = Gol(
        shape = (x_dim,y_dim),
        init_flipped = n_flipped
    )

    frames = gol.simulate(n_loops)

    t2 = time.time()
    times.append(t2-t1)

avg_time = sum(times) / n_loops
var = max(times) - min(times)
date = datetime.datetime.now()

df = pd.concat([
    pd.read_csv('speed_test_data.csv'), 
    pd.DataFrame([avg_time, var, n_loops, x_dim, date], 
                     columns=['time', 'variance', 'n_iterations', 'date'])
]).to_csv('speed_test_data.csv')