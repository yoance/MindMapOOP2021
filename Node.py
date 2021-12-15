class Node(object):
    def __init__(self, objectID, objectType, name="Node", desc='-'):
        self.name = str(name) + str(" ") + str(objectID)
        self.desc = desc
        self.objectID  = objectID
        self.objectType = objectType
    def __repr__(self):
        return self.name
    def display(self):
        print("Name\t\t:", self.name)
        print("Description\t:", self.desc)
        
    def setName(self,name):
        self.name = name
    def setDesc(self,desc):
        self.desc = desc

    def getObjectID(self):
        return self.objectID
    def getName(self):
        return self.name
    def getDesc(self):
        return self.desc