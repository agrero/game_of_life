from numpy.typing import ArrayLike
import plotly.graph_objects as go
from src.Gol import Gol
from src.plot.tools import play_button

def gen_Frame(plot_type, data) -> list[go.Frame]:
    return [
        go.Frame(data=[plot_type(z=frame, colorscale='agsunset')], name=str(i))
        for i,frame in enumerate(data)
    ]


def heatmap_animation(frames:ArrayLike, gol_engine:Gol) -> go.Figure:
    # initial data
    init_data = [
        go.Heatmap(z=frames[0], colorscale='agsunset')
    ]
    
    layout = go.Layout(
        title="Conway's Game of Life",
        updatemenus=[play_button],
        xaxis=dict(range=[0, gol_engine.shape[0]-1]),
        yaxis=dict(range=[0, gol_engine.shape[1]-1])
    )
    
    return go.Figure(
        data=init_data,
        layout=layout,
        frames=gen_Frame(go.Heatmap, frames)
    )