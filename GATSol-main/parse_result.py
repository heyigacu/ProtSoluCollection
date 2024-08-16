import pandas as pd



df = pd.read_csv('Predict/Output.csv')
df = df[['id','Solubility_hat']]
df.columns = ['Name','GATSol']
df.to_csv('GATSol.csv',index=False,header=True,sep='\t')