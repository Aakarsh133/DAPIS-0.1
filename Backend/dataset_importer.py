import pandas as pd

def importer():
    df= pd.read_csv("/home/aakarsh/Downloads/Share of Students Studying Abroad.csv")
    print(df.head())