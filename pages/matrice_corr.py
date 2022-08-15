import dash
from dash import html, dcc, callback, Input, Output

dash.register_page(__name__, path='/matrice_corr', title='Matrice de corrélations')

layout = html.Div(children=[
    html.H1(children='This is a page'),


])
