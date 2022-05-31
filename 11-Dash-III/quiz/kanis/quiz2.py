import json
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

import pandas as pd

app = Dash(__name__)

df = pd.read_csv('Starbucks.csv')

df=df[df['Brand'] == 'Starbucks']
df=df[df['Country'].isin(['TH','MY','VN','SG'])]
df['CityKey']=df['Country']+df['City']

dfsummary=df.groupby(['Country'])['Store Number'].count()
dfsummary=dfsummary.reset_index()

dfsummarybycity=df.groupby(['City'])['Store Number'].count()
dfsummarybycity=dfsummarybycity.reset_index()


figbycountry = px.bar(dfsummary, x='Country', y='Store Number', barmode='group')

figbycity = px.bar(dfsummarybycity, x='City', y='Store Number', barmode='group')
app.layout = html.Div(children=[
    html.H1(children='Number of Store in TH,MY,SG,VN'),

    
    dcc.Graph(
        id='storeByCountryViz',
        figure=figbycountry
    ),

    dcc.Graph(
        id='storeByCityViz',
        figure=figbycity
    )

    

])


@app.callback(
    Output('storeByCityViz', 'figure'),
    Input('storeByCountryViz', 'clickData')
    )

def update_graph(data):
    dffilter=df
    if bool(data):
        dffilter=df[df['Country']==data['points'][0]['x']]

    dfsummarybycity=dffilter.groupby(['City'])['Store Number'].count()
    dfsummarybycity=dfsummarybycity.reset_index()

    figbycity = px.bar(dfsummarybycity, x='City', y='Store Number', barmode='group')

    return figbycity


if __name__ == '__main__':
    app.run_server(debug=True)