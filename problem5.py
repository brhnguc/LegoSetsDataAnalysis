import pandas as pd
import numpy as np
sets = pd.read_csv('Python\LegoSetsDataAnalysis\sets\sets.csv')
parts = pd.read_csv('Python\LegoSetsDataAnalysis\sets\parts.csv')
inventory_parts = pd.read_csv('Python\LegoSetsDataAnalysis\sets\inventory_parts.csv')
colors = pd.read_csv('Python\LegoSetsDataAnalysis\sets\colors.csv')
inventories = pd.read_csv('Python\LegoSetsDataAnalysis\sets\inventories.csv')
part_categories = pd.read_csv('Python\LegoSetsDataAnalysis\sets\part_categories.csv')


bricks_categories = part_categories[part_categories['name'].str.contains('bricks', case=False)]

# Bricks kategorilerinin id'lerini al
bricks_category_ids = bricks_categories['id'].tolist()

# Bricks kategorilerine ait olan parçaları filtrele
brick_parts = parts[parts['part_cat_id'].isin(bricks_category_ids)]

# Bricks parçalarının inventory'sini al
brick_inventory = inventory_parts[inventory_parts['part_num'].isin(brick_parts['part_num'])]

# Bricks parçalarının nadir renklerini bul
rare_colors = brick_inventory.groupby('color_id')['quantity'].sum().nsmallest(5).index.tolist()

# Nadir renklerdeki bricks parçalarını bul
rare_bricks = brick_inventory[brick_inventory['color_id'].isin(rare_colors)]

# Parça numarasına göre nadir bricks parçalarını grupla ve nadirliğe göre sırala
rare_bricks_by_part = rare_bricks.groupby('part_num')['quantity'].sum().reset_index()
rare_bricks_by_part.sort_values('quantity', inplace=True)

# En nadir 5 bricks parçasını al
rarest_bricks = rare_bricks_by_part.head(5)

# En nadir 5 bricks parçasının isimlerini ve miktarlarını yazdır
for index, row in rarest_bricks.iterrows():
    part_num = row['part_num']
    quantity = row['quantity']
    part_name = parts[parts['part_num'] == part_num]['name'].values[0]
    print(f"{part_name}: {quantity}")

