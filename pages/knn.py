import dash
from dash import html, dcc, callback, Input, Output

dash.register_page(__name__, path='/knn', title='KNN')

layout = html.Div(children=[
    html.H1(children='This is the knn page'),


])
