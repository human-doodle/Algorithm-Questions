'''

Quick sort

Average and best-case complexity is O(n*logn)
Space complexity is O(logn)

'''


def quicksort(nums: list[int]):

    def __partition(  low: int, high: int):
        # nums: array 
        # low, high: index

        # select pivot as the last element
        pivot = nums[high]

        # i: index (takes index of elements less than the pivot element)
        i = low

        # iterate through the array and compare with the pivot element, the element at j 
        for j in range(low, high):
            # if the element at position j is less than the pivot, swap it with ith element and increament i
            if nums[j]<pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1

        # place the pivot element at it's correct position
        nums[i], nums[high] = nums[high], nums[i]
        
        # return the index of the pivot element 
        return i


    
    def __quicksort( low, high):

        if(low<high):

            # get the pivot index from partition
            pivot = __partition( low, high)
            
            # recurse and sort array through divide and  conquer to sort
            __quicksort( low, pivot-1)
            __quicksort( pivot+1, high)

    __quicksort( low = 0, high = len(nums)-1)
    return nums


# test
nums = [5, 4, 3, 2, 1]
print(quicksort(nums))
    
nums = [3, 4, 2, 1]
print(quicksort(nums))




