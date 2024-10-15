import json
import re
import math
import csv

# Como cada linea es un documento, los separa por lineas usando \n como marcador. Crea un array de documentos
def readDocs(filename):
  with open(filename, "r") as documentos:
    file = documentos.read()
    documentos = file.split("\n")

    return documentos
  

# Version para la lista de lematizacion, lo lee como un diccionario JSON y crea una lista de tuplas de dos elementos
# para que sea más fácil usarlo como queremos
def readLema(filename):
  with open(filename, "r") as doc:
    data = json.load(doc)

  listaTuplas = [(key, value) for key, value in data.items()]

  return listaTuplas


def readCSV(filename):
  datos = []

  with open(filename, newline='') as tabla:
    csvReader = csv.reader(tabla)
    next(csvReader)
    
    for fila in csvReader:
      datos.append([int(fila[0]), fila[1], int(fila[2]), float(fila[3]), float(fila[4])])

  return datos

  
# Funcion para limpiar el documento de stop words, le pasamos la lista de stopwords leida con readDocs
# y el documento que queremos limpiar, busca las palabras que no coinciden y las mete en un array de palabras que luego une  
def clearStopWords(documento, stopWords):

  palabras = documento.split()

  filtered_words = [word for word in palabras if word.lower() not in stopWords]

  cleanDoc = ' '.join(filtered_words)
  
  return cleanDoc


# Version de la limpieza de stopwords que recorre la lista de palabras buscando las que coinciden con el primer elemento
# de las tuplas de la lista de lematización para reemplazarlo por el segundo.
def lematizacion(cleanDoc, listaLematizacion):
  palabras = cleanDoc.split()

  for i in range(len(palabras)):

    word = palabras[i].lower()

    for lema, sustituto in listaLematizacion:
      if word == lema:
        palabras[i] = sustituto

  updatedDoc = ' '.join(palabras)

  return updatedDoc

def separarPalabras(texto):
  # Utiliza una expresión regular para encontrar palabras (secuencias de letras y apóstrofes)
  palabras = re.findall(r'\b\w+\b', texto)
  return palabras

def agregarTerminosConjunto(conjuntoTerminos, arrayTerminos):
  for palabra in arrayTerminos:
    conjuntoTerminos.add(palabra)
  return conjuntoTerminos

def convertirAMinusculas(cadenas):
  # Aplica lower() a cada cadena en el vector
  cadenasMinusculas = [cadena.lower() for cadena in cadenas]
  return cadenasMinusculas

# Cuenta cuántas veces aparece el término en el documento
def calcularTF(termino, documento):
  tf = documento.count(termino)
  return tf

def calcularIDF(termino, palabrasPorDocumentos):
  # Cuenta cuántos documentos contienen la termino
  numeroDocumentosConTermino = sum(1 for documento in palabrasPorDocumentos if termino in documento)
  # Calcula el IDF utilizando el logaritmo neperiano
  idf = math.log(len(palabrasPorDocumentos) / (numeroDocumentosConTermino))
  return idf

def crearTablaDocumento(tabla, nombreArchivo):
  # Abre el archivo en modo de escritura
  with open(nombreArchivo, mode='w', newline='') as archivo_csv:
    # Crea un escritor CSV
    escritor = csv.writer(archivo_csv)
    # Escribe la fila de encabezado
    escritor.writerow(["Índice del término", "Término", "TF", "IDF", "TF-IDF"])
    
    # Escribe las filas de datos desde la tabla
    for fila in tabla:
      escritor.writerow(fila)

def crearTablaCoseno(tabla, nombreCoseno):
  
  with open(nombreCoseno, mode="w", newline='') as tabla_coseno:

    escritor = csv.writer(tabla_coseno)

    escritor.writerow(["Primer Documento", "Segundo Documento", "Similaridad Coseno"])

    for fila in tabla:
      escritor.writerow(fila)

def calcularCoseno(doc1, doc2):
  magnitud1 = math.sqrt(sum(termino[1]**2 for termino in doc1))
  magnitud2 = math.sqrt(sum(termino[1]**2 for termino in doc2))

  norm1 = [(termino[0], termino[1]/magnitud1) for termino in doc1]
  norm2 = [(termino[0], termino[1]/magnitud2) for termino in doc2]

  similaridad = 0

  for termino in norm1:
    for otherTermino in norm2:
      if termino[0] == otherTermino[0]:
        similaridad += (termino[1] * otherTermino[1])

  return similaridad



def terminoPerteneceMatriz(termino, matriz):
  for fila in matriz:
    if termino == fila[1]:
      return True
  return False
