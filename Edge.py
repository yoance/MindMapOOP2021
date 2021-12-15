class Edge(object):
    def __init__(self, objectID, objectID1, objectID2):
        self.objectID = objectID
        self.node1 = objectID1
        self.node2 = objectID2
    def getObjectID(self):
        return self.objectID
    def getNode1(self):
        return self.node1
    def getNode2(self):
        return self.node2