#Reverse an array 

#using two pointer approach 
arr = [1,2,3,4]
length  = len(arr) - 1

def reverse(arr, left , right):
    if right <= left:
        print(arr)
        return
    arr[left], arr[right] = arr[right], arr[left]
    reverse(arr, left+1, right-1)

reverse(arr, 0 , length)




