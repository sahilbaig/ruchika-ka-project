import pandas as pd

df = pd.read_csv (r"C:\Users\sahil\Downloads\sample.csv")
# selecting dataframe with selcted columns
# df = pd.DataFrame(df, columns= [
#     'gr_id',
# 'sap_id',
# 'sfdc_id',
# 'sales_organization',
# 'name',
# 'house_number',
# 'postcode',
# 'street',
# 'city',
# 'sfdc_tenure',
# 'sfdc_tier',
# 'simulation_subtype',
# 'cluster',
# 'quadrant',
# 'sfdc_rtm',
# 'segment',
# 'sub_segment',
# 'poc_image',
# 'oneyp_volume',
# 'volume_potential_3',
# 'strategic_relevance',
# 'salesforce_status',
# 'volume_survey_total_abi',
# 'account_type',
# 'salesforce_channel',
# 'sub_channel',
# 'visit_frequency',
# ])



# Select row by sap_id
# df_new = df[df['sap_id'] == '29801712']
# print (df_new)






# Completeness
columnNames=(list(df.columns))

gr_id_val=df['gr_id'].notnull().sum()
for i in columnNames:
    print(df[i].notnull().sum(),"/",gr_id_val)

