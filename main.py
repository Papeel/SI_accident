import pandas as pd
import time
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.models import Model
from tensorflow.keras import optimizers,utils
from tensorflow import sigmoid
import numpy as np
import matplotlib.pyplot as plt



def notIndex(v, matriz):
    index = []
    for i in range(matriz.shape[0]):
        if i not in v:
            index.append(i)

    return index


# Configuración del conjunto de datos
data_yes = np.loadtxt("yes.csv", delimiter=",")
data_no = np.loadtxt("no.csv", delimiter=",")

#Creamos modelo

input = inputs = Input(shape=(12,))
net = input
net = Dense(20, input_dim=12, activation='relu',kernel_initializer='normal')(net)
net = Dense(32,  activation='sigmoid',kernel_initializer='normal')(net)
net = Dense(1, activation='sigmoid',kernel_initializer='normal')(net)

output = net

model = Model(inputs=input, outputs=output)
# Compila el modelo
model.compile(loss='mean_squared_logarithmic_error', optimizer='adam', metrics=['accuracy'])

#Entrenamiento
mean = []
for i in range(10):

    index_no = np.random.randint(data_no.shape[0], size=2500)
    index_yes = np.random.randint(data_yes.shape[0], size=2500)

    no = data_no[index_no[:2000], :]
    no_val = data_no[index_no[2000:2500], :]

    yes = data_yes[index_yes[:2000], :]
    yes_val = data_yes[index_yes[2000:2500], :]

    data = np.concatenate((no, yes), axis=0)
    data_val = np.concatenate((no_val, yes_val), axis=0)
    np.random.shuffle(data)
    np.random.shuffle(data_val)

    X = data[:, 1:13]

    Y = data[:, 13]

    x_val = data_val[:, 1:13]
    y_val = data_val[:, 13]

    history = model.fit(X, Y, validation_data=(x_val, y_val), epochs=20, batch_size=25,shuffle=True)
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('Error del modelo')
    plt.ylabel('Error')
    plt.xlabel('epocas')
    plt.legend(['Entrenamiento', 'test'], loc='upper left')
    plt.show()

    index_no = notIndex(index_no,data_no)
    index_yes = notIndex(index_yes,data_yes)
    no = data_no[index_no]
    yes = data_yes[index_yes]
    data = np.concatenate((no, yes), axis=0)

    mean.append(model.evaluate(data[:, 1:13], data[:, 13])[0])

# evalua el modelo


sum = 0.
for d in mean:
    print(str(d))
    sum = sum + float(d)

sum = sum/10.

print("El error medio es :" + str(sum))

model.save('my_model.h5')




