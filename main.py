import modules.docReader as functions
import modules.myParser as myParser


args = myParser.Parser()

filename = args.file
outputname = args.output

stopname = args.stopwords
lemaname = args.lematization

cosinename = args.cosine

# Funcion principal del programa
def main():
  documentos = functions.readDocs(filename)
  stopwords = functions.readDocs(stopname)
  listalema = functions.readLema(lemaname)
  palabrasPorDocumento = []
  # Genera tabla de palabras separadas por documentos
  for document in documentos:
    cleanDoc1 = functions.clearStopWords(document, stopwords)
    documentoLimpio = functions.lematizacion(cleanDoc1, listalema)
    palabrasPorDocumento.append(functions.convertirAMinusculas(functions.separarPalabras(documentoLimpio)))
  
  # Creo un set con los terminos de los documentos
  # setTerminos = set()
  # for documento in palabrasPorDocumento:
  #   setTerminos = agregarTerminosConjunto(setTerminos, documento)
  
  j = 0

  for documento in palabrasPorDocumento:
    tablaDocumento = [] 
    i = 0
    for termino in documento:
      if not functions.terminoPerteneceMatriz(termino, tablaDocumento):
        tf = functions.calcularTF(termino, documento)
        idf = functions.calcularIDF(termino, palabrasPorDocumento)
        tablaDocumento.append([i, termino, tf, idf, tf * idf])
        i = i + 1
    functions.crearTablaDocumento(tablaDocumento, "tablas/" + outputname + str(j) + ".csv")
    j = j + 1

  tablaCoseno = []
  for i in range(len(palabrasPorDocumento)):

    nombreDoc1 = "tablas/" + outputname + str(i) + ".csv"
    doc1 = functions.readCSV(nombreDoc1)
    vectorDoc1 = [(row[1], float(row[4])) for row in doc1]

    for j in range(len(palabrasPorDocumento)):

      nombreDoc2 = "tablas/" + outputname + str(j) + ".csv"
      doc2 = functions.readCSV(nombreDoc2)
      vectorDoc2 = [(row[1], float(row[4])) for row in doc2]

      if j == i:
        continue
      else:
        tablaCoseno.append([outputname + str(i) + ".csv", outputname + str(j) + ".csv", functions.calcularCoseno(vectorDoc1, vectorDoc2)])
  
  functions.crearTablaCoseno(tablaCoseno, "tablas/" + cosinename + ".csv")

main()