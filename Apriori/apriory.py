# Assuming the recorded transactions to be in the following format: 
# [[[T-Nrt][Item 1, Item 2, Item 3]],[[T-3689], [1,2,2,3,8,7]]]
#from powerset import potenzmenge
from itertools import combinations, product
from create_transactions import create_transactions

def apriori (transactions, min_trashhold, max_iterations):
    c=[0]
    c.append(count_items([a[1] for a in transactions], 4))
    f=[0]
    f.append({k:v for k,v in c[1].items() if v >= min_trashhold})
    #for ind, candidates in enumerate(f):
    print(c, '\n', f)
    
    iteration = 1

    inner_join(transactions, f[1], 4)
    



def count_items(itemsets, size):
    counted = dict()

    for itemset in itemsets:
        itemset.sort()
        for item in combinations(itemset, size):
            if item not in counted.keys():
                counted[(item)] = 1
            else:
                 counted[(item)] += 1
    
    return counted



def inner_join(itemsets, counted, current_size):
    c=[]
    for freq_itemset in combinations(counted.keys(),2):
       # print('Häufige Tupel, in Kombination miteinander: ', freq_itemset)
        if (freq_itemset[0][0:current_size-1] == freq_itemset[1][0:current_size-1]):
            # print('Juhu, Kandidat gefunden!: ', freq_itemset)
            s=set(freq_itemset[0])
            s.add(freq_itemset[1][current_size-1])
            c.append(tuple(s))
    
    print('Übereinstimmende Itemsets: ', c)


if __name__ == '__main__':
    #apriori([[[1], [1,2,3,4,5]], [[2],[2,3,4,5,6,7,8]], [[3], [7,8,9,10]]], 2,1000)
    apriori(create_transactions(200,10,10),3, 15)

  