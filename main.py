# Imports for the project
import pandas as pd

# Loading the data
filename = 'carol_aviation_investigations_data.json'
df: pd.DataFrame = pd.read_json(filename)

# Dropping unnecessary columns
df = df.drop(['MKey',
              'NTSBNumber',
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
              'ReportDate'], axis=1)

# Converting datatypes
df = df.astype({
              'HighestInjuryLevel': 'category',
              'EventType': 'category',
              'InjuryOnboardCount': 'Int16',
              'FatalInjuryCount': 'Int16',
              'OnboardFatal': 'Int16',
              'SeriousInjuryCount': 'Int16',
              'MinorInjuryCount': 'Int16',
              'OnboardSerious': 'Int16',
              'OnboardMinor': 'Int16',
              'InjuryOngroundCount': 'Int16',
              'OnboardNone': 'Int16',
              'OngroundFatal': 'Int16',
              'OngroundSerious': 'Int16',
              'OngroundMinor': 'Int16'
               })

# Printout of data
print(df.info())
