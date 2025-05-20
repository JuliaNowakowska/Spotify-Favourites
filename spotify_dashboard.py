import plotly.graph_objects as go

class Dashboard:
    def __init__(self):
        pass

    def show(self, fav_song):
        fig = go.Figure()

        fig.add_annotation(
            text=f"<b>My Favorite Song is:</b><br>{fav_song}",
            xref='paper', yref='paper',
            showarrow=False,
            font=dict(size=28, color="black"),
            align="right"
        )

        fig.update_layout(
            paper_bgcolor="white",
            plot_bgcolor="white",
            xaxis=dict(visible=False),
            yaxis=dict(visible=False)
        )

        fig.show()
