input = [4, 5, 1, -3, 6]
k = 11
empty_list =[]
for x in input:
    for y in input:
        if x != y:

            sum_of_x_y = x+y 
            if sum_of_x_y == k:
                print("true")
                empty_list.append((x,y))
                break

