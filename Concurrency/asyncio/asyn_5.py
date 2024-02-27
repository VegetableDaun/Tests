def cur(F):
    def innner(*args, **kwargs):
        g = F(*args, **kwargs)
        g.send(None)

        return g

    return innner

def subgen():
    while True:
        try:
            message = yield
        except:
            pass
        else:
            print('........', message)

@cur
def delegator(g):
    yield from g