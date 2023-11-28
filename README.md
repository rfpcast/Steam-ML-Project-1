# Steam-ML-Project-1

Este proyecto consiste en la puesta en practica de una solucion de negocio para la empresa Valve y la plataforma de video juegos Steam, en este Readme presentaremos en detalle el proceso y la logica para la consecusion de esta Solucion

## Descripcion del proyecto

El objetivo es crear un sistema de recomendación de videojuegos para usuarios, basados en 6 funciones que entregaran una serie de datos para que el usuario tenga una nocion de cuales juegos y generos son mas populares y cuales se ajustan mejor 
a sus intereses, para esto, se ha decidido la implementación y prueba de una API utilizando el marco FastAPI para alojar múltiples consultas de Endpoints, así como un modelo de aprendizaje automático de similitud de coseno.

--------------------
## Procesamiento de los datos ETL y limpieza

El dataset esta compuesto por los datos de los usuarios de australia entre los años 2010 y 2015, junto con los lanzamientos de videojuegos en ese periodo, este dataset permite generar un MVP que sirve para mostrar la potencialidad de la solucion.

Los datos sin procesar son volcados a Dataframes, se hace un proceso de EDA para saber las dimensiones, el estado general del dataset, la consistencia y limpieza de los datos, el tipos de datos con el que se esta trabajando, se deciden que datos son utiles y cuales son desechables, una vez hecho esto limpian los datos de nulos y duplicados donde sea necesario, para volcar estos datos en una serie de dataframes que luego seran transformados en archivos CSV, y que seran usados para crear los dataframes finales.  

El proceso de limpieza y analisis de estos datos se encuentraen el documento **"EDA_ETL_Steam_project1.ipynb"** formato notebook, los archivos CSV resultantes de este proceso, no se encuentran en este repositorio debido a limite de almacenamiento de github, 
sino en este [Link](https://drive.google.com/drive/folders/1PN95A5XpdLzjwuS850WrxUvORgMx04wy) se deben descargar en la carpeta **"ETL_Dataset/Data"** de la carpeta desde donde pueden ser cargadas a Dataframe en el mencionado doumento "EDA_ETL_Steam_project1"

## 1. Datos sin procesar

El dataset se recibio en formato JSON compreso (*json.gz), se volcaron los datos a Dataframes, iterando en las filas del documento y guardando el resultado en listas que posteriormente se convirtieron en dataframes,  
