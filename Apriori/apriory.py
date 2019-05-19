# Assuming the recorded transactions to be in the following format: 
# [[[T-Nrt][Item 1, Item 2, Item 3]],[[T-3689], [1,2,2,3,8,7]]]
#from powerset import potenzmenge
from itertools import combinations, product
from create_transactions import create_transactions

def apriori (transactions, min_trashhold, max_iterations):
    itemsets = [a[1] for a in transactions]
    c=[0]
    print(max(max(itemsets)))
    candidates= [a for a in range(0, max(max(itemsets))+1)]
    print(candidates)
    c.append(count_items(itemsets, 1))
    f=[0]
    f.append({k:v for k,v in c[1].items() if v >= min_trashhold})
    #for ind, candidates in enumerate(f):
  
    combinations2 = inner_join(f[1], 1)
    #print('zweiwertige Kombinationen: ', combinations2)
    counted2 = count_items2(itemsets, combinations2,2)
    c.append(counted2)
    f.append({k:v for k,v in c[2].items() if v >= min_trashhold})

    print('F nach Runde 2: ', f)
    iteration = 3
    while iteration <= max_iterations:
        combinationX = inner_join(f[iteration-1], iteration-1)
        c.append(count_items2(itemsets, combinationX, 250))
        f.append({k:v for k,v in c[iteration].items() if v >= min_trashhold})
        iteration +=1

    print('Finales f: ', f[max_iterations])

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

def count_items2(itemsets, to_count, size):
    print('IM zählen (2), to count: ', to_count)
    #itemsets = [set(a) for a in itemsets]
    #to_count = [set(b) for b in to_count]
    counted = dict()
    for counting in to_count:
        for itemset in itemsets:
            #itemset.sort()
            if set(counting) <= set(itemset):
                if counting not in counted.keys():
                    counted[counting] = 1
                else:
                    counted[counting] += 1
        
    return {tuple(k):v for k,v in counted.items() }

def inner_join(counted, current_size):
    c=[]
    for freq_itemset in combinations(counted.keys(),2):
       # print('Häufige Tupel, in Kombination miteinander: ', freq_itemset)
        if (freq_itemset[0][0:current_size-1] == freq_itemset[1][0:current_size-1]):
            # print('Juhu, Kandidat gefunden!: ', freq_itemset)
            s=set(freq_itemset[0])
            s.add(freq_itemset[1][current_size-1])
            c.append(tuple(s))
    
    print('Übereinstimmende Itemsets: ', c)
    return c


if __name__ == '__main__':
    #apriori([[[1], [1,2,3,4,5]], [[2],[2,3,4,5,6,7,8]], [[3], [7,8,9,10]]], 2,1000)
    apriori(create_transactions(2500,17,12),3, 7)

  