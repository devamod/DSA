def linear_search(list , target):
    """
    Return the index of the target if found , else return None
    """

    # start at index 0 and iterate over the list 
    for i in range(len(list)):
        # compare every element to the target
        if list[i] == target:
            # if found return the index
            return i
        
    #if element not found return None
    return None 

def verify(index):
    if index is not None:
        print(f"Target found at index: {index}")
    else:
        print("Target not found")

numbers = [1,2,3,4,5,6,7,7,7,8,9]

result = linear_search(numbers , 6)

verify(result)
