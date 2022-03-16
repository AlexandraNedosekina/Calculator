my_A_rows = int(input("введите число строк матрицы коэфициентов: "))
    
print("введите матрицу коэфициентов (по строкам, пробелы между коэффициентами)")
A = [list(map(float, (input(f"строка {i+1}: ").split()))) 
            for i in range(my_A_rows) ]

B = [list(map(float, input("Введите матрицу правых частей, пробелы между числами: ").split()))]
B = list(B)


def minorMatrix(i,j,k):
    return [row[:k] + row[k+1:] for row in (i[:j]+i[j+1:])]

def getMatrixDeternminant(i):
    # Если матрица размера 2x2
    if len(i) == 2:
        return i[0][0]*i[1][1]-i[0][1]*i[1][0]

    determinant = 0
    for c in range(len(i)):
        determinant += ((-1)**c)*i[0][c]*getMatrixDeternminant(minorMatrix(i,0,c))
    return determinant
print ("Матрица А")
print (A,"\n")

print ("Матрица B")
print (B,"\n")

print ("Определитель матрицы А")
print (getMatrixDeternminant(A), "\n")