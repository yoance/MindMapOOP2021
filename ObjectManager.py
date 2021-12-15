class ObjectManager(object):
    def __init__(self):
        self.totalObject = 0
        self.deletedObject = []
        #self.nDigits = 5
    def newObject(self):
        self.totalObject = self.totalObject + 1
        # self.objectType = objectType
        return self.totalObject
        # str_ID = str(self.totalObject)
        # self.zero_filled_ID = str_ID.zfill(self.nDigits)
        # return self.zero_filled_ID
    def getLatestObjectID(self):
        return self.totalObject
        # return self.zero_filled_ID
    def removeObject(self, objectID):
        self.deletedObject.append(objectID)