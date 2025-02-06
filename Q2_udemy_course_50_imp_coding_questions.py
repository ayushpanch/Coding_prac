input_str =  "programming"

empty_dictonary = {}
for x in input_str:
    if x not in empty_dictonary.keys():
        empty_dictonary[x] = 1
    else:
        empty_dictonary[x] = empty_dictonary[x] + 1 



list_values =[]
for keys,values in empty_dictonary.items():
    if empty_dictonary[keys]>1:
        list_values.append(keys)

list_values[0]
