play_button = dict(
    type="buttons",
    direction="left",
    pad={"r": 10, "t": 87},
    showactive=False,
    x=0.1,
    xanchor="right",
    y=0,
    yanchor="top",
    buttons=[
        dict(
            label="Play",
            method="animate",
            args=[None, {"frame": {"duration": 100, "redraw": True},
                        "fromcurrent": True, "transition": {"duration": 0}}]
        ),
        dict(
            label="Pause",
            method="animate",
            args=[[None], {"frame": {"duration": 0, "redraw": False},
                          "mode": "immediate",
                          "transition": {"duration": 0}}]
        )
    ]
)