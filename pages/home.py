
from dash import html, dcc
from dash.dependencies import Input, Output, State


import dash_bootstrap_components as dbc


# Define Card components
value= 100

card_content = [
    dbc.CardHeader("Card header"),
    dbc.CardBody(
        [
            html.H5(value, className="card-title"),
            html.P(value,className="card-text"),
        ]
    ),
]
cards = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(dbc.Card(card_content, color="black", inverse=True)),
                dbc.Col(dbc.Card(card_content, color="black", inverse=True)),
                dbc.Col(dbc.Card(card_content, color="black", inverse=True)),
                dbc.Col(dbc.Card(card_content, color="black", inverse=True)),
            ],
            className="mb-4",
        ),
        dbc.Row(
            [
                dbc.Col(dbc.Card(card_content, color="black", inverse=True)),
                dbc.Col(dbc.Card(card_content, color="black", inverse=True)),
                dbc.Col(dbc.Card(card_content, color="black", inverse=True)),
                dbc.Col(dbc.Card(card_content, color="black", inverse=True)),
            ],
            className="mb-4",
        ),
    ]
)
