# Assuming the recorded transactions to be in the following format: 
# [[[T-Nrt][Item 1, Item 2, Item 3]],[[T-3689], [1,2,2,3,8,7]]]

def apriori (transactions, min_trashhold):
    c1 = count_items([a[1] for a in transactions]) 

    f1 = {k:v for k,v in c1.items() if v >= min_trashhold}
    print ('Erhalte: ', c1, f1)

def count_items(itemsets):
    counted = dict()

    for itemset in itemsets:
        itemset.sort()
        for item in itemset:
            if item not in counted.keys():
                counted[(item)] = 1
            else:
                 counted[(item)] += 1
    
    return counted





if __name__ == '__main__':
    apriori([[[1], [1,2,3,4,5]], [[2],[2,3,4,5,6,7,8]], [[3], [7,8,9,10]]], 2)

