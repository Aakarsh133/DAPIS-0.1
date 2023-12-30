import pandas as pd

def importer(i, src):
    def import_csv(add):
        df= pd.read_csv(add)
        
        return df 

    def import_excel(add):
        df= pd.read_excel(add)
        
        return df 

    if (i==1):
        return import_csv(src)
    elif (i==2):
        return import_excel(src)