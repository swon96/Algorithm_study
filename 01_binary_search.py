def binary_search(list, item):
    low = 0;
    high = len(list)-1;

    while low <= high:
        mid = (low+high)/2;
        if list[mid] == item: return mid;
        if list[mid] < item: low = mid-1;
        if list[mid] > item: high = mid+1;
        else: return None;


my_list = [1,3,5,7,9]

print binary_search(my_list, 5);
print binary_search(my_list, 10);

