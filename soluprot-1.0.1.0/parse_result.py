
import pandas as pd

df = pd.read_csv('./soluprot.csv', header=0, sep=',')
df = df[['fa_id','soluble']]
df.columns = ['Name','soluprot']
df.to_csv('soluprot.csv', header=True, sep='\t', index=False)
