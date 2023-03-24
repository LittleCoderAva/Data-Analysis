import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/cwkteacher/Data/master/athletes.csv')

print(df[("gold")])
print(df[["name","bronze"]])
tennis = df.where(df["sport"]=="tennis").dropna().to_string()
print(tennis)