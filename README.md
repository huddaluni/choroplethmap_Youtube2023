# Tutorial: Choroplethmap_Youtuber earnings, by country (2023)

![image](https://github.com/huddaluni/choroplethmap_Youtube2023/assets/117635800/bc18d8a4-e192-415b-9624-de1067c9dee6)





# I have used Global YouTube Statistics.csv from kaggle:   
get here: https://www.kaggle.com/datasets/nelgiriyewithana/global-youtube-statistics-2023 
# For additional study on choropleth maps here are a few useful refrences  
References:  
 https://geopandas.org/en/stable/docs/user_guide/mapping.html#choropleth-maps  
https://waterprogramming.wordpress.com/2022/09/08/bivariate-choropleth-maps/  
 https://dev.to/oscarleo/how-to-create-data-maps-of-the-united-states-with-matplotlib-p9i   



 
-------------------------------------------------------------------------------  
The first line of codes    
-------------------------------------------------------------------------------    
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
*******************************************************************************
Here's a breakdown of what the code is doing:

Importing necessary libraries:

pandas: Used for data manipulation and analysis.
math: Provides mathematical functions and operations.
statistics as stats: Used for statistical calculations.
csv: Provides tools for reading and writing CSV files.
numpy as np: Used for numerical operations.
seaborn and matplotlib.pyplot: Libraries for data visualization.
geopandas: Used for geospatial data and maps.
matplotlib: Matplotlib is a library for creating static, animated, and interactive visualizations in Python.
mpl_toolkits.axes_grid1: Used for creating axes with shared grids.





-------------------------------------------------------------------------------   
Second line of code   
-------------------------------------------------------------------------------   
#mount Drive  
from google.colab import drive  
drive.mount("/content/drive")  
#Specify the file path to your CSV file   
file_path = '/content/drive/MyDrive/Colab Notebooks/YT.csv'    

#Load the CSV file into a DataFrame with the 'latin-1' encoding    
yt_data = pd.read_csv(file_path, encoding='latin-1', usecols=['Youtuber', 'Country', 'highest_monthly_earnings', 'subscribers', 'Gross tertiary education enrollment (%)'])   

#Display the first few rows of the DataFrame    
yt_data     
*******************************************************************************
*In this code i am mounting my drive in google colab and changing filepath to where my file is, you can change it your file path, note i am also using specific colums from the data







-------------------------------------------------------------------------------
Third line of code
-------------------------------------------------------------------------------
#Set of colors matching the elements of Bi_Class  
colors = ['#e8e8e8', # 1A    
          '#b0d5df', # 1B   
          '#e4acac', # 2A  
          '#ad9ea5', # 2B  
          '#c85a5a', # 3A  
          '#985356'] # 3B  
            
cmap = matplotlib.colors.ListedColormap(colors)  
cmap  
*******************************************************************************
this code defines a set of colors and creates a color map (cmap) using those colors. These colors can be used later in data visualizations, such as maps or charts, to represent different categories or data points with distinct colors.
colors = ['#e8e8e8', '#b0d5df', '#e4acac', '#ad9ea5', '#c85a5a', '#985356']: This is where the actual work is happening. Here, a list of colors is defined. Each color is represented by a code starting with a '#' symbol. For example, #e8e8e8 is a light gray color, and #b0d5df is a light blue color.Note i found these colours from one the refrences i have provided at the top.

cmap = matplotlib.colors.ListedColormap(colors): This line creates what's called a "color map" or cmap. It's like a palette of colors that can be used to color different parts of a map or a chart. The colors list we defined earlier is used to create this color map.
cmap: Finally, when you type cmap and run the code, it will display or show you the color map that you've just created. It's a way to see what the colors in your palette look like.








-------------------------------------------------------------------------------  
Final line of code  
-------------------------------------------------------------------------------  
#Group by country and calculate total earnings
country_earnings = yt_data.groupby('Country')['highest_monthly_earnings'].sum().reset_index()

#Load a world map shapefile from geopandas without using deprecated dataset module
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

#Merge the total earnings data with the world map data based on 'Country' column
merged_data = world.merge(country_earnings, left_on='name', right_on='Country')

#Create a choropleth map based on total earnings with the new color palette
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
merged_data.plot(
    column='highest_monthly_earnings',
    cmap=cmap,
    linewidth=0.8,
    ax=ax,
    edgecolor='0.8',
    legend=True,
    legend_kwds={'label': "Total Earnings", 'orientation': "horizontal", 'shrink': 0.5}
)

#Add country labels
for x, y, label in zip(merged_data.centroid.x, merged_data.centroid.y, merged_data['name']):
    ax.annotate(label, xy=(x, y), xytext=(3, 3), textcoords="offset points", fontsize=7, color='black')

#Customize the plot appearance
ax.set_title('Total YouTubers\' Earnings by Country', fontsize=16)
ax.set_axis_off()

#Show the plot
plt.show()

*******************************************************************************
In this code: 
#Group by country and calculate total earnings: This comment tells us that we're going to group data by countries and calculate the total earnings for each country.

country_earnings = yt_data.groupby('Country')['highest_monthly_earnings'].sum().reset_index(): This line of code does the following:

It takes our YouTube data (yt_data) and groups it by the 'Country' column.
Within each group, it adds up the 'highest_monthly_earnings' for all YouTubers from that country.
The result is a new table (country_earnings) that shows the total earnings for each country.
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres')): Here, we're loading a world map. Think of it like loading a map of the entire world, but it's in a digital format.

merged_data = world.merge(country_earnings, left_on='name', right_on='Country'): Now, we're combining our world map (world) with the total earnings data (country_earnings) based on a common column, which is 'Country.' This step connects the map with the earnings data for each country.

fig, ax = plt.subplots(1, 1, figsize=(15, 10)): We're preparing a canvas or space for our map. Think of it as getting a blank sheet of paper to draw on, and it's going to be 15 units wide and 10 units tall.

merged_data.plot(...): This is where we're actually drawing the map and specifying how it should look:

column='highest_monthly_earnings': We're coloring each country based on its total earnings.
cmap=cmap: We're using a special set of colors (defined earlier) to color the countries.
linewidth=0.8: This controls the thickness of the lines that outline the countries on the map.
ax=ax: It tells the code to draw the map on the canvas we created earlier.
edgecolor='0.8': This sets the color of the lines outlining the countries.
legend=True: We're adding a legend (like a key) to explain the colors on the map.
legend_kwds={'label': "Total Earnings", 'orientation': "horizontal", 'shrink': 0.5}: These settings customize how the legend appears on the map.
for x, y, label in zip(merged_data.centroid.x, merged_data.centroid.y, merged_data['name']):: Here, we're adding labels to the countries on the map. It's like writing the names of the countries next to them.

xy=(x, y): This is where we place the label on the map.
xytext=(3, 3): We're adjusting the position of the label slightly.
fontsize=7: This controls the size of the font used for the country names.
color='black': The color of the text is set to black.
ax.set_title(...): We're giving our map a title, which will appear at the top.

ax.set_axis_off(): This line hides the axes (the lines showing measurements) on the map, making it look cleaner.

plt.show(): Finally, this command displays the map we've created, showing the total earnings of YouTubers by country in a visually appealing way.

In simple terms, this code takes data about how much money YouTubers from different countries make, and it shows this information on a colorful map, with each country colored based on earnings. It also labels the countries and makes the map look nice.






















sklearn.preprocessing.MinMaxScaler: Provides a way to scale numerical data to a specific range.
scipy.stats.mstats.winsorize: Used for winsorizing data (replacing extreme values with less extreme values).
