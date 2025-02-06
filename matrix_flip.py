input = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]



def flip_diagonal(matrix):
    # Get the number of rows and columns in the matrix
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Create a new matrix with flipped dimensions
    flipped_matrix = [[0] * rows for _ in range(cols)]
    
    # Iterate through the matrix and assign the elements diagonally
    for i in range(rows):
        for j in range(cols):
            flipped_matrix[j][i] = matrix[i][j]
    
    return flipped_matrix

flip_diagonal(input)


#ayush code 
input_ap =  [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]


# check the rows and columns of a dataframe 
rows = len(input_ap)
cols = len(input_ap[0])

empty_matrix = [[0]*3 for _ in range(cols)]

for every_row in range(rows):
    for every_col in range(cols):
        empty_matrix[every_col][every_row] = input_ap[every_row][every_col]

















