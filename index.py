from app import app
from dash import dcc, html, ctx, callback
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import login, home_page

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
              Output('url', 'pathname'),
              Input('url', 'pathname'),
              Input('token', 'data'),
              Input('full_name-store', 'data'),
              Input('email-store', 'data'))
def display_page(pathname, token, full_name, email):
    if pathname == '/' or not token:
        return login.layout, '/login'
    elif token:
        return home_page.layout, pathname
    else:
        return '404: Page not found', '/'


if __name__ == '__main__':
    app.run_server(debug=True, port=8050)