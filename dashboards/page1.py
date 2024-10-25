from dash import html, dcc
from dash.dependencies import State, Input, Output

import dash_bootstrap_components as dbc


layout = html.Div(children=[
    dbc.Row(children=[
        dbc.Col(dcc.Graph(figure={}), width=6),
        dbc.Col(dcc.Graph(figure={}), width=6)
    ])
])