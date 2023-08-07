def valid_braces(string):
    brackets = {'(': ')', '{': '}', '[': ']'}

    check = []
    for i in string:
        if i in brackets:
            check.append(i)
        else:
            if (len(check) != 0) and (brackets[check[-1]] == i):
                del check[-1]
            else:
                return False
    else:
        if len(check) == 0:
            return True
        else:
            return False


print(valid_braces("([{}])"))
