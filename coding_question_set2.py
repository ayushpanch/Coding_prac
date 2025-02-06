summary_dictonary = {"A" : 1 , "B": 2 ,  "CH" : 900000, "C" : 3 , "D" : 4 , "E" : 5 , "GH" : 1000}

# find the max key value pair without sorting 
list_to_store_values =[]
for key,value in summary_dictonary.items():
    print(f"the key is ------ {key}")
    print(f"the value is -------- {value}")
    list_to_store_values.append(value)
    

max_number = 0 
for x in list_to_store_values:
    if x > max_number:
        max_number = x 

max_number   

summary_dictonary   

key_to_be_found = 0
for key,value in summary_dictonary.items():
    print(f"the key is ------ {key}")
    print(f"the value is -------- {value}")

    if max_number == value:
        key_to_be_found = key
        break


key_to_be_found

