import backend.dataConfig as dataConfig
import pandas as pd

# Load data
datastream=pd.read_excel(dataConfig.file_path)

# Setzt die Spaltennamen
datastream.columns=['Portalnummer','Portalname','Link']

# Portalname wird entsprechend der Portalnummer gesetzt
namePortal1=datastream.loc[datastream['Portalnummer']==1, 'Portalname'].iloc[0]
namePortal1=datastream.loc[datastream['Portalnummer']==2, 'Portalname'].iloc[0]

# Portallink wird entsprechend der Portalnummer gesetzt
linkPortal1=datastream.loc[datastream['Portalnummer']==1, 'Link'].iloc[0]
linkPortal2=datastream.loc[datastream['Portalnummer']==2, 'Link'].iloc[0]


# Ideen zur Abstraktion
# Erstellt Key-Value-Paare für die Portale anstelle von LinkPortal1 und LinkPortal2