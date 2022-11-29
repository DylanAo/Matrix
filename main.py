from matrix import Matrix

a = Matrix(3, 2, [9, 2, 3, 21, 5, 6])
b = Matrix(2, 4, [1, 2, 10, 4, 23, 6, 15, 8])
c = Matrix(3, 2, [18, 19, 23, 1, 3, 51])
print('a = ')
a.print_matrix()
print('b = ')
b.print_matrix()
print('c = ')
c.print_matrix()
print('a + c =')
a.sum(a, c, True)
print('a - c =')
a.sub(a, c, True)
print('c的转置')
c.transpose(True)
print('a * b =')
a.multiply(a, b, True)
print('2 * a = ')
a.number_multiply(2, True)



