# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import json
import plotly.express as px
import plotly.graph_objects as go
import matplotlib as plt

# Incorporate data
df = pd.read_json('/Users/leslieleiva/Documents/GitHub/Medicaid-Drug-Rebate-Program/Jupyter Output/Product_Data_2023.json')
data_df = pd.read_json('/Users/leslieleiva/Documents/GitHub/Medicaid-Drug-Rebate-Program/Jupyter Output/Medicaid_2023_Dataset.json')


#List all drug names
drug_name = list(df.product_name)

#Create new dataframe for sum
sum_df = pd.DataFrame({
    "Reimbursement Type": ["Medicaid", "Non-Medicaid"],
    "Total Amount Reimbursed": [df["Medicaid Amount Reimbursed"].sum(), df["Non-medicaid Amount Reimbursed"].sum()]
})



# Initialize the app
app = Dash(__name__)

@app.callback(
    Output("pie-chart", "figure"),
    Input("pie-chart", "figure")
)
def generate_pie_chart():
    fig = px.pie(sum_df, 
                 values="Total Amount Reimbursed", 
                 names="Reimbursement Type", 
                 hole=.3)
    return fig

# Callback to update the box plot
@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('scatter-plot', 'figure')]  # You can use dropdown or any other input component
)

def scatter_plot():
    fig = px.scatter(df, 
                     x='Number of Prescriptions', 
                     y='Units Reimbursed', 
                    # title='Number of Prescriptions vs Units Reimbursed', 
                     #size=['Total Amount Reimbursed'],
                     hover_data='product_name'
                     ) 
    return fig

# Callback to update the box plot
@app.callback(
    Output('box-plot', 'figure'),
    [Input('box-plot', 'figure')]  # You can use dropdown or any other input component
)

def box_plot():
    fig = px.box(data_df,
                 x = 'product_name',
                 y='Total Amount Reimbursed')
    #fig.update_traces(quartilemethod="exclusive")
    return fig


# App layout
app.layout = html.Div([
    html.H1('California Medicaid 2023 Dashboard'),
    #Pie Chart
    html.Div([
        html.H3('Reimbursements'),
        dcc.Graph(id="pie-chart",figure=generate_pie_chart())
    ]),
    #Scatter
    html.Div([
        html.H3('Number of Prescriptions vs Units Reimbursed'),
        dcc.Graph(id="scatter-plot",figure=scatter_plot())
    ]),
    #Box plot
        html.Div([
        html.H3('Number of Prescriptions'),
        dcc.Graph(id="box-plot",figure=box_plot())
    ]),

    # Add Text
    html.H3('Reimbursement Drug Comparison'),
    html.Div([
        dcc.Dropdown(
            id="dropdown1",
            options=[{"label": name, "value": name} for name in drug_name],
            value=drug_name[0]
        ),
        dcc.Graph(id="graph1"),
    ], style={'width': '50%', 'display': 'inline-block'}),

    html.Div([
        dcc.Dropdown(
            id="dropdown2",
            options=[{"label": name, "value": name} for name in drug_name],
            value=drug_name[1]
        ),
        dcc.Graph(id="graph2"),
    ], style={'width': '50%', 'display': 'inline-block'}),
])

# @app.callback(
#     Output("pie-chart", "figure"),
#     Input("pie-chart", "figure")
# )
# def generate_pie_chart():
#     fig = px.pie(sum_df, 
#                  values="Total Amount Reimbursed", 
#                  names="Reimbursement Type", 
#                  hole=.3)
#     return fig

@app.callback(
    Output("graph1", "figure"), 
    Input("dropdown1", "value")
)
def update_bar_chart1(product):
    mask = df.product_name == product
    filtered_df = df[mask]

    fig = go.Figure(data=[
        go.Bar(
            name='Medicaid',
            x=filtered_df["product_name"],
            y=filtered_df["Medicaid Amount Reimbursed"]
        ),
        go.Bar(
            name='Non-Medicaid',
            x=filtered_df['product_name'],
            y=filtered_df["Non-medicaid Amount Reimbursed"]
        )
    ])
    return fig

@app.callback(
    Output("graph2", "figure"), 
    Input("dropdown2", "value")
)
def update_bar_chart2(product):
    mask = df.product_name == product
    filtered_df = df[mask]

    fig = go.Figure(data=[
        go.Bar(
            name='Medicaid',
            x=filtered_df["product_name"],
            y=filtered_df["Medicaid Amount Reimbursed"]
        ),
        go.Bar(
            name='Non-Medicaid',
            x=filtered_df['product_name'],
            y=filtered_df["Non-medicaid Amount Reimbursed"]
        )
    ])
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)

