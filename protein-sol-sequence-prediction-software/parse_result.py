import pandas as pd

ls = []
lines = open('seq_prediction.txt','r').readlines()
for line in lines:
    if line.startswith('SEQUENCE PREDICTIONS,>'):
        line = line.split('>')[-1].strip()
        words = line.split(',')
        words = [word.strip() for word in words]
        ls.append(words)
df = pd.DataFrame(ls)
df.columns = ['Name', 'Protein_Sol percent-sol','Protein_Sol scaled-sol','Protein_Sol population-sol','Protein_Sol pI']
df.to_csv('Protein_Sol.csv', header=True, sep='\t', index=False)



