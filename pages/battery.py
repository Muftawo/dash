#import depende

import dash 
from dash import html, dcc
from dash.dependencies import Input, Output, State

import dash_bootstrap_components as dbc



from app import app

######################### Build layout Components #########################


def layout():
    return [
        dbc.Row(
            children=[
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            children=[
                                dbc.CardHeader("Battery Board"),
                                html.Div( id="battery-live-log"),
                            ]
                        )
                    ), 
                    width={"size": 6, "offset": 3}, #check the width size later , you set width = 4 or 6
                ),
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            children=[
                                dbc.CardHeader("Battery Live Locations"),
                                dcc.Graph(id="battery-live-map"),
                            ]
                        )
                    ),
                    width={"size": 8, "offset": 3},
                ),
            ]  
        )
    ]

                    


######################### Build app callbacks #########################

@app.callback(
    Output("battery-live-log", "children"),
    [Input("battery-live-map", "clickData")]
)
def update_live_log(clickData):
    if clickData is None:
        return "No data to display"
    else:
        return "You clicked on %s" % (clickData["points"][0]["text"])   