# Global Choropleth Map of COVID 19 Infections & Casualties

# Importing libraries
import pandas as pd, numpy as np
import matplotlib.pyplot as plt, seaborn as sb

# Importing dataset
ds = pd.read_csv('WHO-COVID-19-global-data.csv')

# Dropping columns
ds = ds.drop(columns = ['WHO_region', 'New_cases', 'New_deaths'])

# Creating a new DataFrame with only the latest case counts of each country
cases_df = ds.groupby('Country').max().reset_index()

cases = cases_df.drop(columns = ['Country_code', 'Cumulative_deaths'])
deaths = cases_df.drop(columns = ['Country_code', 'Cumulative_cases'])


# =============================  Choropleth Map  =============================
from plotly.offline import plot
import plotly.graph_objects as go

# 1) Infection Rates
fig_cases = go.Figure(data = go.Choropleth(locations = cases['Country'],
                                     z = cases['Cumulative_cases'].astype(int),
                                     locationmode = 'country names',
                                     colorscale = 'matter',
                                     colorbar_title = "Infections"))

fig_cases.update_layout(title_text = 'COVID 19: Global Infections Count',
                  geo = dict(showframe = False,
                           showcoastlines = False,
                           projection_type = 'equirectangular'),

                annotations = [dict(x = 0.5,
                                    y = 0.1,
                                    text='Source: <a href="https://covid19.who.int/info">\
                                    WHO</a>',
                                    showarrow = False)])
plot(fig_cases)


# 2) Death Counts
fig_deaths = go.Figure(data = go.Choropleth(locations = deaths['Country'],
                                            z = deaths['Cumulative_deaths'].astype(int),
                                            locationmode = 'country names',
                                            colorscale = 'ylgnbu',
                                            colorbar_title = "Deaths"))

fig_deaths.update_layout(title_text = 'COVID 19: Global Death Count',
                         geo = dict(showframe = False,
                                    showcoastlines = False,
                                    projection_type = 'equirectangular'),
                         annotations = [dict(x = 0.5,
                                             y = 0.1,
                                             text='Source: <a href="https://covid19.who.int/info">\
                                             WHO</a>',
                                             showarrow = False)])
plot(fig_deaths)
