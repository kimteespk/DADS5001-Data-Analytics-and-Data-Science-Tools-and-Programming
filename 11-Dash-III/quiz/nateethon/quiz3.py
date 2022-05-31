from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd


app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df=pd.read_csv("Starbucks.csv")
df2=df.loc[df["Country"].isin(["TH"])]
df2=df2.loc[df["State/Province"]=='83']

fig = px.scatter_mapbox(df2, lat="Latitude", lon="Longitude",hover_name="City",hover_data=["Store Number", "Store Name"],
                        color_discrete_sequence=["fuchsia"])
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


app.layout = html.Div(children=[
    html.H1(children='Starbucks stores'),

    html.Div(children='''
        this map graph, users can see the density of Starbucks stores in
Phuket, Thailand..
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)