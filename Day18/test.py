ARRAY = [i for i in  range(10)]
# print(list(filter(lambda c : c % 3 == 0 , map(lambda b : b * b, map(lambda a : a + 1, ARRAY)) )))

class TestA():
    def func_a(self):
        print("func a of test a")

    @staticmethod
    def func_b():
        print("func b of test a")


class TestB(TestA):
    @staticmethod
    def func_a():
        print("func a of test b")


class TestC(TestB):
    def func_b(self):
        print("func b of test c")


TestA().func_a()
TestB().func_a()
TestB().func_b()