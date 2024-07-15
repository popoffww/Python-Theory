number = int(input())

num_4 = number % 10
num_3 = (number // 10) % 10
num_2 = (number // 100) % 10
num_1 = (number // 1000) % 10

print(num_4, num_3, num_2, num_1)