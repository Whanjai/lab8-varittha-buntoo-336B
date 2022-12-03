def hoarse(arr,low,high):
    if (low >= high):
        return
    pivot = arr[high]
    i = low
    j = high
    while(i<j):
        while(arr[i]<pivot):
            i += 1
        while (arr[j] > pivot):
            j -= 1
        if (i<j):
            arr[i],arr[j]=arr[j],arr[i]
            i += 1
    hoarse(arr,low,i-1)
    hoarse(arr,i,high)
    return arr
    
Array_A = [29,10,14,37,14,20,7,16,12]
print(hoarse(Array_A,0,len(Array_A)-1))
