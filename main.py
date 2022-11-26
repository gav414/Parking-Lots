# Main Python Code

class ParkingLot:

    
    def __init__(self, row, col, amount):
        self.row = row
        self.col = col
        self.amount = amount
        self.lotList = []
        
        #Generate lot 2D list
        self.makeLotList()
    
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
                self.lotList[i].append([])
        
        self.debugPrint(self.lotList)
    
    def selectSpot(self):
        '''
        Prompts the user to select a parking spot based on the lot's visual representation. Breaks
        the input into a char (index 0) and integer (index 1).
        '''
        spot = str(input("Please select a spot: "))
        spotRow = spot[0]
        spotCol = spot[1]
        print(f"spotRow={spotRow} and spotCol={spotCol}")
        #isTaken(spotRow, spotCol)
        
    def isTaken(self, spotRow, spotCol):
        pass

coolLot = ParkingLot(9, 8, 10)
