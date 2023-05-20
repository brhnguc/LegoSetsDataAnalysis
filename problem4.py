import pandas as pd
import numpy as np
sets = pd.read_csv('Python\LegoSetsDataAnalysis\sets\sets.csv')
parts = pd.read_csv('Python\LegoSetsDataAnalysis\sets\parts.csv')
inventory_parts = pd.read_csv('Python\LegoSetsDataAnalysis\sets\inventory_parts.csv')
colors = pd.read_csv('Python\LegoSetsDataAnalysis\sets\colors.csv')
inventories = pd.read_csv('Python\LegoSetsDataAnalysis\sets\inventories.csv')
part_categories = pd.read_csv('Python\LegoSetsDataAnalysis\sets\part_categories.csv')

populer_renkler = inventory_parts.groupby('color_id')['quantity'].sum().nlargest(5)
populer_renkler = populer_renkler.reset_index().merge(colors, left_on='color_id',
right_on='id')[['name', 'quantity']]
print("Lego parçalarında en popüler olan 5 renk: \n",populer_renkler)