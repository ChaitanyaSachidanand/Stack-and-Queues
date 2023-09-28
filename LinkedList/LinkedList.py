class LinkedList_():

    class Node():
        def __init__(self,data):
            self.data = data
            self.link =None

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def is_Empty(self):
        if self.count == 0:
            return True
        else:
            return self.count

    def inset_head(self,element):
        new_node = Node(element)
        if self.count!=0:
            






    