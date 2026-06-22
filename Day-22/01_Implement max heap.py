# Max-Heap implementation: ---------------


# start from up and go down heapifying elem - used for building heap or deletion

def heapify_down_max(arr, n, i):
    largest = i
    left = (2*i)+1
    right = (2*i)+2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify_down_max(arr, n, largest)


def build_max_heap(arr):
    # last non-leaf node = (n//2)-1. we traverse from last non-leaf towards 0 and heapify all elem to follow the property of heap

    n = len(arr)
    last_non_leaf = (n//2)-1
    for i in range(last_non_leaf, -1, -1):
        heapify_down_max(arr, n, i)


# get the max elem from heap ------------------------
def extract_max(arr):

    if not arr:
        return None

    max_elem = arr[0]
    # deleting by swaping value so that the structue must be preserved and complete
    arr[0], arr[-1] = arr[-1], arr[0]
    arr.pop()
    heapify_down_max(arr, len(arr), 0)

    return max_elem


def heapify_up_max(arr, i):
    parent = (i-1)//2

    if i>0 and arr[parent] < arr[i]:
        arr[parent], arr[i] = arr[i], arr[parent]
        heapify_up_max(arr,parent)


def insert_max(arr, k):
    arr.append(k)
    heapify_up_max(arr,len(arr)-1)


def peek_max(arr):
    if not arr:
        return None
    
    return arr[0]


def max_heap_run():
    # Binary Tree Representation
    # of input array
    #             3
    #           /    \
    #         1       6
    #       /  \     /  
    #     5     2   4  
   
    arr = [3,1,6,5,2,4]

    build_max_heap(arr)

    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

    # 6 5 4 1 2 3 
    # Final Heap:
    #             6
    #           /    \
    #         5       4
    #       /  \     /  
    #      1     2   3


    # insert testing -------
    insert_max(arr,7)

    # build_maxheap(arr)

    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


    # extract max 
    print(extract_max(arr))


    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


    # Outputs:
    # 6 5 4 1 2 3 
    # 7 5 6 1 2 3 4
    # 7
    # 6 5 4 1 2 3

