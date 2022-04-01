
# from pydoc import classname
from tkinter.ttk import Style
from turtle import width
from dash import html, dcc
from dash.dependencies import Input, Output, State


import dash_bootstrap_components as dbc

# import app.py
from app import app
# from app import server


# import all pages 
from pages import home, battery, swap_station


server=app.server


######################## Define header componensts #########################

header = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [dbc.Col(html.Img(src=app.get_asset_url("kofa_logo_black.png"), height="30px")),
                    dbc.Col(dbc.NavbarBrand("Operations Dasboard", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="/",
                style={"textDecoration": "none"},
            ),
            dbc.Row(
                [
                    dbc.NavbarToggler(id="navbar-toggler"),
                    dbc.Collapse(
                        dbc.Nav(
                            [
                                dbc.NavItem(dbc.NavLink("Home",href="/pages/home")),
                                dbc.NavItem(dbc.NavLink("Battery", href="/pages/battery")),
                                dbc.NavItem(
                                    dbc.NavLink("Swap Stations",href="/pages/swap_stations"),
                                    # add an auto margin after page 2 to
                                    # push later links to end of nav
                                    className="me-auto",
                                ),
                                # dbc.NavItem(dbc.NavLink("Help")),
                                # dbc.NavItem(dbc.NavLink("About")),
                            ],
                            # make sure nav takes up the full width for auto
                            # margin to get applied
                            className="w-100",
                        ),
                        id="navbar-collapse",
                        is_open=False,
                        navbar=True,
                    ),
                ],
                # the row should expand to fill the available horizontal space
                className="flex-grow-1",
            ),
        ],
        fluid=True,
    ),
    dark=True,
    color="black",
    sticky={'offset': '4px'},
)


######################## Define Body components #########################

value= 100
card_style={"border-radius":"30px",
            "height": "220px", "width":"100%",}
icon_style = {"height": "50px", "width":"50px", "background-color":"red"}

value_style = {"font-weight":"900", "font-size":"40px"}
col_style = {"margin-right":"0px"}

# we need to look into how to pass props to component then we can refactor to use a single component
swap_stations_card_content = [
    dbc.CardBody(
        [
            # html.I(className="fas fa-cube", style = icon_style),
            html.Img(src=app.get_asset_url("glossy-transparent-battery-icon-yellow-vector-1538275.jpeg"), height="80px"),
            html.H5(value, className="card-title pt-3", style = value_style),
            html.P("Total Swap Stations",className="text-center pt-3", style={ "font-size":"16px"}),
        ]
    ),
]
 #public card co
public_card_content = [
    dbc.CardBody(
        [
            # html.I(className="fas fa-cube", style = icon_style),
            html.Img(src=app.get_asset_url("glossy-transparent-battery-icon-yellow-vector-1538275.jpeg"), height="80px"),
            html.H5(value, className="card-title pt-3", style = value_style),
            html.P("Public",className="text-center pt-3", style={ "font-size":"16px"}),
        ]
    ),
]
 #public card co
private_card_content = [
    dbc.CardBody(
        [
            # html.I(className="fas fa-cube", style = icon_style),
            html.Img(src=app.get_asset_url("glossy-transparent-battery-icon-yellow-vector-1538275.jpeg"), height="80px"),
            html.H5(value, className="card-title pt-3", style = value_style),
            html.P("Private",className="text-center pt-3", style={ "font-size":"16px"}),
        ]
    ),
]

 #public card co
riders_card_content = [
    dbc.CardBody(
        [
            # html.I(className="fas fa-cube", style = icon_style),
            html.Img(src=app.get_asset_url("glossy-transparent-battery-icon-yellow-vector-1538275.jpeg"), height="80px"),
            html.H5(value, className="card-title pt-3", style = value_style),
            html.P("Riders",className="text-center pt-3", style={ "font-size":"16px"}),
        ]
    ),
]
 #public card co
