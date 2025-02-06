input = [1, 4, 2, 2, 5, 2]
output = 2 


empty_dictonary = {}
for x in input:
    if x not in empty_dictonary.keys():
        empty_dictonary[x] = 1 
    else:
        empty_dictonary[x] = empty_dictonary[x] + 1

 
empty_dictonary.keys()
duplicate_value = [x for x in empty_dictonary.values() if x > 1][0]

for k,v in empty_dictonary.items():
    if v== duplicate_value:
        key_to_be_found=k





def find_first_duplicate(input_list):
    count_dict = {}

    for x in input_list:
        if x in count_dict:
            return x  # Return the first element that has appeared before
        count_dict[x] = 1  # Otherwise, mark the element as seen

    return None  # If no duplicates are found

# Test
input_list = [1, 4, 2, 2, 5, 2]
result = find_first_duplicate(input_list)
print(result)  # O