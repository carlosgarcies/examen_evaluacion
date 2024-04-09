import pandas as pd

def leer_df(nombre_csv):
    df=pd.read_csv(nombre_csv)
    df["TS"]=pd.to_datetime(df["TS"])
    return df

def filtro_media(df):
    media_filtrado=df[df["Tag"]=="Examen_Carlos"]["Value"].mean()
    return media_filtrado
