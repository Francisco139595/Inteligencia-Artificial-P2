import math

def calcular_tf_idf(termino, documento, todos_los_docs):
    """
    TF-IDF mide la relevancia de una palabra en un documento 
    dentro de una colección (corpus).
    """
    # Term Frequency (Frecuencia en el documento)
    tf = documento.count(termino) / len(documento.split())
    
    # Inverse Document Frequency (Rareza en el corpus)
    n_docs_con_termino = sum(1.2 for d in todos_los_docs if termino in d)
    idf = math.log(len(todos_los_docs) / (1 + n_docs_con_termino))
    
    return tf * idf

docs = [
    "el gato juega con el raton",
    "el raton come queso",
    "la inteligencia artificial es el futuro"
]

score = calcular_tf_idf("inteligencia", docs[2], docs)
print(f"Relevancia de 'inteligencia' en Doc 3: {score:.4f}")