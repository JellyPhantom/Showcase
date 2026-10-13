import pandas as pd

filename = 'carol_aviation_investigations_data.json'
df: pd.DataFrame = pd.read_json(filename)
print(df.head())
