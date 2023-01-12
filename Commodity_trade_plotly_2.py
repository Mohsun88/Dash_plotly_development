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
app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])
title = dcc.Markdown(children='')
graph = dcc.Graph(figure={})
dropdown = dcc.Dropdown(options=df.columns.values[2:],
                        value='quantity',  # initial value displayed when page first loads
                        clearable=False)

# Set up the app layout

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([title], width=6)
    ], justify='center'),
    dbc.Row([
        dbc.Col([graph], width=12)
    ]),
    dbc.Row([
        dbc.Col([dropdown], width=6)
    ], justify='center'),

], fluid=True)

# Calling the callback function to allow  components to interact


@app.callback(
    Output(component_id=graph, component_property='figure'),
    Output(component_id=title, component_property='children'),
    Input(component_id=dropdown, component_property='value')
)
# function arguments based on property of the Input
def update_graph(column_name):

    print(column_name)
    print(type(column_name))
    # https://plotly.com/python/choropleth-maps/
    fig = px.choropleth(data_frame=df,
                        locations='country_or_area',
                        locationmode="country names",
                        scope="world",
                        height=600,
                        color=column_name,
                        animation_frame='year')

    return fig, '# '+column_name


# Run local server
if __name__ == '__main__':
    app.run_server(debug=True)
