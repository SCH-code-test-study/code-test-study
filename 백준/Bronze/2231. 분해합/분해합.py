# n = input()

# result = 0
# num = 1

# while num <= int(n):
#     check = num
#     s = str(num)
#     for i in s:
#         check += int(i)
#     if check == int(n):
#         result = num
#         break
#     num += 1

# print(result)
n = int(input())

start = 0
result = 0

while start != n:
    check = 0
    if start <= 9:
        check = start + start
    elif start <= 99:
        check = start + (start // 10) + (start % 10)
    elif start <= 999:
        check = start + (start // 100) + ((start // 10) %
                                          10) + (start % 10)
    elif start <= 9999:
        check = start + (start // 1000) + ((start // 100) % 10) + \
            ((start // 10) % 10) + (start % 10)
    elif start <= 99999:
        check = start + (start // 10000) + ((start // 1000) % 10) + \
            ((start // 100) % 10) + ((start // 10) % 10) + (start % 10)
    elif start <= 999999:
        check = start + (start // 100000) + ((start // 10000) % 10) + \
            ((start // 1000) % 10) + ((start // 100) %
                                      10) + ((start // 10) % 10) + (start % 10)
    if check == n:
        result = start
        break
    start += 1

print(result)
