from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from dash import dcc, html, callback

import dash_bootstrap_components as dbc


layout = html.Div(children=[
    html.Div(dbc.Row(children=[
        dbc.Col(children=[
            dbc.Row(dbc.Col(html.H5(id='user', style={'padding-top': '5px', 'margin-bottom': '0px'}))),
            dbc.Row(dbc.Col(children=[
                dbc.Button(id='toggle-offcanvas', children=[html.I(className='fa fa-bar-chart'), '   Dashboards'],
                           outline=True, color='warning', size='sm', n_clicks=0)]))
        ]),
        dbc.Col(html.H2(id='banner', style={})),
        dbc.Col(dbc.Button(id='logout-btn', children=[html.I(className='fa fa-power-off'), '  Log out'], n_clicks=0,
                           outline=True, color='danger', style={'padding-top': '10px'}))
    ])),
    dbc.Offcanvas(id='offcanvas', is_open=False, style={'width': '350px'}, title='Dashboards'),
    html.Div(id='display-components')
])


@callback(Output('token', 'data'),
          Output('logout-btn', 'n_clicks'),
          Output('url', 'pathname'),
          Input('logout-btn', 'n_clicks'))
def logout(n_clicks):
    if not n_clicks:
        raise PreventUpdate
    else:
        return None, None, '/'