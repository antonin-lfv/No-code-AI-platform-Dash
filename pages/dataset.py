import base64
import datetime
import io
import dash
from dash.dependencies import Input, Output, State
from dash import dcc, html, dash_table, callback
import dash_bootstrap_components as dbc
import pandas as pd


def dataset():
    jumbotron = html.Div(
        dbc.Container(
            [
                html.H1("Dataset section", className="display-3"),
                html.P(
                    "Dans cette section vous allez pouvoir choisir le dataset de votre choix",
                    className="lead",
                ),
                html.Br(),
            ],
            fluid=True,
            className="py-3",
        ),
        className="p-3 rounded-3",
    )

    layout = html.Div([
        dbc.Row([
            dbc.Col(width=1),
            dbc.Col([
                html.Br(), html.Br(), html.Br(), jumbotron,
                     ], width=8)
        ])
    ])

    return layout
