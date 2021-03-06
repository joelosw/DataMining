import pandas as pd 
import math
import numpy as np
iris=pd.read_csv("./iris.data", names=None)
iris.columns=['s_length', 's_width', 'p_length', 'p_width', 'type']
iris.type=iris.type.replace({'Iris-setosa':0, 'Iris-versicolor':1, 'Iris-virginica':2})
daten=iris.values.tolist()


def chimerge(data, stop=6, split_on = 0):
    ''' 
    The hear function of the Algorithm. This one takes it all together. 
    It sorts the data and then transforms the list to  a dictionary, where each distinct attribute-value is a key. 
    The according value is a class distribution of this key. 
    It then calculates all chis for each two adjacents dictonary-values.
    The Pair with the least chi-squared value get's merged, by removing the lower value and adding the class distribution to the higher value.

        '''
    data.sort(key = lambda datapoint:datapoint[split_on] )
    liste = [[a] for a in data] # Each Data Point as one Interval 
    #print(liste)
    
    print('Übergibt: ' , liste[0],' und ', liste[1])
    
    #while (max([len(a) for a in list])<=stop):
    #    chissquared(to_be_filled_in)
    sortiert = counted(data, split_on)
    values = list(sortiert.values())
    chis = []

    for a in range(len(values)-1):
        chis.append(chisquared(values[a], values[a+1]))

    while (len(sortiert) > stop):
        
        values = list(sortiert.values())
        chis = []

        for a in range(len(values)-1):
            chis.append(chisquared(values[a], values[a+1]))
        print(chis)
        sortiert = merge(sortiert, chis)
        

    return(split_points(sortiert))

def merge(sortiert, chis):
    ''' Given a dictionary of values with class distribution and a list of chi values, this function merges
    the two adjancent intervalls with the least chi-squared value by removing the lower value and adding the class distribution to the upper one
    '''
    min_ind = np.argmin(chis)
    lower = list(sortiert.keys())[min_ind]
    upper= list(sortiert.keys())[min_ind+1]
    temp=sortiert[upper]
    np.add(temp[1], sortiert[lower])
    sortiert[upper] = temp
    del sortiert[lower]
    print(sortiert)
    return sortiert



def split_points(merged_list):
    ''' This method simply creates a list of splitpoints based on the given dictionary of attribute-values'''

    points=list()
    points.append(0.0)
    
    for a in list(merged_list.keys()):
        points.append(a) 

    print('Points: ', points)
    return points


def counted(liste, split_on):
    ''' This method gets a list of attribute-values and the attribute of interest. 
    It then counts how often the attribute-value occurs for each class. This is returned as a dictionary, with the value as key and 
    the class distribution as dict-value'''
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
    ''' This function calculates the chi-squared value of two given class distributions'''
   # data1 = [sum([1 if datapoint[4]==iris_class else 0 for datapoint in data1]) for iris_class in range(3)]

   # data2 = [sum([1 if datapoint[4]==iris_class else 0 for datapoint in data2]) for iris_class in range(3)]

    # print( 'Data1: ', data1, type(data1), '\n Data2: ', data2)

    rand_h = [sum(data) for data in [data1, data2]]
    rand_v = [sum([data1[a], data2[a]]) for a in range(3)]

    #print('Summe horizontal: ',rand_h,' Summe vertical: ',  rand_v)
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


points = chimerge(daten)
print('Die optimalen diskreten Intervalle lauten: ')
for i in range(len(points)-1):
    print ('\n  {} < x <= {}'.format(points[i], points[i+1]))
 

