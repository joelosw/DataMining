import pandas as pd 
import math
import numpy as np
iris=pd.read_csv("./iris.data", names=None)
iris.columns=['s_length', 's_width', 'p_length', 'p_width', 'type']
iris.type=iris.type.replace({'Iris-setosa':0, 'Iris-versicolor':1, 'Iris-virginica':2})
daten=iris.values.tolist()


def chimerge(data, stop=6, split_on = 0):
    data.sort(key = lambda datapoint:datapoint[split_on] )
    liste = [[a] for a in data] # Each Data Point as one Interval 
    #print(liste)
    
    print('Übergibt: ' , liste[0], ' und ', liste[1])
    
    #while (max([len(a) for a in list])<=stop):
    #    chissquared(to_be_filled_in)
    sortiert = counted(data, split_on)
    values = list(sortiert.values())
    chis = []

    for a in range(len(values)-1):
        chis.append(chisquared(values[a], values[a+1]))

    minimum_index = np.argwhere(chis == min(chis))
    

    
    print(chis)


def counted(liste, split_on):
    counted_dict = dict()
    for datapoint in liste:
        length = datapoint[split_on]
        if length not in counted_dict.keys():
            #print('In If, hinzugefügt: ', length )
            counted_dict[length] = [0,0,0]
           
        counted_dict[length] [int(datapoint[4])] += 1 #at the according place in the dictionary increse the appropriate count (assuming that the class-number is the last one in the datapoint))
    print(counted_dict)
    return counted_dict

def chisquared(data1, data2):
   # data1 = [sum([1 if datapoint[4]==iris_class else 0 for datapoint in data1]) for iris_class in range(3)]

   # data2 = [sum([1 if datapoint[4]==iris_class else 0 for datapoint in data2]) for iris_class in range(3)]

    # print( 'Data1: ', data1, type(data1), '\n Data2: ', data2)

    rand_h = [sum(data) for data in [data1, data2]]
    rand_v = [sum([data1[a], data2[a]]) for a in range(3)]

    print('Summe horizontal: ',rand_h,' Summe vertical: ',  rand_v)
    n=len(data1) + len(data2)

    data12= [data1, data2]

    chi2 = 0

    for reiheind, reihe in enumerate(data12):
        for elementind, element in enumerate(reihe): 
                E = rand_h[reiheind]*rand_v[elementind]/n

                if E != 0:
                    
                    chi2 += (reihe[elementind] - (E))**2 / max([E, 0.5])


        #print( 'Date 1: ', data1, '\n Data2: ', data2)
    
    return chi2

print(chimerge(daten))

