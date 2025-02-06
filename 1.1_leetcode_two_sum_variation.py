input = [3, 4, 5, 6]
target = 15
# Output: [0, 2]  # 3 * 5 = 15

empty_dictonary = {}
for index, number in enumerate(input):
    complement = target/number
    if complement in empty_dictonary:
        print([empty_dictonary[complement],index])
    
    empty_dictonary[number] = index
    

