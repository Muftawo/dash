# import dependencies
import dash
import dash_bootstrap_components as dbc


FONT_AWESOME = (
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
)

app = dash.Dash(
    __name__,
    meta_tags=[{"name": "viewport", "content": "width=device-width"}],
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP,dbc.icons.FONT_AWESOME],
)
app.title = "Operational Dashboard"

