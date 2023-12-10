import copy

a = [1, [2, 3], (4, 5, [6, 7])]
b = a[:]
c = copy.copy(a)
d = copy.deepcopy(a)

a[1][1] = 10
a[2][2][0] = 11

print(f'a: {a}')
print(f'b: {b}')
print(f'c: {c}')
print(f'd: {d}')

print(f'The second element of b and c are the same object: {b[1] is c[1]}')
print(f'The second element of b and d are different objects: {b[1] is not d[1]}')
print(f'The first element of a and b are interned integers: {a[0] is b[0]}')
print(f'The third element of a and b are different objects: {a[2] is not b[2]}')
