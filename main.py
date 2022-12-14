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
    getColInt(spotCol):
        Gets the integer value of the column based on the letter passed into the
        program.
    doesPositionExist(spotCol, spotRow):
        Determines whether a position exists in the parking lot.
    isTaken(spotCol, spotRow):
        Determines whether a given spot, as passed in, is available to take.
    editLot():
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
        self.strTopRow = "ABCDEFGHIJKLMNOPQRSTUVWXWZ1234567890!@#$%^&*()-_=+{}[]:;'/?.,<>"
        #Generate lot 2D list
        self.makeLotList()
        
    def __str__(self):
        strLot = "\n"
        strLot += self.name + '\n'
        for i in range(len(self.name)):
            strLot += '-'
        strLot += '\n   '
        #Write the column header based on how many columns we got
        for i in range(self.col):
            strLot += self.strTopRow[i] + " "
        strLot += "\n"
        
        #Write the row header and rows
        for i in range(self.row):
            if (i < 9):
                strLot+= " "
            strLot += str(i+1) + " "
            for j in range(self.col):
                strLot += self.lotList[i][j] + " "
            strLot += "\n"
                    
        return strLot
    
    enableDebug = True
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
        doFunction = True
        spot = str(input("Please select a spot: ")).upper()
        spotCol = spot[0]
        
        if len(spot) > 2:
            spotRow = spot[1:3]
            self.debugPrint(f"spotRow={spotRow}")
        elif len(spot) == 2:
            spotRow = spot[1]
        else:
            print("Input couldn't be understood.")
            doFunction = False
        try:
            if mode == "SELECT" and doFunction:
                if not (self.isTaken(spotCol, spotRow)):
                    self.lotList[int(spotRow)-1][self.getColInt(spotCol)] = "X"
                else:
                    print("Cannot park in this spot")
            if mode == "UNSELECT" and doFunction:
                if (self.isTaken(spotCol, spotRow)):
                    self.lotList[int(spotRow)-1][self.getColInt(spotCol)] = "O"
        except:
            print("Input couldn't be understood")
            
        
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
        '''
        Determines whether a position exists in the parking lot.
            Paramters:
                spotCol (String): Letter representing the desired column
                spotRow (int): Integer representing the desired row
            Returns:
                True if the spot exists
                False if the spot does not exist
        '''
        try:
            if ((self.getColInt(spotCol)+1 <= self.col) and (int(spotRow) <= self.row)):
                return True
            else:
                return False
        except:
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
                False if spot is considered open
                True if spot is considered taken or unavailable
        '''
        self.debugPrint(f"spotCol={self.getColInt(spotCol)} and spotRow={spotRow}")
        if self.doesPositionExist(spotCol, spotRow):
            colIndex = self.getColInt(spotCol)
            if self.lotList[int(spotRow)-1][colIndex] == "O":
                return False
            elif self.lotList[int(spotRow)-1][colIndex] == "X"  or self.lotList[int(spotRow)-1][colIndex] == "E":
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
        try:
            spotCol = str(input("Which column would you like to edit? ")).upper()
            spotRow = int(input("Which row would you like to edit? "))
            spotType = str(input("Would you like to change the spot to be empty (O), taken (X), or for employees (E)? ")).upper()
            if not self.isTaken(spotCol, spotRow):
                if spotType == "O" or spotType == "X" or spotType == "E":
                    self.lotList[spotRow - 1][self.getColInt(spotCol)] = spotType
                else:
                    print("Invalid spot type.")
            else:
                print("Invalid spot.")
        except:
            print("Input could not be understood")

pList = []
while True:
    question = input("Would you like to create a new parking lot? ")
    if question.lower() == "yes":
        while True:
            row = int(input("How long would you like the parking lot to be? "))
            if row > 99:
                print("Your parking lot is too long. Please shrink it.\n")
            else:
                break
        while True:
            col = int(input("How wide would you like the parking lot to be? "))
            if col > len("ABCDEFGHIJKLMNOPQRSTUVWXWZ1234567890!@#$%^&*()-_=+{}[]:;'/?.,<>"):
                print("Your parking lot is too wide. Please shrink it.\n")
            else:
                break
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

