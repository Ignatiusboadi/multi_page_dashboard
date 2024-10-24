from app import app
from dash import dcc, html, ctx, callback
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import login

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
    dcc.Store(id='token', data=None),
    dcc.Store(id='full_name-store', data=None),
    dcc.Store(id='email-store', data=None),
    dbc.Row(children=[
        dbc.Col(html.H5([html.I(className='fa fa-copyright'), ' Group 1 2024'], style={'padding-top': '5px'}),
                width={"size": 2, 'offset': 10})])])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'),
              Input('token', 'data'))
def display_page(pathname, token):
    if pathname == '/' or not token:
        return login.layout
    else:
        return '404: Page not found'


if __name__ == '__main__':
    app.run_server(debug=True, port=8050)