class Parent:
    def method_for_childs(self):
        print("Child is calling me!!!")


class OldChild(Parent):
    pass


class YoungChild(Parent):
    pass


old_child = OldChild()
old_child.method_for_childs()

young_child = YoungChild()
young_child.method_for_childs()