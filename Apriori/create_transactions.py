import random

def create_transactions(length, max_item, max_size_of_itemset):
    transactions=[]
    for i in range(1, length+1):
        tran=[]
        tran.append([i])
        tran.append([random.randint(1, max_item) for a in range(random.randint(1,max_size_of_itemset))])

        transactions.append(tran)
    print('Test Transactions created')
    return transactions