# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

input =[2,7,11,15]
target = 9 


emptylist = []
for x in range(len(input)):
    print(x)
    for y in range(len(input)):
        print(y)
        if x!=y:
            if input[x] + input[y] == target:
                emptylist.append((x,y))

list(emptylist[0])


# move the zero towards left
input =[1,2,3,4,0,0,12,14,56]
left_position = 0
for x in range(len(input)):
    if input[x]!= 0:
        input[left_position],input[x] = input[x],input[left_position] 
        left_position = left_position +1


# another solution ( with time complexity = 0(n) ) 
def two_sum(nums, target):
    # Create a dictionary to store the number and its index
    num_to_index = {}
    
        # Iterate over the array
    for index, number in enumerate(nums):
        # Calculate the complement needed to reach the target
        complement = target - number
        
        # Check if the complement is already in the dictionary
        if complement in num_to_index:
            return [num_to_index[complement], index]  # Return the indices
        
        # Store the index of the current number
        num_to_index[number] = index

    # If no solution is found (though the problem states there is one)
    return None

# Example usage
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)  # Output: [0, 1]



#ayush code 
input = [3,2,4]
target = 6
emptylist = []
empty_dictonary = {}
for index, number in enumerate(input):

    complement = target - number

    if complement in empty_dictonary:
        print([empty_dictonary[complement],index])
        
    
    empty_dictonary[number] = index








