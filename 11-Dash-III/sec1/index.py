from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Connect to main app.py file
from app import app
from app import server

# Connect to your app pages
from apps import scatter_layout, histogram_layout

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link('Scatter | ', href='/apps/scatter_layout'),
        dcc.Link('Histogram ', href='/apps/histogram_layout'),
    ], className="row"),
    html.Div(id='page-content', children=[])
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/scatter_layout':
        return scatter_layout.layout
    if pathname == '/apps/histogram_layout':
        return histogram_layout.layout
    else:
        return "Please choose a link"


if __name__ == '__main__':
    app.run_server(debug=False)