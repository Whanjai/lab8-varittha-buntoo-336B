def merge(arr,low,mid,high):
    temp = arr[low:mid+1]
    i = 0
    j = mid + 1
    k = low
    while (i<len(tem)and j <=high):
        if (temp[i] <= arr[j]):
            arr[k] = temp[i]
            i += 1
            k += 1
        else:
            arr[k] = arr[j]
            j += 1 
            k += 1
    while (i<lem(temp)):
        arr[k] = temp[i]
        i += 1
        k += 1
def sort(arr,low,high):
        if (high-low<1):
            return
        mid = low +(high-low)//2
        sort(arr,low,mid)
        sort(arr,mid+1,high)
        merge(arr,low,mid,high)
        return arr
    Array =[29,10,14,37,14,20,7,16,12]
    print(sort(Array,0,len(Array)-1))
