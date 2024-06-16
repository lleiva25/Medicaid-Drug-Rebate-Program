# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
#import statsmodels.api as sm

# Incorporate data
df = pd.read_json('https://raw.githubusercontent.com/lleiva25/Medicaid-Drug-Rebate-Program/main/Jupyter%20Output/Product_Data_2023.json')
data_df = pd.read_json('https://raw.githubusercontent.com/lleiva25/Medicaid-Drug-Rebate-Program/main/Jupyter%20Output/Medicaid_2023_Dataset.json')

# List all drug names
drug_name = list(df.product_name)

# Create new dataframe for sum
sum_df = pd.DataFrame({
    "Reimbursement Type": ["Medicaid", "Non-Medicaid"],
    "Total Amount Reimbursed": [df["Medicaid Amount Reimbursed"].sum(), df["Non-medicaid Amount Reimbursed"].sum()]
})

#Top 10 Medications Reimbursed
top_10_df = df.sort_values(by="Total Amount Reimbursed", ascending=False).head(10)

#Create dataframe for utilization type
util_list = ["FFSU", "MCOU"]
util_counts = [data_df[data_df["utilization_type"] == util].shape[0] for util in util_list]

util_df = pd.DataFrame({
    "Utilization Type": util_list,
    "Number of Products": util_counts
})

# Initialize the app
app = Dash(__name__)
server = app.server

# Define the layout
app.layout = html.Div([
    html.H1('California Medicaid 2023 Dashboard'),
    
    # Pie Chart
    html.Div([
        html.H3('Reimbursements'),
        dcc.Graph(id="pie-chart", figure=px.pie(sum_df, 
                                                values="Total Amount Reimbursed", 
                                                names="Reimbursement Type", 
                                                hole=.3))
    ], style={'width': '50%', 'display': 'inline-block'}),
    
    # Pie Chart
    html.Div([
        html.H3('Utilization Type'),
        dcc.Graph(id="pie-chart1", figure=px.pie(util_df, 
                                                 values=util_counts, 
                                                 names=util_list, hole=.3))
    ], style={'width': '50%', 'display': 'inline-block'}),
    
    # Scatter Plot
    html.Div([
        html.H3('Number of Prescriptions vs Units Reimbursed'),
        dcc.Graph(id="scatter-plot", figure=px.scatter(df, 
                                                       x='Number of Prescriptions', 
                                                       y='Units Reimbursed', 
                                                       hover_data=['product_name'],
                                                       trendline="ols"))
    ]),

    # Bar Plot Top 10 Products that are Reimbursed
    html.Div([
        html.H3('Top 10 Reimbursed Products'),
        dcc.Graph(id="top-bar-plot", figure=px.bar(top_10_df,
                                               x="product_name",
                                               y="Total Amount Reimbursed",
                                               ))
    ]),


    # Box Plot
    html.Div([
        html.H3('Utilization Type & Number of Prescription'),
        dcc.Graph(id="box-plot", figure=px.box(data_df,
                                               x="utilization_type", 
                                               y='Number of Prescriptions'
                                               ))
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

# Callbacks for the bar charts
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

# # Import packages
# from dash import Dash, html, dash_table, dcc, callback, Output, Input
# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go
# import matplotlib as plt
# import gunicorn

# # Incorporate data
# df = pd.read_json('https://raw.githubusercontent.com/lleiva25/Medicaid-Drug-Rebate-Program/main/Jupyter%20Output/Product_Data_2023.json')
# data_df = pd.read_json('https://raw.githubusercontent.com/lleiva25/Medicaid-Drug-Rebate-Program/main/Jupyter%20Output/Medicaid_2023_Dataset.json')


# #List all drug names
# drug_name = list(df.product_name)

# #Create new dataframe for sum
# sum_df = pd.DataFrame({
#     "Reimbursement Type": ["Medicaid", "Non-Medicaid"],
#     "Total Amount Reimbursed": [df["Medicaid Amount Reimbursed"].sum(), df["Non-medicaid Amount Reimbursed"].sum()]
# })



# # Initialize the app
# app = Dash(__name__)

# server = app.server

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

# @app.callback(
#     Output("pie-chart1", "figure"),
#     Input("pie-chart1", "figure")
# )
# def generate_pie_chart1():
#     fig = px.pie(data_df, 
#                  values="utilization_type", 
#                  names="utilization_type", 
#                  hole=.3)
#     return fig

# # Callback to update the box plot
# @app.callback(
#     Output('scatter-plot', 'figure'),
#     [Input('scatter-plot', 'figure')]  # You can use dropdown or any other input component
# )

# def scatter_plot():
#     fig = px.scatter(df, 
#                      x='Number of Prescriptions', 
#                      y='Units Reimbursed', 
#                     # title='Number of Prescriptions vs Units Reimbursed', 
#                      #size=['Total Amount Reimbursed'],
#                      hover_data='product_name'
#                      ) 
#     return fig

# # Callback to update the box plot
# @app.callback(
#     Output('box-plot', 'figure'),
#     [Input('box-plot', 'figure')]  # You can use dropdown or any other input component
# )

# def box_plot():
#     fig = px.box(data_df,
#                  x = "utilization_type",
#                  y='Number of Prescriptions',
#                 # points="all"
#                  )
#     #fig.update_traces(quartilemethod="exclusive")
#     return fig


# # App layout
# app.layout = html.Div([
#     html.H1('California Medicaid 2023 Dashboard'),
#     #Pie Chart
#     html.Div([
#         html.H3('Reimbursements'),
#         dcc.Graph(id="pie-chart",figure=generate_pie_chart())
#     ], style={'width': '50%', 'display': 'inline-block'}),
#     #Pie Chart
#     html.Div([
#         html.H3('Utilization Type'),
#         dcc.Graph(id="pie-chart1",figure=generate_pie_chart1())
#     ], style={'width': '50%', 'display': 'inline-block'}),

#     #Scatter
#     html.Div([
#         html.H3('Number of Prescriptions vs Units Reimbursed'),
#         dcc.Graph(id="scatter-plot",figure=scatter_plot())
#     ]),
#     #Box plot
#         html.Div([
#         html.H3('Total Reimbursed vs Utilization'),
#         dcc.Graph(id="box-plot",figure=box_plot())
#     ]),

#     # Add Text
#     html.H3('Reimbursement Drug Comparison'),
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

# # @app.callback(
# #     Output("pie-chart", "figure"),
# #     Input("pie-chart", "figure")
# # )
# # def generate_pie_chart():
# #     fig = px.pie(sum_df, 
# #                  values="Total Amount Reimbursed", 
# #                  names="Reimbursement Type", 
# #                  hole=.3)
# #     return fig

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
