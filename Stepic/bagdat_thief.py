# Код писать сюда \(❤‿❤)/
import copy

N = int(input())
carta = [list(input()) for _ in range(N)]
way = [['-'] * N for _ in range(N)]


def step(carta, way, i, j, count):
    count = count + int(carta[i][j])
    way[i][j] = '#'
    count, way = look_for(carta, way, i, j, count)

    return count, way


def look_for(carta, way, i=0, j=0, count=0):
    way[0][0] = '#'
    way_1 = copy.deepcopy(way)
    way_2 = copy.deepcopy(way)

    if j != N - 1 and carta[i][j + 1] != '0':
        count_1, way_1 = step(carta, way_1, i, j + 1, count)
    else:
        count_1, way_1 = count, way

    if i != N - 1 and carta[i + 1][j] != '0':
        count_2, way_2 = step(carta, way_2, i + 1, j, count)
    else:
        count_2, way_2 = count, way

    if count_1 > count and count_2 > count:
        return min(((count_1, way_1), (count_2, way_2)), key=lambda x: x[0])
    elif count_1 > count or count_2 > count:
        return max(((count_1, way_1), (count_2, way_2)), key=lambda x: x[0])
    else:
        return count, way


if carta[0][0] == '0':
    print('Impossible')
else:
    count, way = look_for(carta=carta, way=way)
    if way[N - 1][N - 1] != '#':
        print('Impossible')
    else:
        for s in way:
            print(''.join(s))
