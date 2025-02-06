"""find the largest number in list without sorting"""

input = [1,2,3,44,512,66,7,8,9,10]

max_number =input[0]
for every_number in input:
    print(f"the every number is ------ {every_number}")
    if every_number > max_number:
        max_number = every_number
        print(f"the new max number is --- {max_number}")
    else:
        pass

print(f"the max number is {max_number}")