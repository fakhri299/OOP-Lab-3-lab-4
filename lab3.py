numbers = input()

numbers_list = numbers.split()

numbers_list = [int(num) for num in numbers_list if int(num)<20]

print(*numbers_list)





