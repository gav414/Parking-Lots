# Main Python Code

class ParkingLot:
    
    
    def __init__(self, row, col, amount):
        self.row = row
        self.col = col
        self.amount = amount
        self.lotList = []
        self.charIsTaken = "X"
        self.charIsOpen = "O"
        self.charIsEmployee = "E"
        
        #Generate lot 2D list
        self.makeLotList()
        
    def __str__(self):
        self.strTopRow = "ABCDEFGHIJKLMNOPQRSTUVWXWZ"
        strLot = "  "
        
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
        Generate an 2D List that serves as a visual representation of the Parking Lot object.
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
        Prompts the user to select a parking spot based on the lot's visual representation. Breaks
        the input into a char (index 0) and integer (index 1).
        '''
        spot = str(input("Please select a spot: "))
        spotRow = spot[0]
        spotCol = spot[1]
        print(f"spotRow={spotRow} and spotCol={spotCol}")
        #print(self.isTaken(spotRow, spotCol))
        if (self.isTaken(spotRow, spotCol)):
            if mode == "SELECT":
                self.lotList[int(spotCol)-1][self.getRowInt(spotRow)] = "X"
            
        
    def getRowInt(self, spotRow):
        for i in range(len(self.strTopRow)):
            if self.strTopRow[i] == spotRow:
                rowIndex = i
                return rowIndex
    def isTaken(self, spotRow, spotCol):
        self.debugPrint(f"spotRow={self.getRowInt(spotRow)} and self.col={self.col}")
        if (self.getRowInt(spotRow)+1 <= self.col):
            rowIndex = self.getRowInt(spotRow)
            if self.lotList[int(spotCol)-1][rowIndex] == "O":
                return True
            else:
                return False
        else:
            print("ERROR: This spot doesn't exist. Please select another spot.")
            return False;

coolLot = ParkingLot(9, 8, 10)

print(coolLot)
coolLot.selectSpot("SELECT")
print(coolLot)
