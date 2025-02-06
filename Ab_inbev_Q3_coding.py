# l1 = [1,2,3,4,5]
# output = [5,1,2,3,4]


# empty_list = l1.copy()
# for x in range(len(empty_list)):
#     # print(x)
#     empty_list.append(None)    

# empty_list = empty_list[5:]

# for x in l1:
#     print(x)
#     empty_list[x+1] = l1[x]
#     print(empty_list)


def rotate_list(input_list, movement):
    # Calculate the effective movement by taking the remainder to handle movement > len(input_list)
    effective_movement = movement % len(input_list)
    # Perform rotation
    rotated_list = input_list[-effective_movement:] + input_list[:-effective_movement]
    return rotated_list

# Example usage
input_list = [1, 2, 3, 4, 5]
movement = 4
output_list = rotate_list(input_list, movement)
print(output_list) 