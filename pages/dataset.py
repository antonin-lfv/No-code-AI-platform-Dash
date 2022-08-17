from dash import dcc, html, dash_table, callback
import dash_bootstrap_components as dbc

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

form_dataset = dbc.Form(dbc.Row(
    [
        dbc.Col(
            dbc.RadioItems(
                id="example-radios-row",
                options=[
                    {"label": "Iris", "value": "Iris"},
                    {"label": "Penguins", "value": "Penguins"},
                    {"label": "Car Price", "value": "CarPrice"},
                ],
            ),
            width=10,
        ),
    ],
    className="mb-3",
))

accordion = html.Div(
    dbc.Accordion(
        [
            dbc.AccordionItem(
                [
                    form_dataset
                ],
                title="Choisir un dataset",
            )
        ],
    )
)

layout = html.Div([
    dbc.Row([
        dbc.Col(width=1),
        dbc.Col([
            html.Br(), html.Br(), html.Br(), jumbotron
        ], width=8)
    ]),
    dbc.Row([
        dbc.Col(width=1),
        dbc.Col([
            html.Br(), accordion
        ], width=5)
    ])
])
