

from tensorflow.keras.models import Model, load_model

import numpy as np

model = load_model('Modelos/0_036.h5')




# Configuración del conjunto de datos
data_no = np.loadtxt("no.csv", delimiter=",")
data_yes = np.loadtxt("yes.csv", delimiter=",")

index_no = np.random.randint(data_no.shape[0], size=10)
index_yes = np.random.randint(data_yes.shape[0], size=10)
data = np.concatenate((data_yes[index_yes, 1:13],data_no[index_no, 1:13]),axis=0)
np.random.shuffle(data)


print(model.predict(data))
import tkinter as tk

counter = 0



def config(label,i):
    color = ("red", "orange", "yellow", "light green", "dark green")
    label.config(bg= color[i])

def predict():
    global counter
    global label
    counter += 1
    if counter ==20:
        counter = 0
    predict = model.predict([[data[counter, :]]])

    print(str(predict))
    if predict < 0.2:
        config(label, 4)
    elif predict < 0.4:
        config(label, 3)
    elif predict < 0.6:
        config(label, 2)
    elif predict < 0.8:
        config(label, 1)
    else:
        config(label, 0)


root = tk.Tk()
root.title("Detector")
label = tk.Label(root, text="Dange")
label.pack()

button = tk.Button(root, text='Next', width=25, command=predict)
button.pack()
root.mainloop()

#print(model.predict(data_no[:10, 1:13]))
#print(model.predict(data_yes[1000:1010, 1:13]))