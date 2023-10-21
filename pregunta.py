"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():
    
    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    
    df.rename(columns = {'Unnamed: 0': 'index'}, inplace = True)
    df.set_index('index', inplace = True)
    df.sexo = df.sexo.str.lower()
    df.sexo = df.sexo.astype('category')
    df.tipo_de_emprendimiento = df.tipo_de_emprendimiento.str.lower()
    df.tipo_de_emprendimiento = df.tipo_de_emprendimiento.astype('category')
    df.idea_negocio = df.idea_negocio.str.lower().str.strip('_').str.strip('-').str.strip().str.replace('_',' ').str.replace('-',' ')
    df.idea_negocio = df.idea_negocio.astype('category')
    df.barrio = df.barrio.str.lower().str.replace('_','-').str.replace("-", " ")
    df.comuna_ciudadano = df.comuna_ciudadano.astype('Int64')
    df.comuna_ciudadano = df.comuna_ciudadano.astype('category')
    df.fecha_de_beneficio = pd.to_datetime(df.fecha_de_beneficio, dayfirst = True)
    df.monto_del_credito = df.monto_del_credito.str.replace('$','').str.replace(',','')
    df.monto_del_credito = df.monto_del_credito.astype(float)
    df.línea_credito = df.línea_credito.str.lower().str.strip('_').str.strip('-').str.strip().str.replace('_',' ').str.replace('-',' ')
    df.dropna(inplace = True)
    df.drop_duplicates(inplace = True)
    
    return df