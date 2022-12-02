def quick_sort(sequence):
    lengeth = len(sequence)
    if lngth <= 1:
        return sequence
    else:
        pivot = seqeunce.pop()
    items_greater = []
    items_lower =[]
    for items in sequence:
    if items > pivot:
        items_greater.appen(item)
    else:
        items_lower.append(item)
        return quick_sort(items_lower)+[pivot]+quick_sort(items_greater)
    print (quick_sort(29,10,14,37,14,20,7,16,12))
