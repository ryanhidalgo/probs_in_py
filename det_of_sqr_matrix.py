#https://edabit.com/challenge/NY9KKZezoKXrQNFEJ
#for any size square matrix, calculate the determinant

#input
#size argument(s)
#Example
#4 4 3 2 2 0 1 -3 3 0 -1 3 3 0 3 1 1
#Generates the 4x4 matrix
#[4, 3, 2, 2]
#[0, 1, -3, 3]
#[0, -1, 3, 3]
#[0, 3, 1, 1]
#with determiant -240

import sys

class Matrix():
    def __init__(self, matrix):
        self.matrix = matrix
        
    def __str__(self):
        return_string = ""
        for r_index, row in enumerate(self.matrix):
            return_string= return_string + str(self.matrix[r_index]) + "\n"
        return return_string
            
    def __getitem__(self, row):
        return self.matrix[row]
            
class Square_Matrix(Matrix):
    def __init__(self, matrix):
        self.size = len(matrix)
        super().__init__(matrix)

    def find_determinant(matrix):
        #handles case of 1x1 matrix
        if (matrix.size == 1):
            return matrix[0][0]
        #base case of 2x2 matrix
        #|a b|
        #|c d|
        if (matrix.size == 2):
            #ad-bc = determinant
            ad = matrix[0][0] * matrix[1][1]
            bc = matrix[0][1] * matrix[1][0]
            return ad - bc
        else:
            #list of element, cofactor products
            det = []
            #sample 3x3 matrix
            #|a b c|
            #|d e f|
            #|g h i|
            #for the first pass we want:
            #       |e f|
            #a * det|h i|
            #second would be:
            #       |d f|
            #b * det|g i|
            #after the third pass, we calculate the determinant with:
            #     |e f|        |d f|        |d e|
            #a*det|h i| - b*det|g i| + c*det|g h|
            for c_index, column in enumerate(matrix[0]):
                #take top value of column and multiply by 
                #cofactor (determinant of submatrix).
                #Submatrix is the n-1 x n-1 size matrix
                #which includes all elements not in the current
                #column
                
                #generate submatrix
                sub_matrix = []
                for r_index, row in enumerate(matrix):
                    if (r_index == 0):
                        pass
                    else:
                        next_row = []
                        
                        if (c_index == 0):
                            column_index = 1
                        else:
                            column_index = 0
                            
                        while (column_index < matrix.size):
                            if (column_index == c_index):
                                pass
                            else:
                                next_row.append(matrix[r_index][column_index])
                            column_index += 1
                        sub_matrix.append(next_row)
                
                #element times cofactor
                det.append(matrix[0][c_index] * Square_Matrix.find_determinant(Square_Matrix(sub_matrix)))
            total = 0
            for index, determinant in enumerate(det):
                if (index % 2 != 0):
                    total -= determinant
                else:
                    total += determinant
            return total

size = int(sys.argv[1])
argv_index = 2
while (argv_index < len(sys.argv)):
    temp_matrix = []
    row_counter = 0
    while (row_counter < size):
        temp_row = []
        column_counter = 0
        while (column_counter < size):
            temp_row.append(int(sys.argv[argv_index]))
            argv_index += 1
            column_counter += 1
        row_counter += 1
        temp_matrix.append(temp_row)
    argv_index += 1
        
my_matrix = Square_Matrix(temp_matrix)
print(my_matrix)
print(Square_Matrix.find_determinant(my_matrix))
