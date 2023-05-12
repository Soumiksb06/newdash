import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import dash
from dash import dcc
from dash import html
from jupyter_dash import JupyterDash
import json
import plotly.graph_objects as go
import plotly.utils
import base64
import io
import plotly.graph_objects as go

# Set the working directory
# Assumes the CSV file is in the specified directory
# Replace 'C:/Users/soumi/Downloads/TAL R/intern R' with your desired directory path
import os
#os.chdir('C:/Users/soumi/Downloads/TAL R/intern R')

# Read the CSV file using pandas
dta = pd.read_csv("C:/Users/soumi/Downloads/TAL R/intern R/Dummy Data HSS.csv")

# Create the Dash app
app = JupyterDash(__name__)
server = app.server

app.layout = html.Div(children=[
    html.H1(children='sb6'),
    dcc.Tabs(id='tabs', children=[
        dcc.Tab(label='Sales', children=[
            dcc.Graph(id='plot_sales'),
            dcc.Dropdown(id='features-sales', options=[
                {'label': 'TV', 'value': 'TV'},
                {'label': 'Radio', 'value': 'Radio'},
                {'label': 'SocialMedia', 'value': 'Social Media'},
            ], value='TV')
        ]),
        dcc.Tab(label='TV', children=[
            dcc.Graph(id='plot_tv'),
            dcc.Dropdown(id='features-tv', options=[
                {'label': 'TV', 'value': 'TV'},
                {'label': 'Radio', 'value': 'Radio'},
                {'label': 'SocialMedia', 'value': 'Social Media'},
                {'label': 'Sales', 'value': 'Sales'}
            ], value='TV')
        ]),
        dcc.Tab(label='Radio', children=[
            dcc.Graph(id='plot_radio'),
            dcc.Dropdown(id='features-radio', options=[
                {'label': 'TV', 'value': 'TV'},
                {'label': 'Radio', 'value': 'Radio'},
                {'label': 'SocialMedia', 'value': 'Social Media'},
                {'label': 'Sales', 'value': 'Sales'}
            ], value='TV')
        ]),
        dcc.Tab(label='SocialMedia', children=[
            dcc.Graph(id='plot_social'),
            dcc.Dropdown(id='features-social', options=[
                {'label': 'TV', 'value': 'TV'},
                {'label': 'Radio', 'value': 'Radio'},
                {'label': 'SocialMedia', 'value': 'Social Media'},
                {'label': 'Sales', 'value': 'Sales'}
            ], value='TV')
        ])
    ])
])


# Define the callback functions



@app.callback(
    dash.dependencies.Output('plot_sales', 'figure'),
    [dash.dependencies.Input('features-sales', 'value')]
)
def update_plot_sales(selected_feature):
    fig, ax = plt.subplots()
    sns.lineplot(data=dta, x='Sales', y=selected_feature, color='blue', linewidth=1, ax=ax)
    sns.scatterplot(data=dta, x='Sales', y=selected_feature, color='pink', ax=ax)

    buf = io.BytesIO()
    fig.canvas.print_png(buf)
    buf.seek(0)
    encoded_image = base64.b64encode(buf.getvalue()).decode('utf-8')

    plotly_fig = go.Figure()
    plotly_fig.add_layout_image(
        source=f"data:image/png;base64,{encoded_image}",
        x=0, y=1, xref="paper", yref="paper",
        sizex=1, sizey=1, sizing="stretch",
        layer="below"
    )
    plotly_fig.update_layout(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        autosize=True,
        margin=dict(l=0, r=0, t=0, b=0)
    )

    return plotly_fig


@app.callback(
    dash.dependencies.Output('plot_tv', 'figure'),
    [dash.dependencies.Input('features-tv', 'value')]
)
def update_plot_tv(selected_feature):
    fig, ax = plt.subplots()
    sns.lineplot(data=dta, x='TV', y=selected_feature, color='blue', linewidth=1, ax=ax)
    sns.scatterplot(data=dta, x='TV', y=selected_feature, color='pink', ax=ax)

    buf = io.BytesIO()
    fig.canvas.print_png(buf)
    buf.seek(0)
    encoded_image = base64.b64encode(buf.getvalue()).decode('utf-8')

    plotly_fig = go.Figure()
    plotly_fig.add_layout_image(
        source=f"data:image/png;base64,{encoded_image}",
        x=0, y=1, xref="paper", yref="paper",
        sizex=1, sizey=1, sizing="stretch",
        layer="below"
    )
    plotly_fig.update_layout(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        autosize=True,
        margin=dict(l=0, r=0, t=0, b=0)
    )

    return plotly_fig


@app.callback(
    dash.dependencies.Output('plot_radio', 'figure'),
    [dash.dependencies.Input('features-radio', 'value')]
)
def update_plot_radio(selected_feature):
    fig, ax = plt.subplots()
    sns.lineplot(data=dta, x='Radio', y=selected_feature, color='blue', linewidth=1, ax=ax)
    sns.scatterplot(data=dta, x='Radio', y=selected_feature, color='pink', ax=ax)

    buf = io.BytesIO()
    fig.canvas.print_png(buf)
    buf.seek(0)
    encoded_image = base64.b64encode(buf.getvalue()).decode('utf-8')

    plotly_fig = go.Figure()
    plotly_fig.add_layout_image(
        source=f"data:image/png;base64,{encoded_image}",
        x=0, y=1, xref="paper", yref="paper",
        sizex=1, sizey=1, sizing="stretch",
        layer="below"
    )
    plotly_fig.update_layout(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        autosize=True,
        margin=dict(l=0, r=0, t=0, b=0)
    )

    return plotly_fig


@app.callback(
    dash.dependencies.Output('plot_social', 'figure'),
    [dash.dependencies.Input('features-social', 'value')]
)
def update_plot_social(selected_feature):
    fig, ax = plt.subplots()
    sns.lineplot(data=dta, x='Social Media', y=selected_feature, color='blue', linewidth=1, ax=ax)
    sns.scatterplot(data=dta, x='Social Media', y=selected_feature, color='pink', ax=ax)

    buf = io.BytesIO()
    fig.canvas.print_png(buf)
    buf.seek(0)
    encoded_image = base64.b64encode(buf.getvalue()).decode('utf-8')

    plotly_fig = go.Figure()
    plotly_fig.add_layout_image(
        source=f"data:image/png;base64,{encoded_image}",
        x=0, y=1, xref="paper", yref="paper",
        sizex=1, sizey=1, sizing="stretch",
        layer="below"
    )
    plotly_fig.update_layout(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        autosize=True,
        margin=dict(l=0, r=0, t=0, b=0)
    )

    return plotly_fig


# In[40]:


#Run the app
if __name__ == '__main__':
    try:
        app.run_server(mode='inline')
    except SystemExit:
        pass

