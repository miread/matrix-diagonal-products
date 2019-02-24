def sum_prod_diags(matrix):

    size = len(matrix[0])
    sum1, sum2 = [], []
    out1, out2 = 0, 0

    for i in range(size):
        product, idx, idx2 = 1, 0, i
        while idx2 < size:
            product = product * matrix[idx][idx2]
            idx += 1
            idx2 += 1
        sum1.append(product)

    for i in range(1, size):
        product, idx, idx2 = 1, i, 0
        while idx < size:
            product = product * matrix[idx][idx2]
            idx += 1
            idx2 += 1
        sum1.append(product)

    for i in range(size):
        product, idx, idx2 = 1, i, size - 1
        while idx < size:
            product = product * matrix[idx][idx2]
            idx += 1
            idx2 -= 1
        sum2.append(product)

    for i in range(2, size + 1):
        product, idx, idx2 = 1, 0, size - i
        while idx2 >= 0:
            product = product * matrix[idx][idx2]
            idx += 1
            idx2 -= 1
        sum2.append(product)

    for num in sum1:
        out1 += num
    for num in sum2:
        out2 += num

    return out1 - out2


M1 = [[1, 4, 7, 6, 5],
      [-3, 2, 8, 1, 3],
      [6, 2, 9, 7, -4],
      [1, -2, 4, -2, 6],
      [3, 2, 2, -4, 7]]

print(sum_prod_diags(M1))  # 1098

M2 = [[1, 4, 7, 6],
      [-3, 2, 8, 1],
      [6, 2, 9, 7],
      [1, -2, 4, -2]]

print(sum_prod_diags(M2))  # -11

M3 = [[1, 2, 3, 2, 1],
      [2, 3, 4, 3, 2],
      [3, 4, 5, 4, 3],
      [4, 5, 6, 5, 4],
      [5, 6, 7, 6, 5]]

print(sum_prod_diags(M3))  # 0
