import pandas as pd
from tensorflow.python.keras.models import load_model
class predic:
   
    def __init__(self):
            a=None
        

    def predecir(self):
            model = load_model("apps/Riesgos/redNeuronalME/modelo_ME.h5")
            print('hola pase')
            """entrada nuevo, para una prediccion"""
            X =pd.read_csv("Eprediccion.csv").values
            """realizar una prediccion con la red neuronal"""
            predicction = model.predict(X)

            """se obtiene la primera linea los nuevos productos"""
            predicccion = predicction[0]
            

            """se pasan desnormalizan los datos de los valores para asi pasarlos a pesos"""
            max = 30
            min = 1
            max_min=max-min
            prediccionFinal = (predicction[0]*(max_min)+min)
            
            return prediccionFinal[0]



   
      
        
       

      
        



        








