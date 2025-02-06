summary_dictonary = {"A" : 1 , "B": 2 , "C" : 3 , "D" : 4 , "E" : 5}

dict(sorted(summary_dictonary.items(), key= lambda every_row : every_row[1] , reverse= True))   

# Iterate over the items in the dictionary and swap key-value pairs
for key in summary_dictonary:
    print(f"the key is ------ {key}")
    max_key = key
    for other_key in summary_dictonary:
        print(f"the other key is ------- {other_key}")
        if summary_dictonary[other_key] > summary_dictonary[max_key]:
            print(f"the summary_dictonary[other_key] is ---- {summary_dictonary[other_key]}")
            print(f"summary_dictonary[max_key] is ---- {summary_dictonary[max_key]}")

            max_key = other_key
            print(f"the max key is ---- {max_key}" )
    
    # Swap the positions of the current key and the key with the maximum value
    summary_dictonary[key], summary_dictonary[max_key] = summary_dictonary[max_key],summary_dictonary[key]


summary_dictonary

