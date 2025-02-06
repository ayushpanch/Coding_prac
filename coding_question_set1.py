# l1 = [1,2,3,4,5]
# output = [5,1,2,3,4]


# so if input 1 is given it will take the last index and sort it then 

l1 = [1,2,3,4,5]
movement = 1 

l1[-1:] + l1[:-1]
# movement of list


def udf_movement(movement,l1):

    return l1[-movement:] + l1[:-movement]

restored_list = udf_movement(2,[1,2,3,4,5])

