import dash
from dash import html, dcc, callback, Input, Output

dash.register_page(__name__, path='/dataset', title='Dataset')

layout = html.Div(children=[
    html.H1(children='This is the dataset\'s page'),


])
