import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import requests
from datetime import datetime
import pytz

# Constants for IP and port
IP_ADDRESS = "20.206.144.151"
PORT_STH = 8666
DASH_HOST = "0.0.0.0"  # Set this to "0.0.0.0" to allow access from any IP

# Function to get data from the API
def get_data(attribute, lastN):
    url = f"http://{IP_ADDRESS}:{PORT_STH}/STH/v1/contextEntities/type/Lamp/id/urn:ngsi-ld:Lamp:003x/attributes/{attribute}?lastN={lastN}"
    headers = {
        'fiware-service': 'smart',
        'fiware-servicepath': '/'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        try:
            values = data['contextResponses'][0]['contextElement']['attributes'][0]['values']
            return values
        except KeyError as e:
            print(f"Key error for {attribute}: {e}")
            return []
    else:
        print(f"Error accessing {url}: {response.status_code}")
        return []

# Function to convert UTC timestamps to Lisbon time
def convert_to_lisbon_time(timestamps):
    utc = pytz.utc
    lisbon = pytz.timezone('Europe/Lisbon')
    converted_timestamps = []
    for timestamp in timestamps:
        try:
            timestamp = timestamp.replace('T', ' ').replace('Z', '')
            converted_time = utc.localize(datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f')).astimezone(lisbon)
        except ValueError:
            # Handle case where milliseconds are not present
            converted_time = utc.localize(datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')).astimezone(lisbon)
        converted_timestamps.append(converted_time)
    return converted_timestamps

# Set lastN value
lastN = 10  # Get 10 most recent points at each interval

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Environmental Data Viewer'),
    dcc.Graph(id='environmental-graph'),
    dcc.Store(id='environmental-data-store', data={
        'timestamps': [],
        'luminosity_values': [],
        'temperature_values': [],
        'humidity_values': []
    }),
    dcc.Interval(
        id='interval-component',
        interval=10*1000,  # in milliseconds (10 seconds)
        n_intervals=0
    )
])

@app.callback(
    Output('environmental-data-store', 'data'),
    Input('interval-component', 'n_intervals'),
    State('environmental-data-store', 'data')
)
def update_data_store(n, stored_data):
    # Get data for luminosity, temperature, and humidity
    data_luminosity = get_data('luminosity', lastN)
    data_temperature = get_data('temperature', lastN)
    data_humidity = get_data('humidity', lastN)

    if data_luminosity and data_temperature and data_humidity:
        # Extract values and timestamps
        luminosity_values = [float(entry['attrValue']) for entry in data_luminosity]
        temperature_values = [float(entry['attrValue']) for entry in data_temperature]
        humidity_values = [float(entry['attrValue']) for entry in data_humidity]
        timestamps = [entry['recvTime'] for entry in data_luminosity]  # Assuming timestamps are similar

        # Convert timestamps to Lisbon time
        timestamps = convert_to_lisbon_time(timestamps)

        # Append new data to stored data
        stored_data['timestamps'].extend(timestamps)
        stored_data['luminosity_values'].extend(luminosity_values)
        stored_data['temperature_values'].extend(temperature_values)
        stored_data['humidity_values'].extend(humidity_values)

        return stored_data

    return stored_data

@app.callback(
    Output('environmental-graph', 'figure'),
    Input('environmental-data-store', 'data')
)
def update_graph(stored_data):
    if stored_data['timestamps']:
        # Create traces for the plot
        trace_luminosity = go.Scatter(
            x=stored_data['timestamps'],
            y=stored_data['luminosity_values'],
            mode='lines+markers',
            name='Luminosity',
            line=dict(color='orange')
        )
        trace_temperature = go.Scatter(
            x=stored_data['timestamps'],
            y=stored_data['temperature_values'],
            mode='lines+markers',
            name='Temperature',
            line=dict(color='red')
        )
        trace_humidity = go.Scatter(
            x=stored_data['timestamps'],
            y=stored_data['humidity_values'],
            mode='lines+markers',
            name='Humidity',
            line=dict(color='blue')
        )

        # Create figure
        fig = go.Figure(data=[trace_luminosity, trace_temperature, trace_humidity])

        # Update layout
        fig.update_layout(
            title='Environmental Data Over Time',
            xaxis_title='Timestamp',
            yaxis_title='Values',
            hovermode='closest'
        )

        return fig

    return {}

if __name__ == '__main__':
    app.run_server(debug=True, host=DASH_HOST, port=8050)
