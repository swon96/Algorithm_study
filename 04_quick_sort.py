def quickSort(arr):
    if(len(arr)<2):
        return arr
    else:
        pivot = arr[0]
        lower. larger = []
        for i in arr[1:]:
            if i < pivot:
                lower.append(i)
            else:
                larger.append(i)
        return quickSort(lower) + [pivot] + quickSort(larger)
print(quickSort([4,2,5,3,1]))