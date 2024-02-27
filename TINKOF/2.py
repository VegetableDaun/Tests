def connect(developers : int, limits : list[int]):

    while limits:
        max_coop = max(limits)
        limits.pop(limits.index(max_coop))
        developers -= 1 + max_coop

        if developers <= 0:
            break

        for i in range(max_coop):
            ind = limits.index(max(limits))
            limits[ind] -= 1

            if limits[ind] == 0:
                limits.pop(ind)
                # developers -= 1

        if len(limits) == 1:
            break

    if developers <= 0:
        print("Yes")
    else:
        print("No")


num_data = int(input())
for i in range(num_data):
    developers = int(input())
    limits = list(map(int, input().split()))

    connect(developers, limits)