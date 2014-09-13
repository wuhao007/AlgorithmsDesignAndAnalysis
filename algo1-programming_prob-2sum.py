'''
Programming assignment 6.1:

implement the 2-SUM algorithm,
that for given list of integers
and number t finds whether there are
two distinct integers x and y
in the list such that x+y = t.

Implementation alternatives:
* Naive method - O(n^2)
* Via binary search - O(n*log(n))
* Via hash table - O(n)
'''

import sys
import threading

def TwoSum_Naive(lst, target):
    '''
    Naive 2-SUM algorithm.
    
    O(n^2) time.
    '''
    
    for x in lst:
        for y in lst:
            if x != y and x+y == target:
                return (x, y)
            
    return None


def binarySearch(lst, x):
    
    def _binarySearch(lst, i, j, x):
        if i > j:
            return None
        m = (i + j)/2
        if x < lst[m]:
            return _binarySearch(lst, i, m-1, x)
        elif x > lst[m]:
            return _binarySearch(lst, m+1, j, x)
        else: # x == lst[m]
            return i
    
    return _binarySearch(lst, 0, len(lst)-1, x)


def TwoSum_BinarySearch(lst, target):
    '''
    2-SUM algorithm via binary search.
    Expects lst to be sorted.
    
    O(n*log(n)) time.
    '''
    
    for x in lst:
        y = target-x
        i = binarySearch(lst, y)
        if i and x != y:
            return (x, y)
        
    return None


def TwoSum_HashTable(lst, target):
    '''
    2-SUM algorithm via hash table.
    
    O(n) time.
    '''
    
    for x in lst:
        y = target-x
        if y in lst and x != y:
            return (x, y)
        
    return None


def main():
    
    data = map(lambda x: int(x), open('algo1-programming_prob-2sum.txt').readlines())

    #count = 0
    #for t in range(2500, 4000+1):
    #    if(TwoSum_Naive(data, t)):
    #        count += 1
    #print('Naive:' + str(count))
    
    #count = 0
    #sorted_data = sorted(data)
    #for t in range(2500, 4000+1):
    #    if(TwoSum_BinarySearch(sorted_data, t)):
    #        count += 1
    #print('Via binary search: ' + str(count))
    
    count = 0
    data_set = set(data)
    for t in range(-10000, 10001):
        if(TwoSum_HashTable(data_set, t)):
            count += 1
    print('Via hash table: ' + str(count))
    

if __name__ == '__main__':
    threading.stack_size(67108864) # 64MB stack
    sys.setrecursionlimit(2 ** 20)  # approx 1 million recursions
    thread = threading.Thread(target = main) # instantiate thread object
    thread.start() # run program at target
    
