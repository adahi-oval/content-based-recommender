# Sistemas de recomendación - Modelos basados en el contenido.

## Instrucciones

Para el correcto funcionamiento del programa solo es necesario tener instalado `Python 3`. Esto se puede hacer en sistemas Linux con el siguiente comando:
```bash
sudo apt install python3
```

La ejecución se efectúa con este comando:
```bash
python3 main.py [argumentos]
```

Para el correcto funcionamiento del programa se le deben pasar tres argumentos. Éstos se pueden ver con el comando:
```bash
python3 main.py -h
```

## Descripción del código

### Funciones de entrada y limpieza

En primer lugar, todo lo necesario para el funcionamiento del programa se lee de los documentos pasados por el usuario. Para ello se utiliza un módulo creado por nosotros llamado `docReader`. En este módulo se encuentran 4 funciones en total. 

Las dos primeras funciones, `readDocs` y `readLema` se utilizan para formar las listas en `Python` que utilizaremos a lo largo del programa. La función `readDocs` lee el fichero con los documentos y crea una lista con ellos, también se utiliza para leer la lista de ***stop words*** para crear una lista con ellas. La función `readLema` lee el documento con el cual se crea una lista de tuplas de dos elementos, aprovechando el formato similar al de un diccionario **`JSON`**.

Las dos funciones restantes, `clearStopWords` y `lematizacion` se encargan de formatear los documentos para su posterior análisis.

La primera, `clearStopWords` se encarga de separar el documento proporcionado en una lista de palabras. Esta lista la recorre para encontrar las palabras que no coinciden con las ***stop words*** y juntarlas de nuevo en un documento limpio de ellas.

La segunda, `lematizacion` es similar a la primera, pero esta recorre la lista de palabras buscando las que coindicen con los primeros elementos en la lista de tuplas para sustituirlas por el segundo elemento. 