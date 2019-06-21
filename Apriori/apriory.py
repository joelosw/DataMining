# Assuming the recorded transactions to be in the following format: 
# [[[T-Nrt][Item 1, Item 2, Item 3]],[[T-3689], [1,2,2,3,8,7]]]
#from powerset import potenzmenge
from itertools import combinations, product
from create_transactions import create_transactions
import timeit

def apriori (transactions, min_trashhold, max_iterations):
    ''' The hear function of the Algorithm. This one takes it all together. 
    It sorts and count the Data. 
    It does the first two iterations manually
    and all the other ones in a loop. 
    These allways includes:
        1. Join Operation to form new candidates based on Last Tupels
        2. Prune Cadidates with apriori knowledge
        3. Count candidates
        4. Keep those candidates as frequent itemsets, whose support >= threshhold '''
        
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
    counted2 = count_items2(itemsets, combinations2)
    c.append(counted2)
    f.append({k:v for k,v in c[2].items() if v >= min_trashhold})

    print('F nach Runde 2: ', f)
    iteration = 3
    #while iteration <= max_iterations:
    while c[iteration-1]: 
        combinationX = inner_join(f[iteration-1], iteration-1)
        c.append(count_items2(itemsets, combinationX))
        #not_counted_candidates = pruning(combinationX, f[len(f)-1].values(), iteration)
        #c.append(count_items2(itemsets, not_counted_candidates))
        f.append({k:v for k,v in c[iteration].items() if v >= min_trashhold})
        iteration +=1

        print (f'aktuelle Frequent {iteration-1}-Itemsets: ', f[iteration-1])

    print(f'Finales f  (Größtes Frequent Itemset: {iteration-2}): ', f[iteration-2])

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

def count_items2(itemsets, to_count):
    #print('IM zählen (2), to count: ', to_count)
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


def pruning(combinationX, l_minus_1, current_size):
    for candidate in combinationX:
        for sub_candidates in combinations(candidate, current_size-1):
            if sub_candidates not in l_minus_1:
                combinationX.remove(candidate)
                print('pruned: ', candidate, ' because of: ', sub_candidates )
                break

    return combinationX

def inner_join(counted, current_size):

    c=[]
    for freq_itemset in combinations(counted.keys(),2):
       # print('Häufige Tupel, in Kombination miteinander: ', freq_itemset)
        if (freq_itemset[0][0:current_size-1] == freq_itemset[1][0:current_size-1]):
            # print('Juhu, Kandidat gefunden!: ', freq_itemset)
            s=set(freq_itemset[0])
            s.add(freq_itemset[1][current_size-1])
            c.append(tuple(s))
    
    #print('Übereinstimmende Itemsets: ', c)
    return c
if __name__ == '__main__':
    #apriori([[[1], [1,2,3,4,5]], [[2],[2,3,4,5,6,7,8]], [[3], [7,8,9,10]]], 2,1000)
    start = timeit.default_timer()
    apriori(create_transactions(1500,15,8),3, 8)
    stop= timeit.default_timer()
    print('Time: ', stop - start)


  