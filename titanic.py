import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plot

data = pd.read_csv("tested.csv")
print(data.head())
# print(data.info())
# print(data.describe())
# print(data.isnull().sum())

# Day 2: Visualization  of Missing Data
# define the figure size
plot.figure(figsize = (10, 8))
# plot the heatmap
sb.heatmap(data.isnull(), cbar = False,  cmap = "viridis")
# show the plot TITLE
plot.title("Missing Data in Titanic Dataset")
# show the plot
# plot.show()


#  remove the age colomn
data = data.drop(columns = ['Age'])

# replace the missing value in Fare with mean
data['Fare'] = data['Fare'].fillna(data['Fare'].mean())

# show only the first letter of the cabin
data['Cabin'] = data['Cabin'].str[0]
# relace the missing values with 'U' for unknown
data['Cabin'] = data['Cabin'].fillna('U')
# show the first 5 rows of the Cabin column
print(data.isnull().sum())

print(data.head())

data.to_csv("clean_Titanic_data.csv", index= False)
