def test_(a, b=2, c=3.5, txt='Job'):
    print(a, b, c, txt)


test_(15, 1, 15, 'BMV')


def test(txt, n):
    if n < 0:
        return 0
    else:
        return txt, n + (n - 1)


print(test('Итог: ', 9))
