import pandas as pd
import numpy as np
sets = pd.read_csv('Python\LegoSetsDataAnalysis\sets\sets.csv')
parts = pd.read_csv('Python\LegoSetsDataAnalysis\sets\parts.csv')
inventory_parts = pd.read_csv('Python\LegoSetsDataAnalysis\sets\inventory_parts.csv')
colors = pd.read_csv('Python\LegoSetsDataAnalysis\sets\colors.csv')
inventories = pd.read_csv('Python\LegoSetsDataAnalysis\sets\inventories.csv')
part_categories = pd.read_csv('Python\LegoSetsDataAnalysis\sets\part_categories.csv')

# What is the average number of Lego parts per year?

sets_inventories = sets.merge(inventories, left_on='set_num', right_on='set_num')
sets_inventory_parts = sets_inventories.merge(inventory_parts, left_on='id', right_on='inventory_id')
total_parts_per_year = sets_inventory_parts.groupby('year')['quantity'].sum()
ort_parca = total_parts_per_year.mean()
print("Yılda ortalama Lego parça sayısı:", ort_parca)