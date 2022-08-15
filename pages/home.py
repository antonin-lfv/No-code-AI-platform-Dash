import dash
from dash import html, dcc, callback, Input, Output
import dash_extensions as de

dash.register_page(__name__, path='/', title='Home')

layout = html.Div(children=[
    html.Br(),
    html.Br(),
    html.Br(),
    html.P("No-code AI Platform",
           className="first_titre"),
    html.Hr(style={'width': '75%', 'margin': 'auto'}),
    html.Br(),
    html.Br(),

    html.Div([
        html.Div([
            html.Div(className="col-1"),
            html.Div([
                html.P("""Bienvenue sur la no-code AI platform ! Déposez vos datasets csv ou excel ou
                    choisissez en un parmi ceux proposés et commencez votre analyse dès maintenant ! Cherchez les
                    variables
                    les plus intéressantes, visualisez vos données, et créez vos modèles de Machine Learning en toute
                    simplicité. Si vous choisissez de travailler avec votre dataset et que vous voulez effectuez des
                    modifications sur celui-ci, il faudra le télécharger une fois les modifications faites pour pouvoir
                    l'utiliser sur les autres pages. """,
                       className="intro"),
                html.P("""Un tutoriel sur l'utilisation de ce site est disponible sur le repo Github. En cas de
                    bug ou d'erreur veuillez m'en informer par mail ou sur Discord.""",
                       className="intro"),
                html.P("""Commencez par choisir un dataset dans la section Dataset !""",
                       className="intro"),
                html.Div([
                    html.Div([
                        html.Div([
                            html.H4("Liens"),
                            ". ",
                            html.A("Mon site", href="https://antonin-lfv.github.io")
                        ],
                            className="col-6"),
                        html.Div([
                            de.Lottie(options=dict(background="transparent",
                                                   speed="1",
                                                   style="width: 120px; height: 120px; display: flex; flex-flow: "
                                                         "column wrap; ",
                                                   loop=True,
                                                   autoplay=True),
                                      width="25%",
                                      height="25%",
                                      url='https://assets6.lottiefiles.com/packages/lf20_vEfHlN.json')
                        ],
                            className="col-6")
                    ],
                        className="row")
                ],
                    className="container")
            ],
                className="col-6"),
            html.Div([
                html.Img(src='assets/images/logo.png', alt="logos")
            ],
                className="col-4"),
            html.Div(className="col-1"),
        ],
            className="row")
    ],
        className='container')
])
