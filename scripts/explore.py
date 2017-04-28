import pandas as pd

dataDF = pd.read_csv('../data/en.openfoodfacts.org.products_10.tsv', sep='\t')
print(dataDF.columns)


