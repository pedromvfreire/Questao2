# Definiria como sendo a distancia entre as conexoes de cobradores e cobrados

import pandas as pd
from scipy.spatial.distance import pdist, squareform

dist = pd.read_csv('cobrancas_ia.csv', sep=';')

print(dist.dtypes)

dist = dist.groupby(['cobrador_id', 'cobrado_id']).size().unstack().fillna(0)

pairwise = pd.DataFrame(
    squareform(pdist(dist)),
    columns = dist.index,
    index = dist.index)

pairwise

table_dist = pairwise.unstack()

table_dist.index.rename(['Cliente A', 'Cliente B'], inplace=True)
table_dist = table_dist.to_frame('cosine distance').reset_index()

table_dist = table_dist[(table_dist['Cliente A'] != table_dist['Cliente B'])]

print(table_dist)