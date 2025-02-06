input_list = [4, 2, 5, 3, 3, 1, 2, 4, 1, 5, 5, 5, 3, 1]

# Output: [4, 2, 5, 3, 1]
empty_dictonary = {}
for x in input_list:
    if x not in empty_dictonary.keys():
        empty_dictonary[x] = 1
    else:
        empty_dictonary[x] = empty_dictonary[x] + 1 



list_values =[]
for keys,values in empty_dictonary.items():
        list_values.append(keys)

# solution 2 

input_list = [4, 2, 5, 3, 3, 1, 2, 4, 1, 5, 5, 5, 3, 1]
output_list=[]

for x in input_list:
     if x not in output_list:
          output_list.append(x)
          
     
