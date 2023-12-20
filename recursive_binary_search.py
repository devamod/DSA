def binary_search(list , target):

    # define base case
    if len(list) == 0:
        return False 
    else:
        midpoint = (len(list))//2

    # if target is equal to mid element return mid position
    if target == list[midpoint]:
        return True
    else:
        # if target is less than the midpoint splice the right half of the list
        if target < list[midpoint]:
            return binary_search(list[:midpoint] , target)
        # if target is greater than the midpoint splice the left half of the list
        else:
            return binary_search(list[midpoint+1:] , target)

numbers = [1,2,3,4,5,6,7,8,9]

result = binary_search(numbers , 12)
print(result)