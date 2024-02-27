class UnexpectedTypeException(Exception):
    pass


def expected_type(return_types):
    def outer(func):
        def inner(test):
            ans = func(test)
            if isinstance(ans, return_types):
                return ans
            else:
                raise UnexpectedTypeException

        return inner

    return outer


@expected_type((str,))
def return_something(something):
    return something


print(return_something('txt'))
