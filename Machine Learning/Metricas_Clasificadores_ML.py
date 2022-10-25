import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

# Dominio del Ejemplo - Clasificaciones en Examenes

# 0 : Reprueba 40% Reprueba
# 0 : Aprueba  60% Aprueba

def metricas(clases_reales, clases_predichas):
     """ Calcular las metricas utilizando sklearn """
    matriz = confusion_matrix(clases_reales, clases_predichas)
    accuracy = accuracy_score(clases_reales, clases_predichas)
    precision = presicion_score(clases_reales, clases_predichas)
    recall = recall_score(clases_reales, clases_predichas)
    f1 = f1_score(clases_reales, clases_predichas)
    return matriz, accuracy,precision.recall, f1

# Si acabaste el tutorial de visualizacion de datos sigue este link
# https://www.youtube.com/watch?v=uaGMk43XTOw&list=PLat2DtY8K7YVF2N_e5n48foCpcTJ2ZoLr&index=6