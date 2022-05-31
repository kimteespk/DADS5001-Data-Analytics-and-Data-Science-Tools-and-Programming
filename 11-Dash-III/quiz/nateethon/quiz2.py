#Reference: https://github.com/Coding-with-Adam/Dash-by-Plotly/blob/master/Dash%20Components/Graph/dash-graph.py

from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
df=pd.read_csv("Starbucks.csv")
df["province_code"]=df["Country"]+df["State/Province"]
df2=df.groupby("Country").agg({"Store Number":"count"})
df2=df2.reset_index()
df2=df2.sort_values(by=['Store Number']).tail(25)


fig2 = px.pie(data_frame=df2, values='Store Number', names='Country',color='Country')
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Starbucks stores'),

    html.Div(children='''
        this graph, users can compare the number of Starbucks stores
    '''),

    dcc.Graph(
        id='example-graph',figure=fig2,clickData=None
    ),
    dcc.Graph(
        id='example-graph2',
        figure={}
    )
])
@app.callback(
    Output(component_id='example-graph2', component_property='figure'),
    Input(component_id='example-graph', component_property='clickData'),
)
def update_graph(clk_data):
    if clk_data ==None:
        cc="US"
        df2 = df.loc[df["Country"]==cc]
        df2 = df2.groupby("province_code").agg({"Store Number": "count"})
        df2 = df2.reset_index()
        fig3 = px.bar(df2, x="province_code", y="Store Number", barmode="overlay", color="province_code")
        return fig3
    else:
        #print(clk_data['points'][0]['label'])
        cc=clk_data['points'][0]['label']
        df2 = df.loc[df["Country"]==cc]
        df2 = df2.groupby("province_code").agg({"Store Number": "count"})
        df2 = df2.reset_index()
        fig3 = px.bar(df2, x="province_code", y="Store Number", barmode="overlay", color="province_code")
        return fig3

if __name__ == '__main__':
    app.run_server(debug=True)
