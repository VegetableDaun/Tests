def f(a, b, c, *args, key_1=None, key_2=None, key_3=None, **kwargs):
    print(a, b, c)
    print(key_1, key_2, key_3)
    print(args)
    print(kwargs)


f(1, 2, 3, 214, d=235, L='www', V='fadas')
