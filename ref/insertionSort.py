def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        yield arr  # Yield the array after each insertion

# Example usage
arr = [4, 2, 8, 3, 10, 7, 9, 6, 5, 1]
sort_generator = insertion_sort(arr)

for step in sort_generator:
    print("Current array state:", step)