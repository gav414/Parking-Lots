# Main Python Code

class ParkingLot:
    '''
    This class represents a Parking Lot, particularly one that can be found
    at Baldwin Wallace.
    
    Attributes
    ----------
    row: int
        The number of rows the parking lot should have
    col: int
        The number of columns the parking lot should have
    name: str
        The name of the parking lot.
    
    Methods
    -------
    debugPrint(thing):
        Prints a debug print-out, if enableDebug is True.
    makeLotList():
        Generate a 2D List that serves as a visual representation of the
        Parking Lot object.
    selectSpot(mode):
        Prompts the user to select a parking spot based on the lot's visual 
        representation.
    getColInt(self, spotCol):
        Gets the integer value of the column based on the letter passed into the
        program.
    isTaken(self, spotCol, spotRow):
        Determines whether a given spot, as passed in, is available to take.
    editLot(self, spotCol, spotRow, spotType):
        Specify where certain elements are in a parking lot, including
        employee spots, non-spots, or roads.
    '''
    
    def __init__(self, row, col, name):
        self.row = row
        self.col = col
        self.name = name
        self.lotList = []
        self.charIsTaken = "X"
        self.charIsOpen = "O"
        self.charIsEmployee = "E"
        self.strTopRow = "ABCDEFGHIJKLMNOPQRSTUVWXWZ"
        #Generate lot 2D list
        self.makeLotList()
        
    def __str__(self):
        strLot = "\n"
        strLot += self.name + '\n'
        for i in range(len(self.name)):
            strLot += '-'
        strLot += '\n  '
        #Write the column header based on how many columns we got
        for i in range(self.col):
            strLot += self.strTopRow[i] + " "
        strLot += "\n"
        
        #Write the row header and rows
        for i in range(self.row):
            strLot += str(i+1) + " "
            for j in range(self.col):
                strLot += self.lotList[i][j] + " "
            strLot += "\n"
                    
        return strLot
    
    enableDebug = False
    def debugPrint(self, thing):
        '''
        Prints a debug print-out, if enableDebug is True.
            Parameters:
                thing (Object): Any Python object to print out
        '''
        if (self.enableDebug):
            print(f"<<DEBUG>>: {thing}")
    
    
    
    def makeLotList(self):
        '''
        Generate a 2D List that serves as a visual representation of the
        Parking Lot object.
        Used internally.
        '''
        #Add desired number of rows
        for i in range(self.row):
            #Add a new row (list)
            self.lotList.append([])
            
            #Add desired number of columns  
            for j in range(self.col):
                self.lotList[i].append(self.charIsOpen)
        
        self.debugPrint(self.lotList)
    
    def selectSpot(self,mode):
        '''
        Prompts the user to select a parking spot based on the lot's visual 
        representation. Breaks the input into a char (index 0) and integer
        (index 1).
            Parameters:
                mode ("String"): If mode is "SELECT," the user is trying to
                    select a spot that is open. If mode is "UNSELECT," the
                    user is trying to mark a spot that is taken as available.
        '''
        spot = str(input("Please select a spot: "))
        spotCol = spot[0]
        spotRow = spot[1]
        if mode == "SELECT":
            if not (self.isTaken(spotCol, spotRow)):
                self.lotList[int(spotRow)-1][self.getColInt(spotCol)] = "X"
            else:
                print("Cannot park in this spot")
        if mode == "UNSELECT":
            if (self.isTaken(spotCol, spotRow)):
                self.lotList[int(spotRow)-1][self.getColInt(spotCol)] = "O"
            
        
    def getColInt(self, spotCol):
        '''
        Gets the integer value of the column based on the letter passed into the
        program.
            Parameters:
                spotCol (String): Letter representing the desired column
            Returns:
                colIndex (int): Integer that the column letter represents
        '''
        
        #TODO: What happens if a lot is larger than 26?
        #The program supports it. We just need characters to represent it.
        for i in range(len(self.strTopRow)):
            if self.strTopRow[i] == spotCol:
                colIndex = i
                return colIndex

    def doesPositionExist(self, spotCol, spotRow):
        if ((self.getColInt(spotCol)+1 <= self.col) and (int(spotRow) <= self.row)):
            return True
        else:
            return False
                
    def isTaken(self, spotCol, spotRow): 
        '''
        Determines whether a given spot, as passed in, is available to take.
        If the spot is available, the function returns True.
        If the spot is taken (or is an Employee spot, or not a spot), the
        function returns False.
            Parameters:
                spotCol (String): Letter representing the desired column
                spotRow (int): Integer representing the desired row
            Returns:
                True if spot is considered open
                False if spot is considered taken or unavailable
        '''
        self.debugPrint(f"spotCol={self.getColInt(spotCol)} and self.row={self.row}")
        if self.doesPositionExist(spotCol, spotRow):
            colIndex = self.getColInt(spotCol)
            if self.lotList[int(spotRow)-1][colIndex] == "O":
                return False
            else:
                return True
        else:
            print("ERROR: This spot doesn't exist. Please select another spot.")
            return True;

    def editLot(self):
        '''
        Specify where certain elements are in a parking lot, including
        employee spots, non-spots, or roads.
            Parameters:
                spotCol(String): Letter representing the desired coulumn
                spotRow(int): Integer representing the desired row
        '''
        spotCol = input("Which column would you like to edit? ")
        spotRow = int(input("Which row would you like to edit? "))
        spotType = input("Would you like to change the spot to be empty (O), taken (X), or for employees (E)? ")
        if not self.isTaken(spotCol, spotRow):
            self.lotList[spotRow - 1][self.getColInt(spotCol)] = spotType
        else:
            print("Invalid spot.")

pList = []
while True:
    question = input("Would you like to create a new parking lot? ")
    if question.lower() == "yes":
        row = int(input("How long would you like the parking lot? "))
        col = int(input("How many columns would you like your parking lot to have? "))
        lotName = input("What would you like to name the lot? ")
        while True:
            if lotName.lower() == "quit":
                lotName = input("Not applicaple name, enter new name: ")
            else:
                break
        newLot = ParkingLot(row, col, lotName)
        pList.append(newLot)
    elif question.lower() == "no":
        break
    else:
        print("Invalid answer")
        print(pList)
    
while True:
    currentLotName = input("Which lot would you like to bring up or would you like to quit? ")
    if currentLotName.lower() == 'quit':
        break
    for i in range(0, len(pList)):
        if currentLotName == pList[i].name:
            while True:
                currentLot = pList[i]
                print(currentLot)
                answer = input("Park in spot \nLeave spot \nEdit Lot \nQuit \nWhat would you like to do? ")
                if answer.lower() == "park in spot":
                    currentLot.selectSpot("SELECT")
                elif answer.lower() == "leave spot":
                    currentLot.selectSpot("UNSELECT")
                elif answer.lower() == "edit lot":
                    currentLot.editLot()
                elif answer.lower() == "quit":
                    break
                else:
                    print("Not an acceptable answer")
        elif currentLotName.lower() == "quit":
            break
    print("Not a name for a parking lot or 'quit' option.")