batteries_card_content = [
    dbc.CardBody(
        [
            # html.I(className="fas fa-cube", style = icon_style),
            html.Img(src=app.get_asset_url("glossy-transparent-battery-icon-yellow-vector-1538275.jpeg"), height="80px"),
            html.H5(value, className="card-title pt-3", style = value_style),
            html.P("Total Batterries in Network",className="text-center pt-3", style={ "font-size":"16px"}),
        ]
    ),
]
 #public card co
swaps_card_content = [
    dbc.CardBody(
        [
            # html.I(className="fas fa-cube", style = icon_style),
            html.Img(src=app.get_asset_url("glossy-transparent-battery-icon-yellow-vector-1538275.jpeg"), height="80px"),
            html.H5(value, className="card-title pt-3", style = value_style),
            html.P("Total Swaps",className="text-center pt-3", style={ "font-size":"16px"}),
        ]
    ),
]
 #public card co
distance_card_content = [
    dbc.CardBody(
        [
            # html.I(className="fas fa-cube", style = icon_style),
            html.Img(src=app.get_asset_url("glossy-transparent-battery-icon-yellow-vector-1538275.jpeg"), height="80px"),
            html.H5(value, className="card-title pt-3", style = value_style),
            html.P("Total Distance",className="text-center pt-3", style={ "font-size":"16px"}),
        ]
    ),
]
 #public card co
average_distance_card_content = [
    dbc.CardBody(
        [
            # html.I(className="fas fa-cube", style = icon_style),
            html.Img(src=app.get_asset_url("glossy-transparent-battery-icon-yellow-vector-1538275.jpeg"), height="80px"),
            html.H5(value, className="card-title pt-3", style = value_style),
            html.P("Avg. Distance before Swap",className="text-center pt-3", style={ "font-size":"16px"}),
        ]
    ),
]
cards = html.Div(
    [ dbc.Container([
        dbc.Row(
            [
                dbc.Col(dbc.Card(swap_stations_card_content, color="black", inverse=True,style=card_style), width = 3, style=col_style),
                dbc.Col(dbc.Card(public_card_content, color="black", inverse=True,style=card_style), width = 3, style=col_style),
                dbc.Col(dbc.Card(private_card_content, color="black", inverse=True,style=card_style), width = 3, style=col_style),
                dbc.Col(dbc.Card(riders_card_content, color="black", inverse=True,style=card_style), width = 3, style=col_style),
            ],
            className="mb-4"
        ),
        # row two

             dbc.Row(
            [
                dbc.Col(dbc.Card(batteries_card_content, color="black", inverse=True,style=card_style), width = 3, style=col_style),
                dbc.Col(dbc.Card(swaps_card_content, color="black", inverse=True,style=card_style), width = 3, style=col_style),
                dbc.Col(dbc.Card(distance_card_content, color="black", inverse=True,style=card_style), width = 3, style=col_style),
                dbc.Col(dbc.Card(average_distance_card_content, color="black", inverse=True,style=card_style), width = 3, style=col_style),
            ],
            className="mb-4", style={"margin-top":"40px"}
        )
    ])
    ],style={"margin-top":"100px"}
)




######################## Define footer components #########################











######################## App layout #########################

app.layout = html.Div([
    dcc.Location(id='url', refresh=False), 
    header,
    cards,
    html.Div(id='page-content',
            children=[   ]),
    # dbc.Container(html.P("Content gos here"), className="p-5"),
])


########################################## Build app callbacks ##########################################

@app.callback(Output(component_id='page-content', component_property='children'),
             [Input(component_id='url',component_property= 'pathname')]
             )



def display_page(pathname):
    if pathname == '/pages/home': 
        return home.layout()
    elif pathname == "/pages/battery":
        return battery.layout()
    elif pathname == "/pages/swap_stations":
        return swap_station.layout()
    else:
        return "/"



if __name__ == "__main__":
    app.run_server(debug=True)
    




#area of a circle
def area_circle(radius):
    return 3.14*(radius**2)



def area_rectangle(length, width):
    return length*width

def area_triangle(base, height):
    return base*height/2


#function to change passwords
def change_password(old_password, new_password):
    new_password = new_password.encode('utf-8')
    old_password = old_password.encode('utf-8')
    if old_password == new_password:
        return False
    else:
        return True 
        