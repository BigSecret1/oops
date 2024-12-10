class GrandParents:
    def __init__(self):
        print("Greeting from grandparents")


class Parents(GrandParents):
    def __init__(self):
        super().__init__()
        print("Greetings from parents")

    def parent_age(self):
        print("We are still young woman !")


class Child(Parents):
    def __init__(self):
        super().__init__()
        print("Greetings from child")


child = Child()
child.parent_age()