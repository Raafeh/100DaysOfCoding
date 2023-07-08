def find_subarray_sum(arr, target_sum):
    left = 0
    current_sum = 0
    subarray_found = False

    for right in range(len(arr)):
        current_sum += arr[right]

        while current_sum > target_sum:
            current_sum -= arr[left]
            left += 1

        if current_sum == target_sum:
            subarray_found = True
            break

    if subarray_found:
        return [left + 1, right + 1]  # Adjusting indexes to 1-based indexing
    else:
        return print("No subarray found with the given sum")

# Example usage
arr = [ 1, 2, 3, 7, 5]
target_sum = 8
result = find_subarray_sum(arr, target_sum)
print(result)
