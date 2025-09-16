import pandas as pd 
import numpy as np

import argparse

import random as rnd
import time
import datetime
import os

from src.Gol import Gol

# scanning random seeds for novel/convergent trajectories

parser = argparse.ArgumentParser()

# add arguments

parser.add_argument('-x', '--xdim', type=int, default=1000)
parser.add_argument('-y', '--ydim', type=int, default=1000)
parser.add_argument('-s', '--seed', type=int, default=0)
parser.add_argument('-e', '--end', type=int, default=1)
parser.add_argument('-pfl', '--p_flipped', type=int, default=50)
parser.add_argument('-th', '--thresh', type=float, default=200.0)
parser.add_argument('-wi', '--w_interval', type=int, default=200)

args = parser.parse_args()

if __name__ == '__main__':
    points = 0

    for seed in range(args.seed, args.seed + args.end):
        rnd.seed(seed)
        gol = Gol(
            shape = (args.xdim, args.ydim),
            init_flipped=int(args.xdim * args.ydim * args.p_flipped)
        )
        filename = '_'.join([f'x:{args.xdim}-y:{args.ydim}', f'sat:{args.p_flipped}'])
        sub_dir = os.path.join('traj', f'seed:{args.seed}')
        if not os.path.exists(sub_dir):
            os.makedirs(sub_dir)
        running = True
        iteration = 0
        while running:

            t1 = time.time()
            print(datetime.datetime.now())
            frames, count = gol.sim_perf(args.w_interval)
            
            # unpack frames        
            if (args.seed + args.end) - seed == args.end:
                prev_count = args.thresh 

            filename = f'{iteration}-{iteration+args.w_interval}.csv'

            pd.DataFrame(np.concat(frames)
            ).to_csv(os.path.join(sub_dir, filename))
            
            t2 = time.time()
            
            print(f'block per second: {(t2-t1)/args.w_interval}')
            
            print(f'iter time:{t2-t1}')

            print(f'abs distance: {np.abs(prev_count - count)}')
            iteration += args.w_interval
            if (np.abs(prev_count - count) < args.thresh) and (points > 5):
                running = False
            elif (np.abs(prev_count - count) < args.thresh):
                points += 1
                print(points)
                prev_count = count
            else:
                points=0
                prev_count = count

