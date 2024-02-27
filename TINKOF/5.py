class child:
    def __init__(self, name, count_manul):
        self.name = name
        self.count_manul = count_manul

        self.friends = []

    def add_sticker(self, num_sticker):
        self.count_manul += num_sticker

    def add_friend(self, friend):
        self.friends.append(friend)

    def send_sticker(self, num_sticker):
        for i in self.friends:
            i.add_sticker(num_sticker)

n, m, q = [int(i) for i in input().split()]
counted_manuls = [int(i) for i in input().split()]

children = []
for i in range(n):
    children.append(child(f'child_{i}', counted_manuls[i]))

friends = []
for i in range(m):
    friends.append([int(i) for i in input().split()])

for i in friends:
    children[i[0] - 1].add_friend(children[i[1] - 1])
    children[i[1] - 1].add_friend(children[i[0] - 1])

for i in range(q):
    event = input().split()
    if event[0] == "?":
        print(children[int(event[1]) - 1].count_manul)
    elif event[0] == "+":
        children[int(event[1]) - 1].send_sticker(int(event[2]))
