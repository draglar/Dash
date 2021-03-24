import pandas as pd
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# ---------- Import and clean data (importing csv into pandas)
# age_grouped = pd.read_csv("intro_bees.csv")
df = pd.read_csv("~/Documents/Dsea/Train_v2.csv")

age_grouped = df.groupby(['country', 'bank_account', 'location_type', 'cellphone_access', 'household_size',
                          'gender_of_respondent', 'relationship_with_head', 'marital_status', 'education_level',
                          'job_type'])[['age_of_respondent']].mean()
age_grouped.reset_index(inplace=True)

print(age_grouped['gender_of_respondent'].value_counts())
# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("Financial inclusion in East Africa", style={'text-align': 'center'}),
    dcc.Dropdown(id="pick_country",
                 options=[
                     {"label": 'Kenya', "value": 'Kenya'},
                     {"label": 'Rwanda', "value": 'Rwanda'},
                     {"label": 'Tanzania', "value": 'Tanzania'},
                     {"label": 'Uganda', "value": 'Uganda'}],
                 multi=False,
                 value='Kenya',
                 style={'width': "35%", 'float': 'left'}
                 ),
    dcc.Dropdown(id="all_or_custom",
                 options=[
                     {"label": 'all', "value": 'all'},
                     {"label": 'custom', "value": 'custom'}],
                 multi=False,
                 value='all',
                 style={'width': "25%", 'float': 'right'}
                 ),
    # html.Div(id='output_container', children=[]),
    html.Br(),
    dcc.Graph(id='bank_accounts', figure={}, style={'width': "50%", 'float': 'left'}),
    dcc.Graph(id='locations', figure={}, style={'width': "50%", 'float': 'right'}),
    dcc.Graph(id='cellphones', figure={}, style={'width': "50%", 'float': 'left'}),
    dcc.Graph(id='genders', figure={}, style={'width': "50%", 'float': 'right'})
    # dcc.Graph(id='bank_accounts', figure={}, style={'width': "50%", 'float': 'right'})

])


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [#Output(component_id='output_container', component_property='children'),
     Output(component_id='bank_accounts', component_property='figure'),
     Output(component_id='locations', component_property='figure'),
     Output(component_id='cellphones', component_property='figure'),
     Output(component_id='genders', component_property='figure'),
     #      Output(component_id='Totals',component_property='children') bank, location, cellphone, gender
     ],
    [Input(component_id='pick_country', component_property='value')]
)
def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "The country chosen by user is : {}".format(option_slctd)

    age_groupedf = age_grouped.copy()
    age_groupedf = age_groupedf[age_groupedf['country'] == option_slctd]
    #     age_groupedf = age_groupedf[age_groupedf["Affected by"] == "Varroa_mites"]

    bank = px.pie(
        age_groupedf,
        names='bank_account',
        title='Bank accounts',
        template='plotly_dark',
        color_discrete_sequence=['#038b8d', '#8d0830']
    )
    location = px.pie(
        age_groupedf,
        names='location_type',
        title='Location types',
        template='plotly_dark',
        color_discrete_sequence=['#038b8d', '#8d0830']
    )
    cellphone = px.pie(
        age_groupedf,
        names='cellphone_access',
        title='Cellphone access',
        template='plotly_dark',
        color_discrete_sequence=['#038b8d', '#8d0830']
    )
    gender = px.pie(
        age_groupedf,
        names='gender_of_respondent',
        title='Genders',
        template='plotly_dark',
        color_discrete_sequence=['#038b8d', '#8d0830']
    )
    bank.update_layout(title_x=0.5,title_font_family='kollektif',title_font_size=30, legend_font_family='kollektif',legend_font_size=20)
    location.update_layout(title_x=0.5,title_font_family='kollektif',title_font_size=30, legend_font_family='kollektif',legend_font_size=20)
    cellphone.update_layout(title_x=0.5,title_font_family='kollektif',title_font_size=30, legend_font_family='kollektif',legend_font_size=20)
    gender.update_layout(title_x=0.5,title_font_family='kollektif',title_font_size=30, legend_font_family='kollektif',legend_font_size=20)
#removes
    return bank, location, cellphone, gender


if __name__ == '__main__':
    app.run_server(debug=True)
