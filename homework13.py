def test(txt, n, a: 6):
    if n < 0:
        return 0
    else:
        return txt, n + (n - 1) ** a


print(test('Итог: ', 5, 6))