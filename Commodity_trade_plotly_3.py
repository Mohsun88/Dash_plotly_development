# importing libraries

from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv(
    r"C:\Users\mohsun.haziyev\Desktop\Dash_plotly_development\commodity_trade_statistics_data.csv")

# Create the Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.VAPOR])
title = dcc.Markdown(children='# The App analyzes Commodity sales')
graph = dcc.Graph(figure={})
dropdown = dcc.Dropdown(options=['Histogram', 'Scatter Plot'],
                        value='Histogram',  # initial value is displayed when page firstly loads
                        clearable=False)

# Customizing the Layout
app.layout = dbc.Container([title, graph, dropdown])

#  Calling the callback function to allow  components to interact


@app.callback(
    Output(component_id=graph, component_property='figure'),
    Input(component_id=dropdown, component_property='value')
)
def update_graph(user_input):  # function arguments based on component property of the Input
    if user_input == 'Histogram':
        fig = px.histogram(data_frame=df, x="year",
                           y="quantity", color="flow")

    elif user_input == 'Scatter Plot':
        fig = px.scatter(data_frame=df, x="year", y="quantity", color="flow",
                         symbol="flow")

    return fig


# Run local server
if __name__ == '__main__':
    app.run_server(debug=True)
