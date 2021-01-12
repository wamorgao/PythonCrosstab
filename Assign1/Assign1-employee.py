import pandas as pd

headers = ["ID", "Gender", "Birth Date", "Jobcat", "Job Time", "Prev Exp", "Minority"]

# Read in the CSV file and convert "?" to NaN
df_raw = pd.read_csv("employee.csv", header=None, names=headers, na_values="?")

# df_raw.head(5)
# Define a list of models that we want to review
Type = ["m", "f"]

# Create a copy of the data with only the top 8 manufacturers
df = df_raw[df_raw.Gender.isin(Type)].copy()

# df_raw.head(5)

f = pd.crosstab(df.Gender, df.Jobcat, margins=True, margins_name="Total")
f.to_csv("PythonCrosstab[employee].csv", index_label = "Gender")
