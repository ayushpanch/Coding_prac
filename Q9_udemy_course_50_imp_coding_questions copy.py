# input = "abcdbeghef"
input = "eddy"

empty_list =[] 
for x in range(len(input)):
    for y in range(len(input),0,-1):
        string_1 = input[x:y]
        if len(string_1) > 1:
            empty_list.append(string_1)

final_list = []
empty_dictonary = {}    
for every_input in empty_list:
    indiidual_letters_list = list(every_input)
    for x in indiidual_letters_list:
        if x not in empty_dictonary:
            empty_dictonary[x] = 1
        else:
            empty_dictonary[x] = empty_dictonary[x] + 1 
    
    element = sorted(empty_dictonary.items(), key = lambda x : x[1], reverse = True)[0][1]
    key = sorted(empty_dictonary.items(), key = lambda x : x[1], reverse = True)[0] 
    if element <2:
        final_list.append((every_input,len(every_input)))
        empty_dictonary.clear()
    else:
        empty_dictonary.clear()

max_number = 0
for everytuple in final_list:
    if everytuple[1] >max_number:
        max_number = everytuple[1]

for everytuple in final_list:
    if everytuple[1]  == max_number:
        final_answer = everytuple[0]
        



# chatgpt solution 
def longest_unique_substring_length(s):
    # Set to store the unique characters in the current window
    char_set = set()
    
    left = 0  # Left pointer for the sliding window
    max_length = 0  # Variable to track the maximum length of substring
    
    # Iterate over the string with the right pointer
    for right in range(len(s)):
        # If the character at 'right' is already in the set, shrink the window
        while s[right] in char_set:
            char_set.remove(s[left])  # Remove the character at 'left' from the set
            left += 1  # Move the left pointer to the right to shrink the window
        
        # Add the current character to the set
        char_set.add(s[right])
        
        # Update the max_length with the size of the current window
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Example usage:
str_input = "abcdbeghef"
print(longest_unique_substring_length(str_input))




