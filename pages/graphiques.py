import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc


def graphiques():
    jumbotron = html.Div(
        dbc.Container(
            [
                html.H1("Graphics", className="display-3"),
                html.P(
                    "Dans cette section vous allez pouvoir créer des graphiques grâce aux données chargées",
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
    return layout
