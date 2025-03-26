# Datos de la matriz de confusión
TP = 40
TN = 30
FP = 20
FN = 10

# Cálculo de las métricas
accuracy = (TP + TN) / (TP + TN + FP + FN)
precision = TP / (TP + FP)
recall = TP / (TP + FN)
f1_measure = 2 * (precision * recall) / (precision + recall)

# Mostrar resultados
print("Resultados del clasificador k-NN:")
print(f"Accuracy (Exactitud): {accuracy:.2f} o {accuracy*100:.2f}%")
print(f"Precision (Precisión): {precision:.4f} o {precision*100:.2f}%")
print(f"Recall (Sensibilidad): {recall:.2f} o {recall*100:.2f}%")
print(f"F1-Measure (Puntuación F1): {f1_measure:.4f} o {f1_measure*100:.2f}%")
