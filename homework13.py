def test_(a, b=2, c=3.5, txt='Job'):
    print(a, b, c, txt)


test_(15, 1, 15, 'BMV')


def test_(n):
    if n <= 1:
        return 1
    else:
        return (n * test_(n - 1))


print(test_(9))
