matrix = [[3.499, 3.512, 3.602, 37.791],
          [-7.117, 3.602, 3.811, 3.52],
          [3.748, 3.901, -5.958, 3.85]]

# matrix = [[0.21, -0.45, -0.20, 1.91],
#           [0.30, 0.25, 0.43, 0.32],
#           [0.60, -0.35, -0.25, 1.83]]


def gauss_slau():
    
    for k in range(1, len(matrix)):
        for j in range(k, len(matrix)):
            m = matrix[j][k-1] / matrix[k-1][k-1]
            for i in range(0, len(matrix)+1):
                matrix[j][i] = matrix[j][i] - m * matrix[k-1][i]
    
        
    biases = [matrix[i][len(matrix)] for i in range(0, len(matrix))]
    
    for i in range(len(matrix)-1, -1, -1):
        biases[i] = matrix[i][len(matrix)] / matrix[i][i]
        for c in range(len(matrix)-1, i, -1):
            biases[i] = biases[i] - matrix[i][c] * biases[c] / matrix[i][i]
            
    return biases
    
ans = gauss_slau()

print('Results: ' + ans)
