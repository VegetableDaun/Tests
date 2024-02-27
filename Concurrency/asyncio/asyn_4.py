def cur(F):
    def innner(*args, **kwargs):
        g = F(*args, **kwargs)
        g.send(None)

        return g
    return innner
@cur
def subgen():
    while True:
        try:
            message = yield
            print('Subgen recieved:', message)
        except StopIteration:
            print('Done')



if __name__ == "__main__":
    g = subgen()
    g.send(None)

    for i in 'LOL':
        try:
            g.send(i)
            g.throw(StopIteration)
        except StopIteration as e:
            print(e.value)
