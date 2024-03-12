import plotly.graph_objects as go
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    number={'suffix': "% match", 'font': {'size': 50}},
    value=80,
    domain={'x': [0, 1], 'y': [0, 1]},
    gauge={
        'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
        'bar': {'color': "darkblue"},
        'bgcolor': "white",
        'borderwidth': 2,
        'bordercolor': "gray",
        'steps': [
            {'range': [0, 33], 'color': 'red'},
            {'range': [33, 66], 'color': 'yellow'},
            {'range': [66, 100], 'color': 'green'}],
    }))

fig.update_layout(font={'color': "black", 'family': "Arial"}, value=40)

fig.show()
