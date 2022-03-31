#import depende

import dash 
from dash import html, dcc
from dash.dependencies import Input, Output, State

import dash_bootstrap_components as dbc



from app import app

######################### Build layout Components #########################


def layout():
    html.Div([
    html.Div([
        dcc.Input(id="stock-input", value="SPY", type="text"),
        html.Button(id="submit-button", n_clicks=0, children="Submit")
    ]),

    html.Div([
        html.Div([
            dcc.Graph(
                id="graph_close",
            )
        ], className="six columns"),

        html.Div([
            html.H3("Market News"),
        ], className="six columns"),

    ],className="row")
])
                    


######################### Build app callbacks #########################

@app.callback(
    Output("ss-tabel", "children"),
    [Input("ss-live-map", "clickData")]
)
def update_live_log(clickData):
    if clickData is None:
        return "No data to display"
    else:
        return "You clicked on %s" % (clickData["points"][0]["text"])   