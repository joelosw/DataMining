import math
import pandas as pd
def entropy(class_label_count_list):
    """ Expected in Form [count1, count 2,...] """
    print(class_label_count_list)
    total_count = sum(a for a in class_label_count_list)
    if 0 in class_label_count_list:
        return 0
    info= - sum([p/total_count * math.log2(p /total_count) for p in class_label_count_list]) 
    print('Needed Expected Bits: ', info )
    return info 

def entropy_for_counted_data(data):
    """ Expects a partition of Data, with information about how many Tupel there are in each subspilt"""


def info_a (dataframe):

    ''' Expects Dataframe with columns "attribute", "count", "class" '''

    distinct = []
    for value in dataframe["attribute"]:
        if value not in distinct:
            distinct.append(value)

    class_labels = []
    for value in dataframe["class"]:
        if value not in class_labels:
            class_labels.append(value)
    print(class_labels)
    info_a = 0 
    
    for j in distinct:
        Dj = dataframe[dataframe["attribute"] == j]

        class_count=[]
        for one_class in class_labels:
            count = sum(Dj['count'][Dj['class'] == one_class])
            print(count)
            class_count.append(count)
            
    
        info_a +=  sum(Dj['count']) / sum(dataframe['count']) * entropy(class_count)

    return info_a




frame = pd.DataFrame({'attribute': ['31','26','31','21','31','26','41','36','31','46','26'], \
    'count': [30,40,40,20,5,3,3,10,4,4,6], \
        'class':['senior', 'junior','junior','junior', 'senior','junior', 'senior','senior', 'junior','senior', 'junior']})

print(info_a(frame))

print('Gain: ', entropy([113, 52]) - info_a(frame))