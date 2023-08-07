class BullsAndCows:
    def __init__(self, secret_number):
        self.check_number(secret_number)
        self.__secret_number = str(secret_number)
        self.__attempts = 8
        self.__win = False

    def check_number(self, number):
        if not isinstance(number, int):
            raise TypeError('Требуется число')

        if not (1234 <= number <= 9876 and len(set(c for c in str(number))) == 4):
            raise ValueError('A number should be positive and contain 4 distinct digits.')

    def compare_with(self, check):
        if self.__win == True:
            return 'You already won!'

        if self.__attempts == 0:
            return "Sorry, you're out of turns!"

        self.check_number(check)

        check = str(check)
        number_bulls = 0
        number_cows = 0

        F = lambda x, y: x == y
        number_bulls = sum(map(F, check, self.__secret_number))
        number_cows = len(set(check) & set(self.__secret_number)) - number_bulls

        self.__attempts -= 1

        if number_bulls == 4:
            self.__win = True
            return 'You win!'

        return f'{number_bulls} bull{"" if number_bulls == 1 else "s"} and {number_cows} cow{"" if number_cows == 1 else "s"}'

        return res
