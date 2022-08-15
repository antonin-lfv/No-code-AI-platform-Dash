from dash import Dash, html, dcc
import dash
from config import *

app = Dash(__name__, use_pages=True, external_scripts=JS_scripts.external_scripts,
           external_stylesheets=CSS_scripts.external_stylesheets)

app.layout = html.Div([
    html.H1('Multi-page app with Dash Pages'),

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

    dash.page_container
],
    className="d-flex flex-column min-vh-100")

if __name__ == '__main__':
    app.run_server(debug=True)
