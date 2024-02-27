class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties


# def most_money(students):
#     dict_money = {}
#     for stu in students:
#         dict_money[5 * stu.fives + 10 * stu.tens + 20 * stu.twenties] = stu.name
#
#     if len(dict_money) == 1 and len(students) != len(dict_money):
#         return 'all'
#     else:
#         return dict_money[max(dict_money)]
class Wallet(Student):
    def __init__(self, sn):
        super().__init__(sn.name, sn.fives, sn.tens, sn.twenties)

    def get_money_sum(self):
        return sum([self.fives * 5, self.tens * 10, self.twenties * 20])

    def __gt__(self, other):
        return self.get_money_sum() > other.get_money_sum()

    def __eq__(self, other):
        return self.get_money_sum() == other.get_money_sum()


def most_money(students):
    students = list(map(Wallet, students))
    if all(x == students[0] for x in students) and len(students) != 1:
        return 'all'
    else:
        return max(students).name


phil = Student("Phil", 2, 2, 1)
cam = Student("Cameron", 2, 2, 0)
geoff = Student("Geoff", 0, 3, 0)
ph = Student("Ph", 2, 2, 2)
c = Student("C", 1, 2, 0)
g = Student("G", 3, 3, 0)
print(most_money([cam, geoff, phil, ph, c, g]))
print(phil.__dict__)
