def test(arg1, arg2 = 'World', *args, **kwargs):
    print(arg1, arg2, args, kwargs)

test('Hello')
test('Hi', 'Tomek', '1', '2', test='test')