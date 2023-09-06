# -*- coding: utf-8 -*-
"""Globalyoutubestats.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19qzT1yFPJ83Cp7smHZfPNUyvVEqVHk8R
"""

#Global YouTube Statistics.csv from kaggle:  https://www.kaggle.com/datasets/nelgiriyewithana/global-youtube-statistics-2023

import pandas as pd
import pandas
import math
import statistics as stats
import csv
import numpy as np
#libraries for visualization
import seaborn as sns
import matplotlib.pyplot as plt
import geopandas as gpd
import matplotlib
from mpl_toolkits.axes_grid1 import make_axes_locatable
from sklearn.preprocessing import MinMaxScaler
from scipy.stats.mstats import winsorize

#References:
# https://geopandas.org/en/stable/docs/user_guide/mapping.html#choropleth-maps
# https://waterprogramming.wordpress.com/2022/09/08/bivariate-choropleth-maps/
# https://dev.to/oscarleo/how-to-create-data-maps-of-the-united-states-with-matplotlib-p9i

#mount Drive
from google.colab import drive
drive.mount("/content/drive")

# Specify the file path to your CSV file
file_path = '/content/drive/MyDrive/Colab Notebooks/YT.csv'

# Load the CSV file into a DataFrame with the 'latin-1' encoding
yt_data = pd.read_csv(file_path, encoding='latin-1', usecols=['Youtuber', 'Country', 'highest_yearly_earnings', 'subscribers', 'Gross tertiary education enrollment (%)'])

# Display the first few rows of the DataFrame
yt_data

yt_data.describe()

yt_data.info()

# Set of colors matching the elements of Bi_Class
# We have to exclude those that did not come up in the data
colors = ['#e8e8e8', # 1A
          '#b0d5df', # 1B
          #'#64acbe', # 1C
          '#e4acac', # 2A
          '#ad9ea5', # 2B
          #'#627f8c', # 2C
          '#c85a5a', # 3A
          '#985356'] # 3B
          #'#574249'] # 3C

cmap = matplotlib.colors.ListedColormap(colors)
cmap

# Group by country and calculate total earnings
country_yr_earnings = yt_data.groupby('Country')['highest_yearly_earnings'].sum().reset_index()

# Load a world map shapefile from geopandas without using deprecated dataset module
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Merge the total earnings data with the world map data based on 'Country' column
merged_data = world.merge(country_yr_earnings, left_on='name', right_on='Country')

# Create a choropleth map based on total earnings with the new color palette
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
merged_data.plot(
    column='highest_yearly_earnings',
    cmap=cmap,
    linewidth=0.8,
    ax=ax,
    edgecolor='0.8',
    legend=True,
    legend_kwds={'label': "Total Earnings in Billions", 'orientation': "horizontal", 'shrink': 0.5}
)

# Add country labels
for x, y, label in zip(merged_data.centroid.x, merged_data.centroid.y, merged_data['name']):
    ax.annotate(label, xy=(x, y), xytext=(3, 3), textcoords="offset points", fontsize=7, color='black')

# Customize the plot appearance
ax.set_title('Total YouTubers\' Earnings by Country', fontsize=16)
ax.set_axis_off()

# Show the plot
plt.show()

# Group by country and calculate total earnings


country_earnings