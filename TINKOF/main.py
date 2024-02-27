n, m = [int(i) for i in input().split()]

summ = m
summ_next = 0
gifts = map(int, input().split())

for i in gifts:
    if i <= summ:
        summ -= i

print(summ)