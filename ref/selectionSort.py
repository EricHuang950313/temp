def selection_sort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        yield arr  # Yield the array after each swap

# Example usage
arr = [4, 2, 8, 3, 10, 7, 9, 6, 5, 1]
sort_generator = selection_sort(arr)

for step in sort_generator:
    print("Current array state:", step)