'''

Problem Statement:
A and B went to a candy store, where A picked out candy based on their color and B picked out candy based on their flavor. 
They want to find the median price of all the candies they bought together and approach you to write a python program to perform this 
operation for them using the concept of divide and conquer. Assuming they both buy the same number of candies and report the prices in 
sorted order, find the median price.

If the two do not buy equal number of candies, the function must return -1.

'''

def getMedian(arr1, arr2, n):
    
    if(len(arr1)!=len(arr2)):
        return -1
    else:
        return median_operation(arr1, arr2, n)
        
def median_operation(arr1, arr2, n):
    # check the base case:
    if n==0:
        return 0
    
    elif n==1:
        # just one element case
        return (arr1[0]+arr2[0])/2
        
    else:
        
        # calculate median of individual lists
        median_arr1 =   findMedianArray(arr1)
        median_arr2 =   findMedianArray(arr2)
        
        # if medians equal, return the median
        if median_arr1 == median_arr2:
            return median_arr2
        
        elif median_arr1< median_arr2:
            return median_operation(arr1[n// 2:], arr2[:n // 2+1], n - n // 2)
        
        elif median_arr2< median_arr1:
            return median_operation(arr1[:n // 2+1], arr2[n // 2:], n - n // 2)
        

       
      
       

def findMedianArray(arr):
    
    len_arr = len(arr)
    if len_arr%2==0:
        mid =  len_arr//2
        median = (arr[mid]+arr[mid-1])/2
    else:
        mid = len_arr//2
        median  = arr[mid]
        
    return median
    
  
