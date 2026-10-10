
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Списки задание 1: ")
print("Первый:", lst[0], "Последний:", lst[-1])
lst[0], lst[-1] = lst[-1], lst[0]
print("После обмена:", lst)
lst[0], lst[-1] = lst[-1], lst[0]

print("Списки задание 2: ")
n = len(lst)
if n % 2 == 0:
    print("Чётная длина, средние элементы:", lst[n//2 - 1], lst[n//2])
else:
    print("Средний элемент:", lst[n//2])

print("Списки задание 3: ")
print("Первые три:", lst[:3])
print("Последние три:", lst[-3:])
print("Чётные индексы:", lst[::2])
print("Обратный порядок:", lst[::-1])

print("Списки задание 4: ")
new_lst = []
new_lst.append(100)
new_lst.append(200)
new_lst.append(300)
new_lst.insert(0, 50)
new_lst.pop()
print("Результат:", new_lst)

print("Списки задание 5: ")
print("Длина:", len(lst))
print("Сумма:", sum(lst))
print("Минимум:", min(lst))
print("Максимум:", max(lst))
print("Среднее:", sum(lst) / len(lst))

print("Списки задание 6: ")
x = 5
print(f"Есть ли {x} в списке:", x in lst)
print(f"Сколько раз встречается {x}:", lst.count(x))
print(f"Индекс первого вхождения {x}:", lst.index(x))

print("Списки задание 7: ")
sorted_lst = sorted(lst)
print("Исходный список:", lst)
print("Три наименьших:", sorted_lst[:3])
print("Три наибольших:", sorted_lst[-3:][::-1])

print("Списки задание 8: ")
other = [11, 12, 13, 14, 15]
merged = lst + other
merged.sort(reverse=True)
print("Объединённый по убыванию:", merged)
print("Второй по величине:", merged[1])

print("Списки задание 9: ")
s = "яблоко банан апельсин груша"
words = s.split()
words.sort()
print("Результат:", ",".join(words))

print("Списки задание 10: ")
k = 3
shifted = lst[-k:] + lst[:-k]
print("Сдвиг на 3 вправо:", shifted)

# ====================================================================================================

print("Строки задание 1: ")
s = input("Введите строку: ")
print("Длина:", len(s))
print("Первый символ:", s[0])
print("Последний символ:", s[-1])

print("Строки задание 2: ")
s = input("Введите строку: ")
n = len(s)
if n % 2 == 0:
    print("Чётная длина, средние символы:", s[n//2 - 1], s[n//2])
else:
    print("Средний символ:", s[n//2])

print("Строки задание 3: ")
s = input("Введите строку: ")
print("Первые три:", s[:3])
print("Последние три:", s[-3:])
print("Чётные индексы:", s[::2])
print("Обратный порядок:", s[::-1])

print("Строки задание 4: ")
s = input("Введите строку: ")
print("Верхний регистр:", s.upper())
print("Нижний регистр:", s.lower())
print("С заглавной буквы:", s.capitalize())

print("Строки задание 5: ")
s = input("Введите строку: ")
c = input("Введите символ: ")
print("Есть ли символ:", c in s)
print("Сколько раз встречается:", s.count(c))
print("Индекс первого вхождения:", s.find(c))

print("Строки задание 6: ")
s = input("Введите строку: ")
print("Замена пробелов:", s.replace(" ", "_"))

print("Строки задание 7: ")
s = input("Введите строку с лишними пробелами: ")
stripped = s.strip()
print("Результат:", repr(stripped))
print("Длина результата:", len(stripped))

print("Строки задание 8: ")
s = input("Введите имя и фамилию через пробел: ")
parts = s.split()
first_name, last_name = parts[0], parts[1]
print("Фамилия:", last_name)
print("Имя:", first_name)
print("Инициалы:", first_name[0] + "." + last_name[0] + ".")

print("Строки задание 9: ")
s = input("Введите строку: ")
normalized = s.lower().replace(" ", "")
if normalized == normalized[::-1]:
    print("Палиндром")
else:
    print("Не палиндром")

print("Строки задание 10: ")
s = input("Введите строку из слов через пробел: ")
words = s.split()
print("Количество слов:", len(words))
print("Первое слово:", words[0])
print("Последнее слово:", words[-1])