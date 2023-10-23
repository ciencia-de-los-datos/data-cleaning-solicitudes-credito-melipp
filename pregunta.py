"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():
    
    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    #
    # Inserte su código aquí
    #
    #print(df.dtypes)

    #eliminar datos faltantes y duplicados
    df.dropna(inplace=True)
    

    #volver todo minusculas y eliminar espacios al inicio y al final
    df["sexo"] = df["sexo"].apply(lambda x: str(x).lower().strip())
    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].apply(lambda x: str(x).lower().strip())
    df["idea_negocio"] = df["idea_negocio"].apply(lambda x: str(x).lower().strip())
    #df["barrio"] = df["barrio"].apply(lambda x: str(x).lower().strip())
    #df["estrato"] = df["estrato"].apply(lambda x: str(x).lower().strip())
    #df["comuna_ciudadano"] = df["comuna_ciudadano"].apply(lambda x: str(x).lower().strip())
    #df["fecha_de_beneficio"] = df["fecha_de_beneficio"].apply(lambda x: str(x).lower().strip())
    df["monto_del_credito"] = df["monto_del_credito"].apply(lambda x: str(x).lower().strip())
    df["línea_credito"] = df["línea_credito"].apply(lambda x: str(x).lower().strip())


    #reemplazar guiones por espacios
    df["idea_negocio"] = df["idea_negocio"].apply(lambda x: str(x).replace("-"," ").replace("_"," ").strip())
    df["barrio"] = df["barrio"].apply(lambda x: str(x).lower().replace("_"," ").replace("-"," "))
    df["línea_credito"] = df["línea_credito"].apply(lambda x: str(x).lower().replace("-", " ").replace("_", " ").strip())

    #modificar formato fecha
    df["fecha_de_beneficio"] = pd.to_datetime(df["fecha_de_beneficio"], dayfirst=True)

    #monto eliminar signo $, y limpiar
    df["monto_del_credito"] = df["monto_del_credito"].apply(lambda x: str(x).strip("$").strip().replace(".00", "").replace(",", ""))
    
    #eliminar columna Unnamed del dataFrame
    df.drop(['Unnamed: 0'], axis=1,inplace=True)
    
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    
    return df