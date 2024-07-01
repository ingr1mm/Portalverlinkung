import backend.dataConfig as dataConfig
import pandas as pd

class Controller:
    def __init__(self):        
        self.datastream.columns=['Portalnummer','Portalname','Link']
        self.namePortal1=self.datastream.loc[self.datastream['Portalnummer']==1, 'Portalname'].iloc[0]
        self.namePortal2=self.datastream.loc[self.datastream['Portalnummer']==2, 'Portalname'].iloc[0]
        self.linkPortal1=self.datastream.loc[self.datastream['Portalnummer']==1, 'Link'].iloc[0]
        self.linkPortal2=self.datastream.loc[self.datastream['Portalnummer']==2, 'Link'].iloc[0]
       
    def getDatastream(self, file_path):
        self.datastream = pd.read_excel(file_path)
        return self.datastream



# Ideen zur Abstraktion
# Erstellt Key-Value-Paare für die Portale anstelle von LinkPortal1 und LinkPortal2