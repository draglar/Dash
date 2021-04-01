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
l_allign = {'width': "50%", 'float': 'left'}
r_allign = {'width': "50%", 'float': 'right'}

# print(age_grouped['gender_of_respondent'].value_counts())
app.layout = html.Div([

    html.H1("Financial inclusion in East Africa", style={'text-align': 'center', 'font_family': 'kollektif'}),
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
    dcc.Dropdown(id="varriate",
                 options=[
                     {"label": 'univarriate', "value": 'univarriate'},
                     {"label": 'bivarriate', "value": 'bivarriate'}],
                 multi=False,
                 value='univarriate',
                 style={'width': "35%", 'float': 'right'}
                 ),
    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='bank_accounts', figure={}, style=l_allign),
    dcc.Graph(id='locations', figure={}, style=r_allign),
    dcc.Graph(id='cellphones', figure={}, style=l_allign),
    dcc.Graph(id='genders', figure={}, style=r_allign),
    dcc.Graph(id='relationships', figure={}, style=l_allign),
    dcc.Graph(id='marriages', figure={}, style=r_allign),
    dcc.Graph(id='educations', figure={}, style=l_allign),
    dcc.Graph(id='jobs', figure={}, style=r_allign),
    # dcc.Graph(id='bankXjobs', figure={}, style=l_allign),
    # dcc.Graph(id='bankXeducation', figure={}, style=r_allign),
    # dcc.Graph(id='bankXrelation', figure={}, style=l_allign),
    # dcc.Graph(id='bankXmarital', figure={}, style=l_allign),
    # dcc.Graph(id='bankXlocation', figure={}, style=r_allign),
    # dcc.Graph(id='bankXcell', figure={}, style=l_allign),
    # dcc.Graph(id='bankXgender', figure={}, style=r_allign),
    # bank_job, bank_education, bank_relation, bank_marital, bank_location, bank_cell, bank_gender
    # dcc.Graph(id='bank_accounts', figure={},option_slctd style={'width': "50%", 'float': 'right'})

])


# ------------------------------------------------------------------------------
# x = 'all'


# App layout


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
# @app.callback(
#     [Output(component_id='output_container', component_property='children')],
#     [Input(component_id='all_or_custom', component_property='value')]
# )
# def checks(option):
#     x = option
#     container = "The country chosen by user is : {}".format(option)
#     return container
#

