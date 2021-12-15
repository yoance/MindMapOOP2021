class MainConsole(object):
    def __init__(self):
        self.nodeList = []
        self.edgeList = []
    def startConsole(self,nodeList,edgeList):
        self.nodeList = nodeList
        self.edgeList = edgeList
        self.console()
        
        print("Console Stopped!")
        return(self.nodeList, self.edgeList)
    def console(self):
        print("Console Started!")
        print("Which Node do you want to see?")
        selectedName = input("Enter Node Name\t\t: ")

        selected = self.searchNode(selectedName)
        while(selected == False):
            print("\nNode not found!")
            selectedName = input("Enter Node Name\t\t:")
            selected = self.searchNode(selectedName)

        print("\nNode's Name\t\t:"+ selected.getName())
        print("Node's ID\t\t:"+ str(selected.getObjectID()))
        print("Node's Description\t:"+selected.getDesc())
        
        print("\nNode's Connections:")
        connected = self.searchEdge(selected.getObjectID())
        if(not connected):
            print("-")
        else:
            for i in connected:
                print(self.searchNode(i.getNode1()).getName() + " is connected to " + self.searchNode(i.getNode2()).getName())

        print("\n\nWould you like to modify current Node?")
        choice = input("Y/N:")
        if(choice == "Y" or choice == "y"):
            name = input("Input Name\t\t:")
            desc = input("Input Description\t:")
            selected.setName(name)
            selected.setDesc(desc)

        print("\nStop Console?")
        choice = input("Y/N:")
        if(choice == "N" or choice == "n"):
            self.console()
                
    def searchNode(self, selected):
        for i in self.nodeList:
            if i.getName() == selected:
                return i
            if i.getObjectID() == selected:
                return i
        return False
    def searchEdge(self, selectedID):
        connected = []
        for i in self.edgeList:
            if i.getNode1() == selectedID or i.getNode2() == selectedID:
                connected.append(i)
        return connected