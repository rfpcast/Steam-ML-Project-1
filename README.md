# Steam-ML-Project-1

Este proyecto consiste en la puesta en practica de una solucion de negocio para la empresa Valve y la plataforma de video juegos Steam, en este Readme presentaremos en detalle el proceso y la logica para la consecusion de esta Solucion

## Descripcion del proyecto

El objetivo es crear un sistema de recomendación de videojuegos para usuarios, basados en 6 Endpoints que entregaran una serie de datos para que el usuario tenga una nocion de cuales juegos y generos son mas populares y cuales se ajustan mejor 
a sus intereses, para esto, se ha decidido la implementación y prueba de una API utilizando el framework FastAPI para alojar múltiples consultas de Endpoints, así como un modelo de aprendizaje automático de similitud de coseno.

--------------------
## Paso 1: EDA y ETL del dataset

El dataset esta compuesto por los datos de los usuarios de australia entre los años 2010 y 2015, junto con los lanzamientos de videojuegos en ese periodo, este dataset permite generar un MVP que sirve para mostrar la potencialidad de la solucion.

Los datos sin procesar son volcados a Dataframes, se hace un proceso de EDA para saber las dimensiones, el estado general del dataset, la consistencia y limpieza de los datos, el tipos de datos con el que se esta trabajando, se deciden que datos son utiles y cuales son desechables, una vez hecho esto limpian los datos de nulos y duplicados donde sea necesario, para volcar estos datos en una serie de dataframes que luego seran transformados en archivos CSV, y que seran usados para crear los dataframes finales.  

El proceso de limpieza y analisis de estos datos se encuentraen el documento **"EDA_ETL_Steam_project1.ipynb"** formato notebook, los archivos CSV resultantes de este proceso, no se encuentran en este repositorio debido a limite de almacenamiento de github, 
sino en este **[Link](https://drive.google.com/drive/folders/1PN95A5XpdLzjwuS850WrxUvORgMx04wy)** se deben descargar en la carpeta **"ETL_Dataset/Data"** desde donde pueden ser cargadas a Dataframe.

## Paso 2: Analisis de sentimiento con modelo NLP 

Uno de los pasos fundamentales para creacion de las funciones que van a servir como endpoint de la aplicacion, es la construccion de un modelo capaz de procesar los comentarios y recomendaciones de los usuarios, para esto se ha creado un modelo de 
procesamiento de lenguaje natural que lee las reseñas guardadas en el archivo **'user_reviews'** y les atribuye el valor de 1 si es positiva, 0 si es neutra o -1 si es negativa, la construccion detallada del modelo esta en el archivo **"FE_Model_Steam_project1.ipynb"** 

Este modlo sirve para la construccion de los dataframes finales que seran utilizados en la construccion de los endpoints

## Paso 3: Sistema de recomendacion con matriz vectorial y similitud de coseno

Una de las funciones mas importantes de la API es un sistema de recomendacion que permite al colocar el numero de id de juego, recibir 3 o mas recomendaciones de contenido similar, para esto se uso los datos recopilados previamente CSV para generar un modelo
de recomendacion basado en similitud de coseno, para esto se importan librearias de scikit, para vectorizar con valores con TF IDF una verz vectorizados se agrupan para formar una matriz de vectores y aplicar la reduccion de la dimensionalidad a traves de SVD
y por ultimo hacer uso de la formula de la similitud de coseno, para al tomar sus indices se puede guardar y usar en el deployment de los endpoints, el desarrollo detallado de este modelo de recomendacion esta en el archivo **"ML_Model_Steam_project1"**

## Paso 4: Proceso de ETL para la generacion de los endpoints de la APP

