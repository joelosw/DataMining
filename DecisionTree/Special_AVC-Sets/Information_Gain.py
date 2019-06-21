import math
import pandas as pd
import operator
def entropy(class_label_count_list):
    """ Expected in Form [count1, count 2,...] """
    total_count = sum(a for a in class_label_count_list)
    if 0 in class_label_count_list:
        return 0
    info= - sum([p/total_count * math.log2(p /total_count) for p in class_label_count_list]) 
    print('Needed Expected Bits: ', info )
    return info 

def info_a(dataframe):
    ''' Expects Dataframe with columns "attribute", "class" '''
     
    distinct_values = []
    for value in dataframe["attribute"]:
        if value not in distinct_values:
            distinct_values.append(value)

    class_labels = []
    for value in dataframe["class"]:
        if value not in class_labels:
            class_labels.append(value)

    info_a = 0

       
    for j in distinct_values:
        Dj = dataframe[dataframe["attribute"] == j]

        class_count=[]
        for one_class in class_labels:
            counted_class = Dj['class'].count(one_class)
            class_count.append(counted_class)
            
    
        info_a +=  len(Dj['attribute']) / len(dataframe['attribute']) * entropy(class_count)

    return info_a


     


def info_a_counted(dataframe):

    ''' Expects Dataframe with columns "attribute", "count", "class" '''

    distinct = []
    for value in dataframe["attribute"]:
        if value not in distinct:
            distinct.append(value)

    class_labels = []
    for value in dataframe["class"]:
        if value not in class_labels:
            class_labels.append(value)


    info_a = 0 
    
    for j in distinct:
        Dj = dataframe[dataframe["attribute"] == j]

        class_count=[]
        for one_class in class_labels:
            count = sum(Dj['count'][Dj['class'] == one_class])
            class_count.append(count)
            
    
        info_a +=  sum(Dj['count']) / sum(dataframe['count']) * entropy(class_count)

    return info_a



def get_splitting_attribute_counted(complete_dataframe):
    ''' Expects Dataframe with attributes with one attribute named "counted" and one "class" '''
    
    gain = dict()
    for col in complete_dataframe.columns:
        if col == 'class' or col == 'count':
            continue
        attribute = complete_dataframe[col]
        count = complete_dataframe['count']
        class_labels  = complete_dataframe['class'] 
        gain[col] = entropy(count_class_labels_counted(class_labels, count)) - info_a_counted(pd.DataFrame({'attribute': attribute, 'count': count, 'class': class_labels})) 
    print('Gain-Liste: ', gain)
    return max(gain.items(), key=operator.itemgetter(1))[0]

def get_splitting_attribute(complete_dataframe):
    ''' Expects Dataframe with attributes with one attribute named "class" '''
    
    gain = dict()
    for col in complete_dataframe.columns:
        if col == 'class' :
            continue
        attribute = complete_dataframe[col]
        class_labels = count = complete_dataframe['class'] 
        gain[col] = entropy(count_class_labels(complete_dataframe['class'])) - info_a_counted(pd.DataFrame({'attribute': attribute, 'class': class_labels}))
    print('Gain-Liste: ', gain)
    return max(gain.items(), key=operator.itemgetter(1))[0]


def count_class_labels(label_array):
    
    class_labels = []
    for value in label_array:
        if value not in class_labels:
            class_labels.append(value)

    class_count=[]
    for one_class in class_labels:
        count = label_array.count(one_class)
        
        class_count.append(count)
    return class_count

def count_class_labels_counted(label_array, count_array):
    
    class_labels = []
    for value in label_array:
        if value not in class_labels:
            class_labels.append(value)

    class_count=[]
    for one_class in class_labels:
        count = sum(count_array[label_array == one_class])
        class_count.append(count)
    return class_count
            
    



frame = pd.DataFrame({'age': ['31','26','31','21','31','26','41','36','31','46','26'], \
        'department' : ['sales','sales','sales','systems','systems','systems','systems', 'marketing', 'marketing', 'secretary', 'secretary'], \
        'salary': [46,26,31,46,66,46,66,46,41,36,26], \
        'count': [30,40,40,20,5,3,3,10,4,4,6], \
        'class':['senior', 'junior','junior','junior', 'senior','junior', 'senior','senior', 'junior','senior', 'junior']})

#print(info_a_counted(frame))

print('Bestes Splitting Criterion: ', get_splitting_attribute_counted(frame))