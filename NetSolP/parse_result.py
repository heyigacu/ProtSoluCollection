import os
import pandas as pd
parent_dir = os.path.abspath(os.path.dirname(__file__))

df = pd.read_csv(parent_dir+'/NetSolP.csv', header=0, sep=',')
df = df[['sid','predicted_solubility']]
df.columns = ['Name','NetSolP']
df.to_csv(parent_dir+'/NetSolP.csv', header=True, sep='\t', index=False)
