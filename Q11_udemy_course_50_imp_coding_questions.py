input =  [1, 3, 4, 7, 8]

empty_location = []
for location in range(1,len(input) -1 ,1):
    print(input[location])
    if ((input[location] >= (input[location -1] )) &  (input[location] >= (input[location +1]) ) ):
        empty_location.append(input[location])
    else:
        pass

if len(empty_location) == 0:
    empty_location.append(input[-1])
