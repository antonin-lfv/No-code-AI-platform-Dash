from dash import Dash, html, dcc, callback, Output, Input
from pages import home, dataset, analyse_colonnes, graphiques, matrice_corr
from config import *
import dash_bootstrap_components as dbc


app = Dash(__name__,
           suppress_callback_exceptions=True,
           external_scripts=JS_scripts.external_scripts,
           external_stylesheets=CSS_scripts.external_stylesheets)
server = app.server

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/")),
        dbc.NavItem(dbc.NavLink("Dataset", href="/dataset")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Analyse des colonnes", href="/analyse_col"),
                dbc.DropdownMenuItem("Graphiques", href="/graphiques"),
                dbc.DropdownMenuItem("Matrice de corrélation", href="/matrice_corr"),
            ],
            nav=True,
            in_navbar=True,
            label="Pre-processing",
            size="lg",
        ),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Page 2", href="#"),
                dbc.DropdownMenuItem("Page 3", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="Machine Learning",
            size="lg",
        ),
        dbc.NavItem(dbc.NavLink("About", href="/about")),
    ],
    brand="No-code AI Platform",
    brand_href="/",
    color="dark",
    dark=True,
    sticky="fixed",
    links_left=True
)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([navbar]),
    html.Div(id='page-content')
])


@callback(Output('page-content', 'children'), Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        layout = home.home()
        return layout
    elif pathname == '/dataset':
        layout = dataset.dataset()
        return layout
    elif pathname == '/analyse_col':
        layout = analyse_colonnes.analyse_colonne()
        return layout
    elif pathname == '/graphiques':
        layout = graphiques.graphiques()
        return layout
    elif pathname == '/matrice_corr':
        layout = matrice_corr.matrice_corr()
        return layout
    else:
        return html.Div('Error 404', className="first_titre")


if __name__ == '__main__':
    app.run_server(debug=True)
