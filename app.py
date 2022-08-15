from dash import Dash, html, dcc
import dash
from config import *

app = Dash(__name__, use_pages=True, external_scripts=JS_scripts.external_scripts,
           external_stylesheets=CSS_scripts.external_stylesheets)

app.layout = html.Div([
    html.Nav(
        html.Div([
            html.A("No-code AI platform", className="navbar-brand", href="/"),
            html.Div(
                html.Ul([
                    # Navbar links
                    html.Li(
                        html.A("Home",
                               className="nav-link", href="/"
                               ),
                        className="nav-item"
                    ),
                    html.Li(
                        html.A("Dataset",
                               className="nav-link", href="/dataset"
                               ),
                        className="nav-item"
                    ),
                    html.Li(
                        html.A("Analyse des colonnes",
                               className="nav-link", href="/analyse_colonnes"
                               ),
                        className="nav-item"
                    ),
                    html.Li(
                        html.A("Matrice de corrélations",
                               className="nav-link", href="/matrice_corr"
                               ),
                        className="nav-item"
                    ),
                    html.Li(
                        html.A("Graphiques",
                               className="nav-link", href="/graphiques"
                               ),
                        className="nav-item"
                    ),
                    html.Li(
                        html.A("Régressions",
                               className="nav-link", href="/regressions"
                               ),
                        className="nav-item"
                    ),
                    # End navbar links
                ]),
                className="collapse navbar-collapse", id="navbarNavDropdown"
            )

        ], className="container-fluid"),
        className="navbar navbar-expand-lg fixed-top navbar-dark bg-dark"
    ),

    html.Div(
        [
            html.Div(
                dcc.Link(
                    f"{page['name']} - {page['path']} - {page['relative_path']}", href=page["relative_path"]
                )
            )
            for page in dash.page_registry.values()
        ]
    ),

    # Content #
    html.Br(),
    dash.page_container,
    # End content #

    # Footer #
    html.Footer([
        html.Br(),
        html.Div([
            "© 2022 Copyright",
            html.A(
                " - Antonin LEFEVRE",
                className="text-dark"
            )
        ],
            className="text-center text-dark p-3",
            style={"background-color": "rgba(0, 0, 0, 0)"})
    ],
        className="text-center text-white, mt-auto")
    # End footer #

],
    className="d-flex flex-column min-vh-100")

if __name__ == '__main__':
    app.run_server(debug=True)
