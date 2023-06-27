# n = int(input())
# m = int(input())
# a1 = []
# a2 = []
# for i in range(n):
#     a1.append(input(i))
#     print(a1)
# for i in range(m):
#     a2.append(input(i))
#     print(a2)
# z = set(a1).intersection(set(a2))
# otv = list(z)
# otv.sort()
# print(otv)



n = int(input())
kust = list()
for i in range(n):
    x = int(input())
    kust.append(x)
yag = list()
for i in range(len(kust)-1):
    yag.append(kust[i - 1] + kust[i] + kust[i + 1])
# yag.append(kust[-2] + kust[-1] + kust[0])
print(max(yag))
