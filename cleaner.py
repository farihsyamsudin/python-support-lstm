import pandas as pd

df = pd.read_csv("datas/output.csv")

df_cleaned = df.dropna()

df_cleaned.to_csv('datas/output_clean.csv', index=False)
