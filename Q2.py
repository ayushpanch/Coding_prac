"""convert the list into list of list"""

input = ['abc','def','ghi']
output_should_be  =[['a','b','c'],['d','e','f'],['g','h','i']] 

empty_list=[]
for x in range(len(input)):
    empty_list.append(list(input[x]))

empty_list