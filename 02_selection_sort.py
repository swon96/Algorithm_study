def smallElement(arr):
    smallest = arr[0]
    returnElement = 0
    for i in range(1, len(arr)):
        if smallest > arr[i]:
            smallest = arr[i]
            returnElement = i
    return returnElement


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        small_element = smallElement(arr)
        newArr.append(arr.pop(small_element))
    return newArr


print selectionSort([5, 4, 3, 2, 1])

