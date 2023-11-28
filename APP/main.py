
import Funciones_endpoints as fe
from fastapi import FastAPI


app = FastAPI()


@app.get("/PlayTimeGenre/")
async def PlayTimeGenre(genero: str):
    """
    Debe devolver año con mas horas jugadas para dicho género

    Ejemplo de retorno: {"Año de lanzamiento con más horas jugadas para Género X": 2013}
    """
    return fe.endpoint1(genero)


@app.get("/UserForGenre/")
async def UserForGenre(genero: str):
    """
    Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.

    Ejemplo de retorno: {"Usuario con más horas jugadas para Género X": "us213ndjss09sdf", "Horas jugadas": [{"Año": 2013, "Horas": 203}, 
    {"Año": 2012, "Horas": 100}, {"Año": 2011, "Horas": 23}]}
    """
    return fe.endpoint2(genero)


@app.get("/UsersRecommend")
async def UsersRecommend(año: int):
    """
    Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)

    Ejemplo de retorno: [{"Puesto 1": X}, {"Puesto 2": Y}, {"Puesto 3": Z}]
    """
    return fe.endpoint3(año)


@app.get("/UsersWorstDeveloper")
async def UsersWorstDeveloper(año: int):
    """
    Devuelve el top 3 de desarrolladoras con juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)

    Ejemplo de retorno: [{"Puesto 1": X}, {"Puesto 2": Y}, {"Puesto 3": Z}]
    """
    return fe.endpoint4(año)


@app.get("/sentiment_analysis")
async def sentiment_analysis(empresa_desarrolladora: str):
    """
    Según la empresa desarrolladora, se devuelve un diccionario con el nombre de la desarrolladora como llave y una lista con la cantidad 
    total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor.

    Ejemplo de retorno: {'Valve': {'Negative': 182, 'Neutral': 120, 'Positive': 278}}
    """
    return fe.endpoint5(empresa_desarrolladora)


@app.get("/recomendacion_juego")
async def recomendacion_juego(id_producto: int):
    """
    Ingresando el id de producto, deberíamos recibir una lista con 5 juegos recomendados similares al ingresado.

    """
    return fe.modelo_recomendacion(id_producto)
