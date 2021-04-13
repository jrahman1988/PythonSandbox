'''
Stripping unwanted character attached to the end of string value of a column
'''
import pandas as pd

# Pandas dataframe
lst = [['Greece[e]', 100], ['China[e]', 200], ['Singapore', 300], ['Australia[17]', 400], ['Zambia', 500], ['France', 600], ['Canada[7]', 700]]
df = pd.DataFrame(lst, columns=['Country','Ranking'])
print (df)

# Remove any '[e]' chars attached to a country name
df["Country"] = df["Country"].str.replace(r"\[.*\]$", "", regex=True)
print(df)