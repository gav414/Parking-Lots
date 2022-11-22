# Main Python Code

class ParkingLot:
    def __init__(self, row, col, amount):
        self.row = row
        self.col = col
        self.amount = amount
        
    def makeArray(self):
        lotCol = []
        lotRow = []
        
        for i in range(self.row):
            for j in range(self.col):
                lotCol.append('X')
                print(f"col in j loop={lotCol}")
            lotRow.append(lotCol)
            print(f"row after append={lotRow}")
            lotCol.clear()
            print(f"col after j loop before i loop={lotCol}")
            
        print(lotRow)
    
    def selectSpot(self):
        spot = str(input("Please select a spot: "))
        spotRow = spot[0]
        spotCol = spot[1]
        print(f"spotRow={spotRow} and spotCol={spotCol}")
        #isTaken(spotRow, spotCol)
        
    def isTaken(self, spotRow, spotCol):
        pass

coolLot = ParkingLot(9, 8, 10)

coolLot.selectSpot()
