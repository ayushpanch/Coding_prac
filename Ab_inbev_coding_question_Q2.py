l1 = [1,2,3,4,5]
l2 = [6,7,3,4,1]


empty_list = []
for x in l1:
    for y in l2:
        if x == y:
            empty_list.append(x)
