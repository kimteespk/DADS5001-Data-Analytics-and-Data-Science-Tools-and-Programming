from dash import Dash, dcc, html, Input, Output
import plotly.express as px

import pandas as pd

app = Dash(__name__)

df = pd.read_csv('Starbucks.csv')

df=df[df['Brand'] == 'Starbucks']
df=df[df['Country'].isin(['TH','MY','VN','SG'])]

dfsummary=df.groupby(['Country'])['Store Number'].count()
dfsummary=dfsummary.reset_index()

fig = px.bar(dfsummary, x='Country', y='Store Number', barmode='group')

app.layout = html.Div(children=[
    html.H1(children='Number of Store in TH,MY,SG,VN'),

    
    dcc.Graph(
        id='storeByCountryViz',
        figure=fig
    ),



])


if __name__ == '__main__':
    app.run_server(debug=True)