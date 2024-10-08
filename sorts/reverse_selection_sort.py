def reverse_selection_sort(arr):
    n = len(arr)
    for i in range(n):
        max_index = i

        # Find the maximum element in the remaining unsorted array

        for j in range(i + 1, n):
            if arr[j] > arr[max_index]:
                max_index = j

        # Swap the found maximum element with the first element

        arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr

# Example : 
arr = [64, 25, 12, 22, 11]
sorted_arr = reverse_selection_sort(arr)
print("Sorted array in descending order:", sorted_arr)
