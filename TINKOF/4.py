def buy(tree: list[tuple], comp: list):
    price = []
    for i in range(len(tree)):
        under_tree = find_under_tree(i, tree)
        price.append(buy_under_tree(under_tree, comp))

    return price


def find_under_tree(i, tree):
    under_tree = []
    under_tree.append(tree[i])

    for j in range(i, len(tree)):
        if tree[j][0] == i + 1:
            # if j + 1 < len(tree):
            under_tree.extend(find_under_tree(j, tree))
    return under_tree


def buy_under_tree(tree: list[tuple], comp: list):
    buyed_comp = set()
    price_comp = 0

    for i in tree:
        buyed_comp.add(i[2])
        price_comp += i[1]

    if buyed_comp == set(comp):
        return price_comp
    else:
        return -1




n, k = [int(i) for i in input().split()]

comp = []
for _ in range(k):
    comp.append(input())

tree = []
for _ in range(n):
    p, a, name = [i for i in input().split()]
    tree.append((int(p), int(a), name))

price = buy(tree, comp)

while -1 in price:
    price.remove(-1)

if min(price) == -1:
    print(-1)
else:
    print(min(price))
