from sklearn.cluster import KMeans
import numpy as np
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
from sklearn.cluster import KMeans
import pandas as pd



app = Dash(__name__)

df = pd.read_csv('Starbucks.csv')
df=df[df['Store Number'] != '19773-160973']



X=df[['Longitude','Latitude']]

nc=20

kmeans = KMeans(n_clusters=nc, random_state=0)
kmeans.fit(X)

df['predict']=kmeans.predict(X)

fig = px.scatter(df, x="Longitude", y="Latitude", color="predict", hover_data=['Country'])



app.layout = html.Div(children=[
    html.H1(children='Use K mean to group store by GPS'),

    
    dcc.Graph(
        id='storeInPhuket',
        figure=fig
    ),



])


if __name__ == '__main__':
    app.run_server(debug=True)