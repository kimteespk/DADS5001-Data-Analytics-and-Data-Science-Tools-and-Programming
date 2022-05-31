from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd


app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df=pd.read_csv("Starbucks.csv")
df2=df.loc[df["Country"].isin(["TH","SG","VN","MY"])]
df2=df2.groupby("Country").agg({"Store Number":"count"})
df2["Country_name"]=["Malaysia","Singapore","Thailand","Viet Nam"]
df2=df2.reset_index()

fig2 = px.bar(df2, x="Country_name", y="Store Number",barmode="overlay",color="Country_name")

app.layout = html.Div(children=[
    html.H1(children='Starbucks stores'),

    html.Div(children='''
        this graph, users can compare the number of Starbucks stores
among Thailand, Vietnam, Singapore, and Malaysia.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig2
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)