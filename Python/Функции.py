enumerate()
# Создает массив пронумерованных элементов, с которым можно что-то делать
employee_names = ["Paul", "John", "Abbie", "Charlotte", "Ron"]

for index, name in enumerate(employee_names, 1):
	print(index, name)

collections.Counter()
# Считает количество вхождений в массиве
any_massive = ['any_values']
counted_numbers = collections.Counter(any_massive)
print(counted_numbers['any_value'])  # Выведет количество этих значений в 