# importing libraries

from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv(
    r"C:\Users\mohsun.haziyev\Desktop\Dash_plotly_development\commodity_trade_statistics_data.csv")

# Create the Dash app
app = Dash(__name__)

# Set up the app layout

app.layout = html.Div(children=[html.H1(children="Commodity Trade Dashboard"),
                                dcc.Dropdown(id="geo-dropdown",
                                             options=[{"label": i, "value": i}
                                                      for i in df["country_or_area"].unique()],
                                             value='USA'),
                                dcc.Graph(id="trade-graph")

                                ])

# Set up the callback function


@app.callback(Output(component_id="trade-graph", component_property="figure"),
              Input(component_id="geo-dropdown", component_property="value")
              )
def update_graph(selected_country):
    filtered_country = df[df["country_or_area"] == selected_country]
    line_graph = px.line(filtered_country,
                         x="year", y="trade_usd", color="flow",
                         title="Comodity trade in {0}".format(selected_country))
    return line_graph


# Run local server
if __name__ == '__main__':
    app.run_server(debug=True)
