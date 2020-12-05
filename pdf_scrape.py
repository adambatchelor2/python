import camelot
import pandas as pd

# read in pdf

tables = camelot.read_pdf("jun19.pdf",  flavor='stream', pages='4') #pages can be comma separated
# Loop through each table (table per page)
test_df = pd.DataFrame() # empty df
for table in tables:
    test_df = test_df.append(table.df) # add to dataframe
# remove headers that are not needed.

print(test_df)

# test_df = test_df[test_df[1] != "CITY"]
# test_df = test_df[test_df[1] != ""]
# # add colun names
# test_df.columns=['Rank','City','IATA','PAX_May_2020','PAX_Vs_19','PAX_Vs_18','Commercial_May_2020', 'Commercial_Vs_19','Freight_May_2020', 'Freight_Vs_19']
# # prin Heathrows May Stats
# print(test_df[test_df['IATA'] == 'LHR'])