from dash import dcc, html, Input, Output, State, callback
from dash.exceptions import PreventUpdate
from numpy import random
import dash_bootstrap_components as dbc
import datetime
import pandas as pd

credentials = pd.read_excel('credentials.xlsx')
credentials.set_index('Username', inplace=True)

layout = html.Div(style={'height': '100vh', 'padding-bottom': '100px',
                         'padding-top': '50px'},
                  children=[
                      dbc.Row(children=[
                          dbc.Col(children=[
                              html.H2('MULTI-PAGE DASHBOARD',
                                      style={'textAlign': 'center', 'font-weight': 'bold', 'color': 'red',
                                             'font-size': '200%'}), ], )], justify='center'),
                      dbc.Container(style={'padding-top': '100px'}, children=[
                          dbc.Row(children=[
                              dbc.Col(children=[
                                  dbc.Card([
                                      dbc.CardBody(style={'background-image': 'url("/assets/grad.webp"',
                                                          'color': 'white', 'border-radius': '15px',
                                                          'padding-top': '20px', 'padding-bottom': '20px'}, children=[
                                          dbc.Row(children=[
                                              dbc.Col(html.H2("Sign in", className="text-center mb-4",
                                                              style={'textAlign': 'center', 'font-weight': 'bold',
                                                                     'color': 'white'}),
                                                      width=12)]),
                                          html.Hr(),
                                          dbc.Label("Username:", html_for="username-input"),
                                          dcc.Input(id='username-input', type='text', placeholder='Enter Username',
                                                    className="form-control mb-3"),
                                          dbc.Label("Password:", html_for="password-input"),
                                          dcc.Input(id='password-input', type='password', placeholder='Enter Password',
                                                    className="form-control mb-3"),
                                          html.Br(),
                                          dbc.Row(children=[
                                              dbc.Col(children=[
                                                  dbc.Button("Login", id='login-btn',
                                                             color="primary", className='text-center', outline=True,
                                                             size='md', style={'padding-left': '45px',
                                                                               'padding-right': '45px'}), ],
                                                  width=4)], justify="evenly"),
                                          html.Br(),
                                          dbc.Row(children=[dbc.Col(children=[html.H5(id='login-output'), ],
                                                                    width=4, style={'color': 'red'}
                                                                    )],
                                                  justify="center"),
                                          html.Hr(),
                                          dbc.Row(children=[
                                              dbc.Col(
                                                  dbc.Button("Reset Password", id='reset-btn', color="light",
                                                             outline=True, className='mt-1', size='md',
                                                             style={'padding-left': '90px', 'padding-right': '60px'}),
                                                  width=7
                                              )],
                                              justify="center"), ])])], width=4)], justify="center"),
                      ], fluid=True)])


@callback(Output('token', 'data', allow_duplicate=True),
          Output('full_name-store', 'data'),
          Output('email-store', 'data'),
          Output('login-output', 'children'),
          Output('url', 'pathname', allow_duplicate=True),
          Input('login-btn', 'n_clicks'),
          State('username-input', 'value'),
          State('password-input', 'value'),
          config_prevent_initial_callbacks=True,
          )
def log_in(n_clicks, username, password):
    if not n_clicks or username is None or password is None:
        raise PreventUpdate
    if username in credentials.index and password == credentials.loc[username, 'Password']:
        access_token = random.randint(0, 100000)
        full_name = credentials.loc[username, 'Full Name']
        email = credentials.loc[username, 'Email']
        return access_token, full_name, email, None, '/home'
    else:
        return None, None, None, 'Wrong Username or Password.', '/'
