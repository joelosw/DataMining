import math

def entropy(classlabels_with_count):
    """ Expected in Form {c1:count1, c2:count2, ..., ck:countk} """
    total_count = sum(a for a in classlabels_with_count.values())
    info= - sum([p/total_count * math.log2(p /total_count) for p in classlabels_with_count.values()]) 
    print('Needed Exoected Bits: ', info )
    return info 