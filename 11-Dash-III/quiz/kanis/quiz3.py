from dash import Dash, dcc, html, Input, Output
import plotly.express as px

import pandas as pd

app = Dash(__name__)

df = pd.read_csv('Starbucks.csv')

df=df[df['Brand'] == 'Starbucks']
df=df[df['City'] == 'Phuket']




fig = px.density_mapbox(df, lat='Latitude', lon='Longitude', radius=10,
                        center=dict(lat=7.8, lon=98.32), zoom=8,
                        mapbox_style="stamen-terrain")

app.layout = html.Div(children=[
    html.H1(children='Store in Phuket'),

    
    dcc.Graph(
        id='storeInPhuket',
        figure=fig
    ),



])


if __name__ == '__main__':
    app.run_server(debug=True)