"""Перенаправить содержимое файла с тестом в стандартный поток ввода программы"""
python solution.py < input.txt

"""Использование ввода"""
n = int(input())

"""Вывод данных"""
print()



"""#########################################################"""
""" Релизация простой очереди """
class Queue:
    def __init__(self, max_n):
        self.max_n = max_n  # Максимальное количество мест в списке очереди
        self.queue = [None] * max_n  # Список очереди
        self.head = 0  # Индекс элемента для удаление (начало)
        self.tail = 0  # Индекс элемента для добавления (конец)
        self.size = 0  # Счетчик элементов в очереди

    def is_empty(self):
        return self.size == 0  # Вернет True, если счетчик размера равен нулю

    def push(self, value):
        """Добавление элемента в конец очереди."""
        if self.size != self.max_n:  # Если очередь не забита
            self.queue[self.tail] = value  # Записываем значение
            self.tail = (self.tail + 1) % self.max_n  # определяем след. значение
            # берем именно остаток от деления, чтобы при значении max_n вставился индекс 0 
            self.size += 1  # Увеличиваем значение размера
        else:
            return print('error')

    def pop(self):
        if self.is_empty():
            return print('None')
        else:
            x = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.max_n
            self.size -= 1
            return print(x)

    def peek(self):
        if self.is_empty():
            return print('None')
        else:
            return print(self.queue[self.head])

    def get_size(self):
        return print(self.size)


def main():
    command_num = int(input())
    max_n = int(input())
    queue = Queue(max_n)
    for i in range(command_num):
        command = (str(input())).split(' ')
        # print(f'Выполняем команду {command}')
        if command[0] == 'push':
            queue.push(command[1])
            continue
        if command[0] == 'pop':
            queue.pop()
        if command[0] == 'peek':
            queue.peek()
        if command[0] == 'size':
            queue.get_size()


if __name__ == '__main__':
    main()


"""#########################################################"""
"""Реализация бинарного поиска с помощью рекурсивной функции"""
функция binarySearch(arr, x, left, right):
    if right <= left: # промежуток пуст
        return -1
    # промежуток не пуст
    mid = (left + right) // 2
    if arr[mid] == x: # центральный элемент — искомый
        return mid
    elif x < arr[mid]: # искомый элемент меньше центрального
                       # значит следует искать в левой половине
        return binarySearch(arr, x, left, mid)
    else: # иначе следует искать в правой половине
        return binarySearch(arr, x, mid + 1, right)

# изначально мы запускаем двоичный поиск на всей длине массива
index = binarySearch(arr, x, left = 0, right = len(arr))
