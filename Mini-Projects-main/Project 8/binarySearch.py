# divide and conquer algorithm to search an element in a faster way
# list of ordered elements are present and then divide the list into two parts based on the condition
# if element > mid element then low = mid+1,high= high
# if < then high = mid - 1
# if = then it is the element
# reccursive process
# binary search is better than navie search which scans entire list
import random
import time
def navie_search(l, target):
    for i in range(len(l)):
        if l[i] == target :
            return i
    return -1

# binary search
def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1  
    
    if high < low:
        return -1
    # l= [1, 3, 5, 10, 20]
    midpoint = (low+high) // 2

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint] :
        return binary_search(l, target, low, midpoint-1)
    else:
        return binary_search(l, target, midpoint+1, high)

if __name__=='__main__':
    # l = [2,3,4,5,10,12]
    # target = 10
    # print(navie_search(l, target))
    # print(binary_search(l, target))

    length = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    # to get the time take by navie search
    start = time.time()
    for target in sorted_list:
        navie_search(sorted_list, target)
    end = time.time()
    print("Navie serach time: ", (end - start)/length,"seconds")
    x= (end - start)/length
    # to get the time taken by binary search
    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary serach time: ", (end - start)/length,"seconds")
    y = (end - start)/length
    if x>y:
        print("NS takes more time")
    else:
        print("BS takes more time")