def ckeck_letters(l : str):
    S = "TINKOFF"

    if set(l) == set(S) and l.count("F") == 2:
        print("Yes")
    else:
        print("No")


num = int(input())
for i in range(num):
    l = input()
    ckeck_letters(l)
