def lomuto(arr,low,high):
    if (low >= high):
        return
    pivot = arr[high]
    j = low
    for i in range(low,high):
        if (arr[i] <= pivot):
            arr[i],arr[j] = arr[j],arr[i]
            j += 1
    arr[high],arr[j] = arr[j],arr[high] 
    
    lomuto(arr,low,j-1)
    lomuto(arr,j+1,high)
    return arr
Array_A = [29,10,14,37,14,20,7,16,12]
print(lomuto(Array_A,0,len(Array_A)-1))
