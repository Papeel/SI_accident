
import pandas as pd
import time
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.models import Model, load_model
from tensorflow.keras import optimizers
from tensorflow import sigmoid

import numpy as np

model = load_model('my_model.h5')




# Configuración del conjunto de datos
data_no = np.loadtxt("no.csv", delimiter=",")
data_yes = np.loadtxt("yes.csv", delimiter=",")


print(model.predict(data_no[:10, 1:13]))
print(model.predict(data_yes[1000:1010, 1:13]))