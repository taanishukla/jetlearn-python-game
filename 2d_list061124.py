matrix=[[23,55,92],[68,94,33],[20,42,86]]
print (matrix)
print (matrix[1][1])
print(len(matrix))

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j])

for i in range(len(matrix)):
    print(matrix[i][i])
    print(matrix[i][len(matrix)-i-1])