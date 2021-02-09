#%%
# Import modules
#import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import data
csv_path = "processed.csv.gz"

# Load data
#@st.cache
def load_data():
    df = pd.read_csv(csv_path)
    df.replace(np.nan, "", regex=True, inplace=True)
    #df["allergens"].replace(np.nan, "", regex=True, inplace=True)
    #df["carbon-footprint_100g"].replace(np.nan, "", regex=True, inplace=True)
    return df

df = load_data()

# Display column names of dataframe
for col in df.columns: 
    print(col)

# Display unique values for rows in dataframe
# for col in df:
#     print(df['nutrition-score-fr_100g'].unique())

for col in df:
    print(df['nova_group'].unique())

num_carbon = len(df[(df['carbon-footprint_100g']!= "")])
print(num_carbon)

num_nova = len(df[(df['nova_group']!= "")])
print(num_nova)

# Plot data
df['nutrition-score-fr_100g'].value_counts()[1:30].plot(kind='bar')
plt.title('Nutrition score distribution')
plt.xlabel('values')
plt.ylabel('# of products')
#plt.xticks(np.arange(0, 20, step=1))
plt.show()

df['carbon-footprint_100g'].value_counts()[2:30].plot(kind='bar')
plt.title('Carbon footprint distribution')
plt.xlabel('values')
plt.ylabel('# of products')
plt.show()

df['nova_group'].value_counts()[2:30].plot(kind='bar')
plt.title('Nova group distribution')
plt.xlabel('NOVA group')
plt.ylabel('# of products')
#plt.xticks(np.arange(0, 700, step=50))
plt.show()
# %%
