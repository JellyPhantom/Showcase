# Imports for the project
import pandas as pd

# Loading the data
filename = 'carol_aviation_investigations_data.json'
df: pd.DataFrame = pd.read_json(filename)

# Dropping unnecessary columns
df = df[['Latitude',
         'Longitude',
         'EventType',
         'EventDateTimeUTC',
         'OnboardNone',
         'OnboardMinor',
         'OnboardSerious',
         'OnboardFatal',
         'OngroundMinor',
         'OngroundSerious',
         'OngroundFatal']]

# Converting datatypes
df['EventType'] = df['EventType'].astype('category')
df['EventDateTimeUTC'] = pd.to_datetime(df['EventDateTimeUTC'])\
                         .dt.tz_localize('UTC')

cols = ['OnboardFatal',
        'OnboardSerious',
        'OnboardMinor',
        'OnboardNone',
        'OngroundFatal',
        'OngroundSerious',
        'OngroundMinor']
for col in cols:
    df[col] = df[col].astype('Int16')
    df[col] = df[col].fillna(0)

# Printout of data
print(df.info())
print(df.head(20))
df.to_csv('output.csv')
