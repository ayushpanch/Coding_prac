input = [2, 3, -6, 4, 2, -8, 3]

def max_subarray_sum(arr):
    # Initialize variables to track the maximum sum and current subarray sum
    max_sum = arr[0]
    current_sum = arr[0]

    # Iterate over the array starting from the second element
    for i in range(1, len(arr)):
        # Update the current subarray sum, either extend or start new from arr[i]
        print(f"the i is ------------- {i}")
        print("------------------------------------------------------------")
        print(f"the arr[i] is -------- {arr[i]}")
        print(f"the current_sum is -------- {current_sum}")
        print(f"the another component is  -------- {current_sum + arr[i]}")

        current_sum = max(arr[i], current_sum + arr[i])
        print(f"the current sum is  -------- {current_sum }")


        # Update the maximum sum encountered so far
        max_sum = max(max_sum, current_sum)
        print(f"the maximum sum is  -------- {max_sum }")


    return max_sum

# Test case
arr = [2, 3, -6, 4, 2, -8, 3]
result = max_subarray_sum(arr)
print(result)  # Output: 6

