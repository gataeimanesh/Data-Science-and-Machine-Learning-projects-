import dash
from dash import dcc
from dash import html
import pandas as pd
import plotly.graph_objects as go

# Read the heart-2020 data from CSV file (replace 'heart-2020.csv' with the actual file path)
heart_data = pd.read_csv(r"C:\Users\gatae\OneDrive\Desktop\heart_2020.csv")

# Create a Dash app
app = dash.Dash(__name__)

# Define colors for the scatter plot
scatter_plot_color = 'rgb(31, 119, 180)'  # Blue color for scatter plot

# Define the layout of the app
app.layout = html.Div(style={'backgroundColor': '#f2f2f2', 'padding': '20px'}, children=[
    html.H1("Heart-2020 Data Dashboard", style={'textAlign': 'center', 'color': '#1f77b4', 'margin-bottom': '20px'}),
    html.Div([
        dcc.Graph(
            id='scatter-plot',
            figure={
                'data': [
                    go.Scatter(x=heart_data['BMI'], y=heart_data['SleepTime'], mode='markers', marker=dict(color=scatter_plot_color), name='BMI vs. SleepTime')
                ],
                'layout': {
                    'title': 'BMI vs. SleepTime (Scatter Plot)',
                    'title_font': dict(size=24),
                    'xaxis': {'title': 'BMI', 'title_font': dict(size=18)},
                    'yaxis': {'title': 'SleepTime', 'title_font': dict(size=18)},
                    'plot_bgcolor': '#ffffff',
                    'paper_bgcolor': '#f2f2f2'
                }
            }
        )
    ])
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
