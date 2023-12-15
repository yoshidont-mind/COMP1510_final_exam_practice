meals = {'breakfast': 'eggs', 'lunch': 'sandwich', 'dinner': 'steak'}
keys = meals.keys()
values = meals.values()
items = meals.items()
print(keys)
print(values)
print(items)

numbers = [1, 2, 3, 4, 5]
numbers_iter = iter(numbers)  # numbers_iterはイテレーター

for num in numbers_iter:
    print(num)  # リストの数値を一つずつイテレート

