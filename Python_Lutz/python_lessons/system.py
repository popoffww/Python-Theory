
import os
import sys

print("Я, Python.")
print("Я могу: ")
print("1.Вывести список директорий.")
print("2.Вывести информацию о системе.")
enter = int(input("Введите номер действия: "))

if enter == 1:
    print(os.listdir())
elif enter == 2:
    print(sys.platform)
    print(os.getlogin())
else:
    print("Неизвестный ввод.")

