import pandas as pd
import numpy as np
sets = pd.read_csv('Python\LegoSetsDataAnalysis\sets\sets.csv')

# 1. Average number of Lego sets released per year
avr_sets = sets.groupby('year')['set_num'].count().mean()
print("Average number of Lego sets released per year:", avr_sets)