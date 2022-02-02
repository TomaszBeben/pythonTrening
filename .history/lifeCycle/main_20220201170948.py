class Test:
    # def __new__(cls):
    #     print('hello class')
    def __del__(self):
        print('Nara')

obj = Test()