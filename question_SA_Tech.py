
#Question 1 
list_1 = [1,2,3,4,5,6]

# find the second largest number 
min_num = 0
for x in list_1:
    if x > min_num:
        min_num =x

second_num = 0
for x in list_1:
    if ((x > second_num) & ( x < min_num)):
        second_num = x 

print(f"the min number is - {min_num}")
print(f"the second number is - {second_num}")

#Q2 find the second largest number but if occurence is 2  then give the third most number 
list_1 = [1,2,3,4,5,5,6]

# find the second largest number 
min_num = 0
for x in list_1:
    if x > min_num:
        min_num =x
dictonary_to_find ={}
for x in list_1:
    if x not in dictonary_to_find:
        dictonary_to_find[x] = 1
    else:
        dictonary_to_find[x] = dictonary_to_find[x] + 1


second_num = 0
for x in list_1:
    if ((x > second_num) & ( x < min_num) &(dictonary_to_find[x]> 1 ) ):
        break
        
    elif ((x > second_num) & ( x < min_num) ):
        second_num = x 


print(f"the min number is - {min_num}")
print(f"the second number is - {second_num}")




string_1 = "abcsdddgmaofaknsmfuaf"
empty_dictonary = {}
for x in string_1:
    if x not in empty_dictonary:
        empty_dictonary[x] = 1
    else:
        empty_dictonary[x] = empty_dictonary[x] + 1

empty_dictonary

sorted(empty_dictonary.items(),key= lambda every_row : every_row[1],reverse= True)

empty_list =[]
for key , values in empty_dictonary.items():
    if 3 ==  values:
        empty_list.append(key)

sorted(empty_list,reverse= True)

# empty_list_2 = []
# for key,vaues in empty_dictonary:
#     empty_list_2.append(values)


# Sample dictionary
empty_dictionary = {'a': 4, 'b': 1, 'c': 1, 's': 2, 'd': 3, 'g': 1, 'm': 2, 'o': 1, 'f': 3, 'k': 1, 'n': 1, 'u': 1}

# Convert the dictionary into a list of tuples (key, value)
items = list(empty_dictionary.items())

# Bubble sort based on the values
n = len(items)
for i in range(n):
    print(f"i is ------ {i}")
    for j in range(0, n-i-1):
        print(f"n-i-1 is ------------ {n-i-1} ")
        # If the current value is greater than the next one, swap them
        if items[j][1] > items[j+1][1]:
            items[j], items[j+1] = items[j+1], items[j]

# Create a new sorted dictionary from the sorted list of tuples
sorted_dict = dict(items)

# Print the sorted dictionary
print(sorted_dict)






