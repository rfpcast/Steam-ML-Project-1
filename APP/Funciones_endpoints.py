import pandas as pd
import numpy as np

df_endpoints_1 = pd.read_csv('Endpoints_df/Endpoint_1.csv')
df_endpoints_2 = pd.read_csv('Endpoints_df/Endpoint_2.csv')
df_endpoints_3 = pd.read_csv('Endpoints_df/Endpoint_3.csv')
df_endpoints_4 = pd.read_csv('Endpoints_df/Endpoint_4.csv')
df_endpoints_5 = pd.read_csv('Endpoints_df/Endpoint_5.csv')

sim_coseno = np.load('Endpoints_df/sim_coseno.npy')

df_MLM = pd.read_csv('Endpoints_df/data_MLM_1.csv')


def endpoint1(genero: str):

    if genero in df_endpoints_1['Gen'].values:

        mensaje = df_endpoints_1.loc[df_endpoints_1['Gen']
                                     == genero, 'Mensaje'].values[0]
        return mensaje
    else:
        return (f"No se encuentra '{genero}' en la lista.")


def endpoint2(genero: str):

    if genero in df_endpoints_2['Genero'].values:

        mensaje = df_endpoints_2.loc[df_endpoints_2['Genero']
                                     == genero, 'mensaje'].values[0]
        return mensaje
    else:
        return (f"No se encuentra '{genero}' en la lista.")


def endpoint3(anio: int):

    if anio in df_endpoints_3['posted'].values:

        mensaje = df_endpoints_3.loc[df_endpoints_3['posted']
                                     == anio, 'Top 3 Games'].values[0]
        return mensaje
    else:
        return (f"No se encuentra '{anio}' en la lista.")


def endpoint4(anio: int):

    if anio in df_endpoints_4['posted_x'].values:

        mensaje = df_endpoints_4.loc[df_endpoints_4['posted_x']
                                     == anio, 'Worst 3 Games'].values[0]
        return mensaje
    else:
        return (f"No se encuentra '{anio}' en la lista.")


def endpoint5(dev: str):

    if dev in df_endpoints_5['developer'].values:

        mensaje = df_endpoints_5.loc[df_endpoints_5['developer']
                                     == dev, 'mensaje'].values[0]
        return mensaje
    else:
        return (f"No se encuentra '{dev}' en la lista.")


def modelo_recomendacion(id: int):

    idx = df_MLM[df_MLM['id'] == id].index[0]
    juegos_rec = df_MLM['app_name'].iloc[sim_coseno[idx]]

    msj = {'recommendations': None}
    msj['recommendations'] = list(juegos_rec)

    return msj
