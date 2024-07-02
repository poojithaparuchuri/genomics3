"""
Problem set 4
Sree Poojitha
upgma.py
"""

# given distance matrix and species list
distanceMatrix = [[0, 12, 12, 13, 15, 15],
                  [12, 0, 2, 6, 8, 8],
                  [12, 2, 0, 6, 9, 9],
                  [13, 6, 6, 0, 8, 8],
                  [15, 8, 9, 8, 0, 4],
                  [15, 8, 9, 8, 4, 0]]
speciesList = ["M_Spacii", "T_Pain", "G_Unit", "Q_Doba", "R_Mani", "A_Finch"]

# function to find the smallest non-zero value in the distance matrix
def findSmallest(dM):
    min_val = float('inf')
    row, col = -1, -1

    # iterate over the distance matrix to find the smallest non-zero value
    for i in range(len(dM)):
        for j in range(i + 1, len(dM[i])):
            if dM[i][j] < min_val and dM[i][j] != 0:
                min_val = dM[i][j]
                row, col = i, j

    return row, col

# function to update the distance matrix based on UPGMA formula
def updateMatrix(dM, row, col):
    # Initialize the new matrix
    new_row_col = []

    # average out the distances of the two smallest clusters with the rest
    for i in range(len(dM)):
        if i != row and i != col:
            # update the distances in the row of the first cluster
            dM[i][row] = (dM[i][row] + dM[i][col]) / 2
            # update symmetrically for the column since the matrix is symmetric
            dM[row][i] = dM[i][row]

    # construct the new matrix without the second cluster's row and column
    for k in range(len(dM)):
        if k != col:
            # create a row excluding the second cluster's column
            new_row = [dM[k][j] for j in range(len(dM)) if j != col]
            # now append the new row to the new matrix
            new_row_col.append(new_row)

    # return the new distance matrix
    return new_row_col

# function to update the species list by merging species at row and col
def updateSpecies(sp, row, col):
    # update the species list by merging the species at row and col
    sp[row] = "(" + sp[row] + "," + sp[col] + ")"
    del sp[col]
    return sp

def UPGMA(dM, sp):
    while len(dM) > 1:
        leastRow, leastCol = findSmallest(dM) # finds the smallest non-0 matrix coordinate
        dM = updateMatrix(dM, leastRow, leastCol)
        sp = updateSpecies(sp, leastRow, leastCol) # updates the species list
        print(dM)
        print(sp)


# Test the UPGMA function
UPGMA(distanceMatrix, speciesList)

