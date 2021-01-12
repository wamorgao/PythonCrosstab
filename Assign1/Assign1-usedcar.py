import pandas as pd

headers = ["Year", "Model", "Price", "Mileage", "Color", "Transmission"]

# Read in the CSV file and convert "?" to NaN
df_raw = pd.read_csv("usedcar.csv", header=None, names=headers, na_values="?")

# df_raw.head(5)
# Define a list of models that we want to review
Type = ["Red", "Blue", "Yellow", "White", "Gold", "Black", "Green", "Silver"]

# Create a copy of the data with only the top 8 manufacturers
df = df_raw[df_raw.Color.isin(Type)].copy()

f = pd.crosstab(df.Color, df.Transmission, margins=True, margins_name="Total")

f.to_csv("PythonCrosstab[usedcar].csv", index_label = "Color")