# if x == 'all':
@app.callback(
    [  # Output(component_id='output_container', component_property='children'),
        Output(component_id='bank_accounts', component_property='figure'),
        Output(component_id='locations', component_property='figure'),
        Output(component_id='cellphones', component_property='figure'),
        Output(component_id='genders', component_property='figure'),
        Output(component_id='relationships', component_property='figure'),
        Output(component_id='marriages', component_property='figure'),
        Output(component_id='educations', component_property='figure'),
        Output(component_id='jobs', component_property='figure'),

        # Output(component_id='bankXjobs', component_property='figure'),
        # Output(component_id='bankXeducation', component_property='figure'),
        # Output(component_id='bankXrelation', component_property='figure'),
        # Output(component_id='bankXmarital', component_property='figure'),
        # Output(component_id='bankXlocation', component_property='figure'),
        # Output(component_id='bankXcell', component_property='figure'),
        # Output(component_id='bankXgender', component_property='figure'),
        #      Output(component_id='Totals',component_property='children') bank, location, cellphone, gender
    ],
    [Input(component_id='pick_country', component_property='value'),
     Input(component_id='varriate', component_property='value')
     ]
)
def update_graph(option_slctd,variate):
    print(option_slctd)
    # print(type(option_slctd))
    print(variate)
    container = "The country chosen by user is : {}".format(option_slctd)

    by_age = age_grouped.copy()
    by_age = by_age[by_age['country'] == option_slctd]
    #     by_age = by_age[by_age["Affected by"] == "Varroa_mites"]

    # Univariate

    bank = px.pie(
        by_age,
        names='bank_account',
        title='Bank accounts',
        template='plotly_dark',
        color_discrete_sequence=['#038b8d', '#8d0825']
    )
    bank.update_layout(
        title_x=0.5,
        title_font_family='kollektif',
        title_font_size=25,
        legend_font_family='kollektif',
        legend_font_size=20
    )
    if variate == 'univarriate':
        location = px.pie(
            by_age,
            names='location_type',
            title='Location types',
            template='plotly_dark',
            color_discrete_sequence=['#038b8d', '#8d0825']
        )
        location.update_layout(
            title_x=0.5,
            title_font_family='kollektif',
            title_font_size=25,
            legend_font_family='kollektif',
            legend_font_size=20
        )

        cellphone = px.pie(
            by_age,
            names='cellphone_access',
            title='Cellphone access',
            template='plotly_dark',
            color_discrete_sequence=['#038b8d', '#8d0825']
        )
        cellphone.update_layout(
            title_x=0.5,
            title_font_family='kollektif',
            title_font_size=25,
            legend_font_family='kollektif',
            legend_font_size=20
        )

        gender = px.pie(
            by_age,
            names='gender_of_respondent',
            title='Genders',
            template='plotly_dark',
            color_discrete_sequence=['#038b8d', '#8d0825']
        )
        gender.update_layout(
            title_x=0.5,
            title_font_family='kollektif',
            title_font_size=25,
            legend_font_family='kollektif',
            legend_font_size=20
        )

        relationship = px.histogram(
            by_age['relationship_with_head'],
            title='Relation of the respondent to the head of the house',
            orientation='h',
            template='plotly_dark',
            color_discrete_sequence=['#038b8d', '#222222']
        )
        relationship.update_layout(
            title_x=0.5,
            title_font_family='kollektif',
            title_font_size=25,
            legend_font_family='kollektif',
            legend_font_size=20
        )

        marriage = px.histogram(
            by_age['marital_status'],
            title='marital status respondent',
            orientation='h',
            template='plotly_dark',
            color_discrete_sequence=['#038b8d', '#222222']
        )
        marriage.update_layout(
            title_x=0.5,
            title_font_family='kollektif',
            title_font_size=25,
            legend_font_family='kollektif',
            legend_font_size=20
        )

        education = px.histogram(
            by_age['education_level'],
            title='education level respondent',
            orientation='h',
            template='plotly_dark',
            color_discrete_sequence=['#038b8d', '#222222']
        )
        education.update_layout(
            title_x=0.5,
            title_font_family='kollektif',
            title_font_size=25,
            legend_font_family='kollektif',
            legend_font_size=20
        )

        job = px.histogram(
            by_age['job_type'],
            title='job type respondent',
            orientation='h',
            template='plotly_dark',
            color_discrete_sequence=['#038b8d', '#222222']
        )
        job.update_layout(
            title_x=0.5,
            title_font_family='kollektif',
            title_font_size=25,
            legend_font_family='kollektif',
            legend_font_size=20
        )
        return bank, location, cellphone, gender, relationship, marriage, education, job
    else:
        # Bivvariate
        # bank_account x location_type
        bank_location = px.pie(
            by_age,
            names='location_type',
            color='bank_account',
            title='Relationship of bank account to location of the respondent',
            # orientation='h',
            template='plotly_dark',
            color_discrete_sequence=['#038b8d', '#8d0825', 'white']
        )
        bank_location.update_layout(
            title_x=0.5,
            title_font_family='kollektif',
            title_font_size=25,
            legend_font_family='kollektif',
            legend_font_size=20
        )

        # removes
        # bank_account x cellphone_access
        bank_cell = px.histogram(
            by_age,
            y='cellphone_access',
            color='bank_account',
            title='Relationship of bank account to Cellphone access',
            orientation='h',
            template='plotly_dark',
            color_discrete_sequence=['#038b8d', '#8d0825', 'white']
        )
        bank_cell.update_layout(
            title_x=0.5,
            title_font_family='kollektif',
            title_font_size=25,
            legend_font_family='kollektif',
            legend_font_size=20
        )

        # bank_account x gender_of_respondent
        bank_gender = px.histogram(
            by_age,
            y='gender_of_respondent',
            color='bank_account',
            title='Relationship of bank account to Gender of the respondents',
            orientation='h',
            template='plotly_dark',
            color_discrete_sequence=['#038b8d', '#8d0825', 'white']
        )
        bank_gender.update_layout(
            title_x=0.5,
            title_font_family='kollektif',
            title_font_size=25,
            legend_font_family='kollektif',
            legend_font_size=20
        )

        # bank_account x relationship_with_head
        bank_relation = px.histogram(
            by_age,
            y='relationship_with_head',
            color='bank_account',
            title='Relationship of bank account to',
            orientation='h',
            template='plotly_dark',
            color_discrete_sequence=['#038b8d', '#8d0825', 'white']
        )
        bank_relation.update_layout(
            title_x=0.5,
            title_font_family='kollektif',
            title_font_size=25,
            legend_font_family='kollektif',
            legend_font_size=20
        )

        # bank_account x marital_status
        bank_marital = px.histogram(
            by_age,
            y='marital_status',
            color='bank_account',
            title='Relationship of bank account to the marital status of the respondent',
            orientation='h',
            template='plotly_dark',
            color_discrete_sequence=['#038b8d', '#8d0825', 'white']
        )
        bank_marital.update_layout(
            title_x=0.5,
            title_font_family='kollektif',
            title_font_size=25,
            legend_font_family='kollektif',
            legend_font_size=20
        )

        # bank_account x education_level
        bank_education = px.histogram(
            by_age,
            y='education_level',
            color='bank_account',
            title='Relationship of bank account to the education level of the respondent',
            orientation='h',
            template='plotly_dark',
            color_discrete_sequence=['#038b8d', '#8d0825', 'white']
        )
        bank_education.update_layout(
            title_x=0.5,
            title_font_family='kollektif',
            title_font_size=25,
            legend_font_family='kollektif',
            legend_font_size=20
        )

        # bank_account x job_type
        bank_job = px.histogram(
            by_age,
            y='job_type',
            color='bank_account',
            title='Relationship of bank account to the job of the respondent',
            orientation='h',
            template='plotly_dark',
            color_discrete_sequence=['#038b8d', '#8d0825', 'white']
        )
        bank_job.update_layout(
            title_x=0.5,
            title_font_family='kollektif',
            title_font_size=25,
            legend_font_family='kollektif',
            legend_font_size=20
        )

        # bank_account x age_of_respondent
        # bank_age = px.histogram(
        #     by_age['bank_account'],
        #     color='age_of_respondent',
        #     orientation='h',
        #     template='plotly_dark',
        #     color_discrete_sequence=['#038b8d', 'white', '#8d0825']
        # )
        return bank, bank_location, bank_cell, bank_gender, bank_relation, bank_marital, bank_education, bank_job
        # return bank,bank_job, bank_education, bank_relation, bank_marital, bank_location, bank_cell, bank_gender


if __name__ == '__main__':
    app.run_server(debug=True)
