# Imports for the project
import pandas as pd

# Loading the data
filename = 'carol_aviation_investigations_data.json'
df: pd.DataFrame = pd.read_json(filename)


# Restricting to USA crashes
df = df[df['Country'] == 'USA']

# Dropping unnecessary columns
df = df.drop(['MKey',
              'NTSBNumber',
              'HighestInjuryLevel',
              'CompletionStatus',
              'hasSafetyRecommendation',
              'IsStudy',
              'Mode',
              'OriginalPublishedDate',
              'ProbableCause',
              'AnalysisNarrative',
              'ConcatenatedFactualNarrative',
              'HazmatInvolved',
              'City',
              'StateOrRegion',
              'Country',
              'LeadAgency',
              'BoardMemberLaunch',
              'LaunchType',
              'ReportType',
              'TopicMode',
              'InvestigationClass',
              'Vehicles',
              'AirportID',
              'AirportName',
              'BoardMeetingDate',
              'ReportNumber',
              'DocketOpenDate',
              'ReportDate',
              'InjuryOnboardCount',
              'FatalInjuryCount',
              'SeriousInjuryCount',
              'MinorInjuryCount',
              'InjuryOngroundCount'], axis=1)

# Converting datatypes
df['EventType'] = df['EventType'].astype('category')
df['EventDateTimeUTC'] = pd.to_datetime(df['EventDateTimeUTC'])

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