###########################################################

# # App layout
# app.layout = html.Div([
#     html.Div([
#     html.H4('Reimbursement Type'),
#     dcc.Graph(id="graph")]),

#     #Add Text
#     html.H2('Reimbursement Drug Comparison'),
#     html.Div([
#         dcc.Dropdown(
#             id="dropdown1",
#             options=[{"label": name, "value": name} for name in drug_name],
#             value=drug_name[0]
#         ),
#         dcc.Graph(id="graph1"),
#     ], style={'width': '50%', 'display': 'inline-block'}),
    
#     html.Div([
#         dcc.Dropdown(
#             id="dropdown2",
#             options=[{"label": name, "value": name} for name in drug_name],
#             value=drug_name[1]
#         ),
#         dcc.Graph(id="graph2"),
#     ], style={'width': '50%', 'display': 'inline-block'}),
# ])

# @app.callback(
#     Output("graph", "figure"), 
#     #Input("dropdown", "value")
# )
# ####
# def generate_chart(names, values):
#     fig = px.pie(sum_df, 
#                  values="Total Amount Reimbursed", 
#                  names="Reimbursement Type", 
#                  hole=.3)
#     return fig


# @app.callback(
#     Output("graph1", "figure"), 
#     Input("dropdown1", "value")
# )
# def update_bar_chart1(product):
#     mask = df.product_name == product
#     filtered_df = df[mask]

#     fig = go.Figure(data=[
#         go.Bar(
#             name='Medicaid',
#             x=filtered_df["product_name"],
#             y=filtered_df["Medicaid Amount Reimbursed"]
#         ),
#         go.Bar(
#             name='Non-Medicaid',
#             x=filtered_df['product_name'],
#             y=filtered_df["Non-medicaid Amount Reimbursed"]
#         )
#     ])
#     return fig

# @app.callback(
#     Output("graph2", "figure"), 
#     Input("dropdown2", "value")
# )
# def update_bar_chart2(product):
#     mask = df.product_name == product
#     filtered_df = df[mask]

#     fig = go.Figure(data=[
#         go.Bar(
#             name='Medicaid',
#             x=filtered_df["product_name"],
#             y=filtered_df["Medicaid Amount Reimbursed"]
#         ),
#         go.Bar(
#             name='Non-Medicaid',
#             x=filtered_df['product_name'],
#             y=filtered_df["Non-medicaid Amount Reimbursed"]
#         )
#     ])
#     return fig


# if __name__ == '__main__':
#     app.run_server(debug=True)

#####################################################
# # Initialize the app
# app = Dash()


# # App layout
# app.layout = html.Div(children=[
#     #Add Text
#     html.H2('Drug Reimbursement Types'),
#     #Create Drop Down
#     dcc.Dropdown(
#         id="dropdown",
#         options=drug_name,
#         value=drug_name[0],
#         clearable=False,
#     ),
#     #View Graph
#     dcc.Graph(id="graph")]),

#     # #New Div for all elements in the
#     # html.Div(children=[
#     #     #Add Text
#     #     html.H2('Drug Reimbursement Types'),
#     #     #Create Drop Down
#     #     dcc.Dropdown(
#     #         id="dropdown",
#     #         options=drug_name,
#     #         value=drug_name[0],
#     #         clearable=False,
#     #     ),
#     #     #View Graph
#     #     dcc.Graph(id="graph")])


# @app.callback(
#     Output("graph", "figure"), 
#     Input("dropdown", "value"))


# #Creating a stacked bar chart
# def update_bar_chart(product):
#     mask = df.product_name == product
#     filtered_df = df[mask]

#     fig = go.Figure(data=[
#         go.Bar(
#             name='Medicaid',
#             x=filtered_df["product_name"],
#             y=filtered_df["Medicaid Amount Reimbursed"]
#         ),
#         go.Bar(
#             name='Non-Medicaid',
#             x=filtered_df['product_name'],
#             y=filtered_df["Non-medicaid Amount Reimbursed"]
#         )
#     ])
#     return fig


# if __name__ == '__main__':
#     app.run_server(debug=True)
# app.run_server(debug=True)


    #df = px.data.tips() # replace with your own data source
    # fig = px.bar(df[mask], x="product_name", y="Total Amount Reimbursed", 
    #              #color="smoker",
    #              barmode="group")
    #View data table
    #[html.Div(children='Medicaid 2023 Product Analysis'),
    #dash_table.DataTable(data=df.to_dict('records'), page_size=100)]
# # Run the app
# if __name__ == '__main__':
#     app.run(debug=True)