# ProtSoluCollection
a collection for protein solubility prediction in E. coli 

## 1. NetSolP (webserver: https://services.healthtech.dtu.dk/services/NetSolP-1.0/)
not submit more than 500 sequences in fasta format \
for example \
task 5: 66BDC87E0008754649767262 \
mutate: 66BEB769000AB16FDB25D42B \
then python parse_result.py
```
# parse_result.py
import os
import pandas as pd
parent_dir = os.path.abspath(os.path.dirname(__file__))

df = pd.read_csv(parent_dir+'/NetSolP.csv', header=0, sep=',')
df = df[['sid','predicted_solubility']]
df.columns = ['Name','NetSolP']
df.to_csv(parent_dir+'/NetSolP.csv', header=True, sep='\t', index=False)
```

## 2. GATSol (respotory: https://github.com/binbinbinv/GATSol)
### 2.1 environmen: must according to 
```
conda create -n GATSol python=3.9
conda activate GATSol
pip install torch==2.2.2 torchvision torchaudio
pip install pandas bio seaborn matplotlib_inline
pip install scikit-learn transformers Ipython
pip install iFeatureOmegaCLI rdkit
pip install torch_geometric==2.3.0 fair-esm
```
### 2.2 download checkpoints according to GATSol-main/check_point/best_model/readme.md

### 2.3 predict structure
put structure pdbs to Predict/NEED_to_PREPARE/pdb \
we use alphafold2 to implement it

### 2.4 predict solution
parepare sequences fasta as input.fasta
```
conda activate GATSol
python generate_input.py
cd Predict
bash ./tools/Predict.sh
python parse_result.py
```

## 3. Protein_Sol (https://protein-sol.manchester.ac.uk/software)

```
bash multiple_prediction_wrapper_export.sh input.fasta
python parse_result.py

```

## 4. soluprot (https://loschmidt.chemi.muni.cz/soluprot/?f=soluprot.zip)
### 4.1 environment
```
conda create -n python37 python=3.7
conda activate python37
pip install scikit-learn=0.20.1
pip install biopython=1.74
pip install pandas
pip install tqdm
```
### 4.2 dependencies

1. USEARCH: https://www.drive5.com/usearch/
2. TMHMM: http://www.cbs.dtu.dk/cgi-bin/nph-sw_request?tmhmm or https://git.loschmidt.cz/misc/tmhmm 

then change the path in soluprot.py to your USEARCH and TMHMM path

```
_USEARCH = '/home/hy/Documents/protein/solu/soluprot/soluprot-1.0.1.0/usearch11.0.667_i86linux32'
_TMHMM = '/home/hy/Documents/protein/solu/soluprot/soluprot-1.0.1.0/tmhmm-2.0c.Linux/tmhmm-2.0c/bin/tmhmm'

```
### 4.3 run
```
conda activate python37
python soluprot.py --i_fa input.fasta --o_csv soluprot.csv --tmp_dir tmp
python parse_result.py
```


