input =  [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]

empty_dictonary = {}

for every_number in input:
    if every_number in empty_dictonary:
        empty_dictonary[every_number] = empty_dictonary[every_number]  + 1
    else:
        empty_dictonary[every_number] =1 
empty_dictonary 