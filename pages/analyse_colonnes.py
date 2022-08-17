import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc


jumbotron = html.Div(
    dbc.Container(
        [
            html.H1("Columns analysis", className="display-3"),
            html.P(
                "Dans cette section vous allez pouvoir analyser en détail les colonnes de votre dataset",
                className="lead",
            )
        ],
        fluid=True,
        className="py-3",
    ),
    className="p-3 rounded-3",
)

layout = html.Div([
    dbc.Row([
        dbc.Col(width=1),
        dbc.Col([html.Br(), html.Br(), html.Br(), jumbotron], width=8)
    ])
])
