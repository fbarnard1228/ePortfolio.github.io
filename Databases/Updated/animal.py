# Import necessary modules
from jupyter_dash import JupyterDash
import dash_leaflet as dl
from dash import dcc, html, dash_table
import plotly.express as px
from dash.dependencies import Input, Output, State
import base64
import pandas as pd
import logging
from animal_shelter import AnimalShelter

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Setup the JupyterDash app
app = JupyterDash(__name__)

# Load and encode the logo image
image_filename = 'Grazioso Salvare Logo.png'
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

# Initialize database connection
username = "farrik"
password = "SNHU1234"
db = AnimalShelter(username, password)

# Function to load data from the database
def load_data(filter_criteria={}):
    try:
        df = pd.DataFrame.from_records(db.read(filter_criteria))
        if '_id' in df.columns:
            df.drop(columns=['_id'], inplace=True)
        return df
    except Exception as e:
        logger.error(f"Error loading data: {e}")
        return pd.DataFrame()

# Custom CSS
custom_css = {
    'backgroundColor': '#f9f9f9',
    'padding': '20px',
    'margin': '20px',
    'borderRadius': '5px',
    'boxShadow': '2px 2px 2px lightgrey'
}

# Layout for the dashboard
def create_layout():
    return html.Div(style=custom_css, children=[
        html.Div(id='hidden-div', style={'display': 'none'}),
        html.Center(html.B(html.H1('CS-499 Updated Dashboard Farrik Barnard', style={'color': '#333'}))),
        html.Center(html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()), style={'height': '150px'})),
        html.Hr(),
        html.Div(dcc.RadioItems(
            id='filter_type',
            options=[
                {'label': 'Water Rescue', 'value': 'Water'},
                {'label': 'Mountain Rescue', 'value': 'Mountain'},
                {'label': 'Disaster Rescue', 'value': 'Disaster'},
                {'label': 'Reset', 'value': 'Reset'}
            ],
            value='Reset',
            labelStyle={'display': 'inline-block', 'margin': '10px'}
        )),
        html.Hr(),
        dash_table.DataTable(
            id='datatable-id',
            columns=[{"name": i, "id": i, "deletable": False, "selectable": True} for i in load_data().columns],
            data=load_data().to_dict('records'),
            editable=False,
            sort_mode="multi",
            sort_action='native',
            filter_action='native',
            page_action='native',
            page_size=10,
            row_selectable="single",
            selected_rows=[0],
            style_table={'overflowX': 'auto'},
            style_cell={
                'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                'whiteSpace': 'normal',
                'textAlign': 'center',
                'border': '1px solid grey',
            },
            style_header={
                'backgroundColor': '#333',
                'fontWeight': 'bold',
                'color': 'white'
            },
            style_data={
                'backgroundColor': '#f9f9f9',
                'color': 'black'
            },
            style_data_conditional=[
                {
                    'if': {'column_id': 'animal_type'},
                    'backgroundColor': '#ffebcd'
                },
                {
                    'if': {'column_id': 'breed'},
                    'backgroundColor': '#e6e6fa'
                },
            ]
        ),
        html.Br(),
        html.Hr(),
        html.Div(className='row', style={'display': 'flex'}, children=[
            html.Div(id='graph-id', className='col s12 m6', style={'padding': '10px'}),
            html.Div(id='map-id', className='col s12 m6', style={'padding': '10px'})
        ])
    ])

app.layout = create_layout()

# Callbacks for updating components based on user interaction
@app.callback(
    Output('datatable-id', 'data'),
    Input('filter_type', 'value')
)
def update_dashboard(filter_type):
    filter_criteria = {}
    if filter_type == 'Water':
        filter_criteria = {
            "animal_type": "Dog",
            "breed": {"$in": ["Labrador Retriever Mix", "Chesapeake Bay Retriever", "Newfoundland"]},
            "sex_upon_outcome": "Intact Female",
            "age_upon_outcome_in_weeks": {"$gte": 26.0, "$lte": 156.0}
        }
    elif filter_type == 'Mountain':
        filter_criteria = {
            "animal_type": "Dog",
            "breed": {"$in": ["German Shepherd", "Alaskan Malamute", "Old English Sheepdog", "Siberian Husky", "Rottweiler"]},
            "sex_upon_outcome": "Intact Male",
            "age_upon_outcome_in_weeks": {"$gte": 26.0, "$lte": 156.0}
        }
    elif filter_type == 'Disaster':
        filter_criteria = {
            "animal_type": "Dog",
            "breed": {"$in": ["Doberman Pinscher", "German Shepherd", "Golden Retriever", "Bloodhound", "Rottweiler"]},
            "sex_upon_outcome": "Intact Male",
            "age_upon_outcome_in_weeks": {"$gte": 20.0, "$lte": 300.0}
        }
    df = load_data(filter_criteria)
    return df.to_dict('records')


@app.callback(
    Output('graph-id', "children"),
    Input('datatable-id', "derived_virtual_data")
)

def update_graphs(viewData):
    try:
        dff = pd.DataFrame.from_dict(viewData)
        
        if dff.empty:
            logger.error("DataFrame is empty. Cannot create histogram.")
            return [html.Div("No data available to display the histogram.", style={'color': 'red', 'textAlign': 'center'})]
        
        if 'breed' not in dff.columns:
            logger.error("Required column 'breed' not found in DataFrame.")
            return [html.Div("Required column 'breed' not found in data.", style={'color': 'red', 'textAlign': 'center'})]

        fig = px.histogram(dff, x='breed', title='Available Dogs by Breed', color='breed',
                           color_discrete_sequence=px.colors.qualitative.Set3,
                           template='plotly_dark')
        return [
            dcc.Graph(figure=fig)
        ]
    
    except Exception as e:
        logger.error(f"Error creating histogram: {e}")
        return [html.Div("An error occurred while creating the histogram.", style={'color': 'red', 'textAlign': 'center'})]


@app.callback(
    Output('datatable-id', 'style_data_conditional'),
    Input('datatable-id', 'selected_columns')
)
def update_styles(selected_columns):
    try:
        if not selected_columns:
            return []

        return [{
            'if': {'column_id': i},
            'background_color': '#D2F3FF'
        } for i in selected_columns]

    except Exception as e:
        logger.error(f"Error updating styles: {e}")
        return []


@app.callback(
    Output('map-id', "children"),
    [Input('datatable-id', "derived_virtual_data"),
     Input('datatable-id', "derived_virtual_selected_rows")]
)
def update_map(viewData, index):  
    dff = pd.DataFrame.from_dict(viewData)
    # Ensure that we have a selected row to display
    if index is None:
       row = 0
    else: 
       row = index[0]
        # Assuming dff has a row for the selected animal, we take the first one for the marker
    return[
            dl.Map(style={'width': '1000px', 'height': '500px'}, 
               center=[30.75, -97.48], zoom=10, children=[
                dl.TileLayer(id="base-layer-id"),
                # Marker with tool tip and popup
                # Column 13 and 14 define the grid-coordinates for 
                # the map
                # Column 4 defines the breed for the animal
                # Column 9 defines the name of the animal
                dl.Marker(position=[dff.iloc[row,13],dff.iloc[row,14]], 
                    children=[
                    dl.Tooltip(dff.iloc[row,4]),
                    dl.Popup([
                        html.H1("Animal Name"),
                        html.P(dff.iloc[row,9]) 
                    ])
                ])
            ])
        ]

if __name__ == '__main__':
    app.run_server(debug=True, mode='inline')

