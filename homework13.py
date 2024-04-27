list_ = [1, 2, 3, 4, 5]
def test_(*args):
    print(args)


test_(*list_)


def test_(n):
    if n <= 1:
        return 1
    else:
        return (n * test_(n - 1))


print(test_(9))
