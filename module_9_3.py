
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x[0]) - len(x[1]) for x in zip(first, second) if len(x[0]) != len(x[1]))
second_result = (True if len(x) == len(y) else False for x in first for y in second if first.index(x) == second.index(y))

print(list(first_result))
print(list(second_result))