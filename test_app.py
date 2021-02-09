# Import modules
import streamlit as st
import pandas as pd
import numpy as np

# Set parameters
csv_path = "processed.csv.gz"
n_cols = 4
n_results = 100

allergens = sorted(
[
    "",
    "gluten",
    "milk",
    "soy"
]
)

# Load data
@st.cache
def load_data():
    df = pd.read_csv(csv_path)
    df["allergens"].replace(np.nan, "", regex=True, inplace=True)
    df["carbon-footprint_100g"].replace(np.nan, -1, regex=True, inplace=True)
    return df

df = load_data()
#display = df.head(10)
#print("First 10 rows of the DataFrame:")
#print(display)

st.sidebar.title("Carbon footprint food check")

cal = st.sidebar.slider("Carbon footprint per 100g", 0, 700, (100, 300), 10)
df = df[(df["carbon-footprint_100g"] > cal[0]) & (df["carbon-footprint_100g"] < cal[1])]

aller = st.sidebar.selectbox("Allergens", allergens)
df = df[df["allergens"].str.lower().str.contains(aller)]

f = st.file_uploader("Select Image")

cols = st.beta_columns(n_cols)
df = df[:n_results].reset_index()

for i, row in df.iterrows():
    cols[i % n_cols].image(row["image_small_url"], use_column_width=True)

#selected = st.sidebar.selectbox("Select category", ["Dog", "Cat"])

#st.select_slider("Range", [1, 5])

#print(selected)