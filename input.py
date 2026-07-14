numX = 0
numY = 0
def GetPoints():
    global numX, numY
    
    while True:
        numX = int(input("Enter the X value: "))
        numY = int(input("Enter the Y value: "))
        return numX, numY