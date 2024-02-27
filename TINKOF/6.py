n, q = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

for i in range(q):
    event = input().split()
    if event[0] == "?":
        new_a = []
        for i in range(len(a)):
            new = int(event[3]) * i + int(event[4])
            new_a.append(min(a[i], new))
        print(max(new_a[int(event[1]) - 1 : int(event[2])]))

    elif event[0] == "+":
        for i in range(int(event[1]) - 1, int(event[2]) + 1):
            a[i] += int(event[3])