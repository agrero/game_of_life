from src.Reader import Reader
from src.plot.figures import heatmap_animation
from src.plot.tools import play_button


import plotly.graph_objects as go
import pandas as pd
import os

class Plotter:
    def gol_2d(self, data:pd.DataFrame, plot_type):
        # count_steps
        max_step = data.loc[:,'step'].max()


        init_data = [
            go.Heatmap(z=data[data['step'] == 0])
        ]

        layout = go.Layout(
            title="Conway's Game of Life",
            updatemenus=[play_button],
            xaxis=dict(range=[0, data.shape[1]-1]),
            yaxis=dict(range=[0, data.shape[1]-1])
        )

        print(data[data['step']==0])
        print(pd.unique(data.loc[:,'step']))

        frames = [
            go.Frame(data=[plot_type(z=data[data['step'] == ndx], colorscale='agsunset')])
            for ndx in pd.unique(data.loc[:,'step'])
        ]

        return go.Figure(
            data=init_data, 
            layout=layout,
            frames=frames
        )


read = Reader(os.path.join('traj', 'seed:0', '0-7000.csv'))

plotter = Plotter()

fig = plotter.gol_2d(read.data, go.Heatmap)

fig.show()
fig.to_html('test.html')