# method resolution order [mro]
class A:
    def __init__(self):
        print("A's constructor")

    def method_a(self):
        print("method in A")


class B(A):
    def __init__(self):
        print("B's construcotr")
        super().__init__()

    def method_a(self):
        print("method in b")
        super().method_a()


class C(A):
    def __init__(self):
        print("C's constructor")
        super().__init__()

    def method_a(self):
        print("method in c")
        super().method_a()


class D(B, C):
    def __init__(self):
        print("D's constructor")
        super().__init__()

    def method_a(self):
        print("mehtod in D")
        super().method_a()


d = D()
d.method_a()