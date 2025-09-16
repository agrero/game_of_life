from src.Gol import Gol

from src.plot.figures import heatmap_animation

import plotly.graph_objects as go
import numpy as np
import random as rnd

# Fixed random seed setting
rnd.seed(42)  

# box sizes
x_dim = 200
y_dim = 200
p_flipped = .5

n_flipped = int(x_dim*y_dim*p_flipped)
n_loops = 400

gol = Gol(
    shape = (x_dim,y_dim),
    init_flipped = n_flipped
)

frames, count = gol.simulate(n_loops)

fig = heatmap_animation(frames, gol)

fig.update_layout(coloraxis_showscale=False)

fig.show()

count = np.array(count)
dcount = np.abs(count[:-1] - count[1:])

count_fig = go.Figure(
    data=[go.Scatter(x=[i for i in range(len(count))], y=count/count.max()),
          go.Scatter(x=[i for i in range(len(dcount))], y=dcount/dcount.max())]
)

count_fig.show()