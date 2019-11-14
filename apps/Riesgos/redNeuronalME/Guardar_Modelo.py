import pandas as pd
from keras.layers import Dense
from keras.models import Sequential

training_data_df = pd.read_csv("apps/Riesgos/redNeuronalME/dataset/dataset_pruebas_escalado.csv", sep=',')

# borrar la columna de la salida para obtener solo los datos de entrada ya normalizado"""
X = training_data_df.drop('salida', axis=1).values

# obtener solo la columna de salida del dataset ya normalizado"""
Y = training_data_df[['salida']].values

# red neuronal vacia"""
model = Sequential()
# capa 1 interna de la red neuronal con 50 nodos, input_dim :con 9 entradas de el dataset(son 9 columnas del dataset)
# por ultimo la funcion de activación relu"""
model.add(Dense(50, input_dim=63, activation='sigmoid'))
# capa 2 de la red con con 100 nodos y una funcion de activacion relu"""
model.add(Dense(100, activation='sigmoid'))
# capa 3 de la red con con 50 nodos y una funcion de activacion relu"""
model.add(Dense(100, activation='sigmoid'))
# capa 4 de la red con con 100 nodos y una funcion de activacion relu"""
model.add(Dense(100, activation='relu'))

model.add(Dense(1, activation='linear'))
# se compila la red, loss = metrica de la presicion de la red neuronal y el algoritmo de optimizacion adam"""
model.compile(loss="mean_squared_error", optimizer="adam")

# entrenar el modelo(red neuronal)"""
# X =datos de entrenamiento entrada"""
# Y =datos entrenamiento salida"""
# epochs =cantidad de iteraciones que realiza la red"""
# shuffle =ordear aleatoreamente los datos de entrenamiento"""
# verbose =imprimir informacion detallada(documentar entrenamiento)"""
model.fit(
    X,
    Y,
    epochs=500,
    shuffle=True,
    verbose=2
)

test_data_df = pd.read_csv("apps/Riesgos/redNeuronalME/dataset/datos_prueba_escalado.csv", sep=',')

# borrar la columna de la salida para obtener solo los datos de entrada ya normalizado de prueba"""
X_test = test_data_df.drop('salida', axis=1).values

# obtener solo la columna de salida del dataset de prueba ya normalizado"""
Y_test = test_data_df[['salida']].values
# error de la precion con respecto a los datos de prueba"""
test_error_rate = model.evaluate(X_test, Y_test, verbose=0)

print(" ERROR : {}".format(test_error_rate))

# guardar el modelo"""
model.save("modelo_ME.h5")
print("modelo guardado")