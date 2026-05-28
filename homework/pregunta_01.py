"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""


import os
import pandas as pd

def pregunta_01():
    #Leemos el archivo
    os.makedirs("files/output", exist_ok=True)
    df = pd.read_csv("files/input/solicitudes_de_credito.csv", sep=";", index_col=0)
    #Limpiamos Texto
    df["sexo"] = df["sexo"].str.lower()
    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.lower().str.strip()
    df["idea_negocio"] = df["idea_negocio"].str.lower().str.replace("_", " ", regex=False).str.replace("-", " ", regex=False).str.strip()
    df["barrio"] = df["barrio"].str.lower().str.replace("-", " ", regex=False).str.replace("_", " ", regex=False)
    df["línea_credito"] = df["línea_credito"].str.lower().str.strip().str.replace("-", " ", regex=False).str.replace("_", " ", regex=False).str.strip()
    #Arreglamos fechas
    #Intentamos parsear con formato dd/mm/aaaa. Si no puede, pone NaT y luego los NaT los pone como fecha correctamente
    df["fecha_de_beneficio"] = (pd.to_datetime(df["fecha_de_beneficio"], format="%d/%m/%Y", errors="coerce")
    .combine_first(pd.to_datetime(df["fecha_de_beneficio"], format="%Y/%m/%d", errors="coerce")))
    #Limpiamos monto
    # conviertimos todo a string primero luego arreglamos y limpiamos los caracteres y lo volvemos a poner en decimales
    df["monto_del_credito"] = (df["monto_del_credito"].astype(str).str.strip().str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False).str.replace(" ", "", regex=False).astype(float))

    #Eliminamos duplicados y nulos
    df=df.drop_duplicates()
    df=df.dropna()
    #Creamos el archivo csv en output
    df.to_csv("files/output/solicitudes_de_credito.csv", sep=";", index=False)


if __name__ == "__main__":
    pregunta_01()


    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
   


