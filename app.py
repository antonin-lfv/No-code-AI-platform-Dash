from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
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
                    dbc.DropdownMenu(
                        children=[
                            dbc.DropdownMenuItem("KNN", href="/knn"),
                            dbc.DropdownMenuItem("KMeans", href="/kmeans"),
                            dbc.DropdownMenuItem("SVM", href="/svm"),
                            dbc.DropdownMenuItem("Decision tree", href="/decision_tree"),
                        ],
                        label="Classifications",
                        nav=True,
                        in_navbar=True,
                            ),
                    dbc.DropdownMenu(
                        children=[
                            dbc.DropdownMenuItem("PCA", href="/pca"),
                            dbc.DropdownMenuItem("UMAP", href="/umap"),
                            dbc.DropdownMenuItem("LLE", href="/lle"),
                        ],
                        label="Réduction de dimension",
                        nav=True,
                        in_navbar=True,
                    ),
                    # End navbar links
                ],
                    className="navbar-nav"
                ),
                className="collapse navbar-collapse", id="navbarNavDropdown"
            )

        ], className="container-fluid"),
        className="navbar navbar-expand-lg fixed-top navbar-dark bg-dark"
    ),

    # Content #
    html.Br(),
    html.Br(),
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
