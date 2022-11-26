# Main Python Code

class ParkingLot:

    
    def __init__(self, row, col, amount):
        self.row = row
        self.col = col
        self.amount = amount
        self.lotList = []
    
    enableDebug = True
    def debugPrint(self, thing):
        if (self.enableDebug):
            print(f"<<DEBUG>>: {thing}")
        
    def makeArray(self):
    
        #Add desired number of rows
        for i in range(self.row):
            #Add a new row (list)
            self.lotList.append([])
            
            #Add desired number of columns  
            for j in range(self.col):
                self.lotList[i].append([])
        
        self.debugPrint(self.lotList)
    
    def selectSpot(self):
        spot = str(input("Please select a spot: "))
        spotRow = spot[0]
        spotCol = spot[1]
        print(f"spotRow={spotRow} and spotCol={spotCol}")
        #isTaken(spotRow, spotCol)
        
    def isTaken(self, spotRow, spotCol):
        pass

coolLot = ParkingLot(9, 8, 10)

coolLot.makeArray()
