import pandas as pd

provincies = ['Oost-Vl', 'West-Vl', 'Antwerpen', 'Limburg',  'Vl-Brabant']

for prov in provincies:
    filename = prov
    read_file = pd.read_excel (r'prioriteitenlijst.xlsx', sheet_name=prov)
    read_file.to_csv (r'{}.csv'.format(prov), index=None, header=True)

