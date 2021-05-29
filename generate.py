import pandas as pd
#df=pd.read_csv('https://raw.githubusercontent.com/adactio/TheSession-data/main/csv/tunes.csv')
df=pd.read_csv('tunes.csv')
with open('input/tunes.txt','w') as f:
  for i in df.index:
    f.write(df['abc'][i]+'\n\n')

