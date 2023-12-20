def binary_search(list , target):
    
    #find the middle element of the list
    first = 0
    last = len(list) - 1
    
    while first <= last:
        mid = (first + last)//2
        mid_element = list[mid]
        # if it matches target return middle position
        if target == mid_element:
            return mid

        # if target is less than the middle element search the left part of the list
        elif target < mid_element:
            last = mid-1

        # if target is greater than the middle element search the right part of the list
        elif target > mid_element:
            first = mid+1

    # if no more elements remain return None.
    return None        
    
def verify(index):
    if index is not None:
        print(f"Target found at index: {index}")
    else:
        print("Target not found")

numbers = [1,2,3,4,5,6,8,9]

result = binary_search(numbers , 8)
verify(result)