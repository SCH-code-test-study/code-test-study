i = int(input())
a = 0
b = 0
n = 1
count = 0


# def pac(n):
#     global count
#     print(n)
#     if count >= i:
#         return n
#     else:
#         count += 1
#         return n +


# print(pac(0))

while count < i:
    b = a
    a += n
    n = b
    print(a, n)
    count += 1


print(a)
