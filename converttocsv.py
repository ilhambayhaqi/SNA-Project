import pandas as pd

filename = 'before_koko_d1.json'

df = pd.read_json('Resource/' + filename, lines=True)
df.to_csv('Resource/csv/' + filename.split('.')[0] + '.csv',index=False, sep=';')