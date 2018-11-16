import pandas as pd
import time
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.models import Model
from tensorflow.keras import optimizers
from tensorflow import sigmoid
import numpy as np
def categoriza(data):
    id = 1.
    dic = {}
    index = []
    for i, d in enumerate(data):
        if d ==" ":
            index.append(i)
            continue
        if d in dic.keys():
            data[i] = dic[d]
        else:
            dic[d] = id
            data[i] = id
            id = id + 1.
    return index

def categoriza_l(data):
    id = 0
    dic = {}
    index = []
    for i, d in enumerate(data):
        if d ==" ":
            index.append(i)
            continue
        if d in dic.keys():
            data[i] = dic[d]
        else:
            dic[d] = id
            data[i] = id
            id = id + 1
    return index
def date_to_seconds(data):
    for i, d in enumerate(data):
        data[i] = time.mktime(data[i].timetuple())

def parse_float(v):
    index = []
    for i, n in enumerate(v):
        try:
            v[i] = float(n);
        except Exception:
           index.append(i)

    return index


def writeCSV(v, openFile):

    pri = True

    for d in v:
        if pri:
            pri = False
            openFile.write(str(d))
        else:
            openFile.write(","+str(d))

    openFile.write("\n")

# Configuración del conjunto de datos
xl = pd.ExcelFile('Datos_PrActica_2_CONJUNTO_1.xls')

df = xl.parse(0, parse_dates=['FECHA_HORA'], dayfirst = True)

data = df.get_values()
no_1 = 0
yes_1 = 0
for v in data:
    if v[13]=='Yes':
        yes_1 = yes_1 + 1

    else:
        no_1 = no_1 +1

data = np.delete(data,categoriza(data[:,8]),0)
data = np.delete(data,categoriza(data[:,9]),0)
data = np.delete(data,categoriza(data[:,12]),0)
data = np.delete(data,categoriza_l(data[:,13]),0)

date_to_seconds(data[:,0])
data = np.delete(data,parse_float(data[:,1]),0)
data = np.delete(data,parse_float(data[:,2]),0)
data = np.delete(data,parse_float(data[:,3]),0)
data = np.delete(data,parse_float(data[:,4]),0)
data = np.delete(data,parse_float(data[:,5]),0)
data = np.delete(data,parse_float(data[:,6]),0)
data = np.delete(data,parse_float(data[:,7]),0)
data = np.delete(data,parse_float(data[:,10]),0)
data = np.delete(data,parse_float(data[:,11]),0)

yes = 0;
no = 0;
file_no = open("no.csv",'w')
file_yes = open("yes.csv",'w')

for v in data:
    if v[13]==1:
        yes = yes + 1
        writeCSV(v, file_yes)
    else:
        no = no +1
        writeCSV(v, file_no)


file_yes.close()
file_no.close()
print("No: " + str(no) + "\nYes: " + str(yes) )
print("No: " + str(no_1) + "\nYes: " + str(yes_1) )