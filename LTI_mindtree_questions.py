# common elelemnts between lists 
list_1 = [1,2,3,4,5,6,7,8,9,10]
list_2 =[1,2,3,9,10,100,120,140]

emptylist=[]
for x in list_1:
    for y in list_2:
        if x == y:
            emptylist.append(x)

emptylist

# which are in A but not in b 
a = [1,2,3,4,5,6,7,8,910,11,12,13,14,15,16,17,18,19,20]
b = [2,4,6,8,10]

second_list =[]
for y in b: 
    if y not in a:
        second_list.append(y)

# using zip function create the dictonary 
list_1 = ['a','b','c','d']
list_2 = [1,2,3,4]

dict_created = dict(zip(list_1,list_2))

# using enumerate function create the dictonary 
list_1 = ['a','b','c','d']
list_2 = [1,2,3,4]

dict(enumerate(list_1))
dict(enumerate(list_2))

# element wise addition 
list1 = [1, 2, 3]
list2 = [4, 5, 6]
another_list = [x + y for x,y in list(zip(list1,list2))]
# Output: [5, 7, 9]

# examples for map,filter and reduce 
list(map(lambda every_row: every_row*2,list1) )
list(filter(lambda every_row : every_row%2== 0 ,list2))
# list(reduce(lambda x,y : x+y , list2))


emptylist_1= []
emptylist_2 = []
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
for every_combination in pairs:
    emptylist_1.append(every_combination[0])
    emptylist_2.append(every_combination[1])

# Output: ([1, 2, 3], ['a', 'b', 'c'])

# same with more optimised way
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
number_1,number_2= zip(*pairs)
list(number_1),list(number_2)


# transpose the matrix 
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

number_1,number_2,number_3 = zip(*matrix)
output  = [list(x) for x in zip(*matrix)]



list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
# Output: [4.0, 5.0, 6.0]  (average of corresponding elements)
another_list = [x + y +z for x,y,z in list(zip(list1,list2,list3))]


experiment1 = [
    [1.2, 2.3, 3.4],
    [4.5, 5.6, 6.7]
]
experiment2 = [
    [1.0, 2.5, 3.3],
    [4.6, 5.4, 6.8]
]
# Output: [
#    [1.1, 2.4, 3.35],
#    [4.55, 5.5, 6.75]
# ]

# prime_number(100)
emptylist =[]
import math
def prime_number(number):
    if number<2:
        return False
    for x in range(2,int(math.sqrt(number)) +1 ):
        if number%x == 0:
            return False
    return True


empty_list = [x for x in range(1,101) if prime_number(x)]

# for x in range(2,101)

import math
def prime_number(number):
    if number < 2:
        return False
    for x in range(2, int(math.sqrt(number)) + 1):
        if number % x == 0:
            return False
    return True

# Generate the list of prime numbers
empty_list = [x for x in range(1, 101) if prime_number(x)]
print(empty_list)





















