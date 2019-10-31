import pandas as pd
from sklearn.preprocessing import MinMaxScaler

training_data_df = pd.read_csv("apps/Riesgos/redNeuronalME/dataset/datasetEntrenamiento.csv",sep = ',')

test_data_df = pd.read_csv("apps/Riesgos/redNeuronalME/dataset/datasetPruebasSalida.csv",sep = ';')

scaler = MinMaxScaler(feature_range=(0, 1))

scaled_training = scaler.fit_transform(training_data_df)
scaled_testing = scaler.transform(test_data_df)

"""print("Note: total_earnings values were scaled by multiplying by {:.10f} and adding {:.6f}".format(scaler.scale_[5], scaler.min_[1]))"""

scaled_training_df = pd.DataFrame(scaled_training, columns=training_data_df.columns.values)
scaled_testing_df = pd.DataFrame(scaled_testing, columns=test_data_df.columns.values)


scaled_training_df.to_csv("dataset_pruebas_escalado.csv", index=False)
scaled_testing_df.to_csv("datos_prueba_escalado.csv", index=False)