class Node:
    def __init__(self, dataval):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def AtBegining(self, newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode

    def AtEnd(self, nwdata):
        NewNode = Node(nwdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval=NewNode

        # Function to add node
    def Inbetween(self, middle_node, newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return
        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode


list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
list.headval.nextval = e2
list.AtBegining("Sun")
list.AtEnd("Sat")
list.Inbetween(list.headval.nextval, "Wed")
list.listprint()