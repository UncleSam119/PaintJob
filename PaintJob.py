

def getFloat(prompt):
    # this function prompts for input and validates the data then returns
    finput = -1
    while finput < 0:
       try:
           finput = float(input(prompt))
       except ValueError:
           print('Input must be numerical non-negative')
    return finput


def getState():
    # This function prompts the user for the that they are in and returns that
    sState = input('Please enter the states abbreviations that the job is being done in(example: Massachusetts = Ma): ')

    # Converting string to uppercase to make for easier if statements
    return sState.upper()


def getGallonsOfPaint(fSquare, fFeet):
    # this function calculates how many gallons of paint is needed
    fGallons = fSquare / fFeet

    # Rounding and returning
    iGall = int(fGallons)
    return iGall if iGall - 1 < fGallons <= iGall else iGall + 1


def getLaborHours(iGallons, fLaborHours):
    # this function determines how long the job is going to take
    iHours = iGallons * fLaborHours
    return iHours


def getLaborCost(fHours, fCostlabor):
    # this functions determines the cost of labor for the job
    fCost = fHours * fCostlabor
    return fCost


def getPaintCost(iGallons, fPaintPrice):
    # this functions determines the total cost of the paint
    fCost = iGallons * fPaintPrice
    return fCost


def getSalesTax(sState):
    # this function calculates the sales tax percent
    if sState == 'CT': return 0.06
    elif sState == 'MA': return 0.0625
    elif sState == 'ME': return 0.085
    elif sState == 'NH': return 0.00
    elif sState == 'RI': return 0.07
    elif sState == 'VT': return 0.06
    else: return 0.0


def showCostEstimate(fLabor, fPaint, fTax):
    # This function shows the final cost and the total while also making a file with the information
    fTotalTax = (fLabor + fPaint) * fTax
    fFinalTotal = fLabor + fPaint + fTotalTax

    # To the screen
    print('\n---------------------------------------------------------------------------------------------\n')
    print('Final labor cost: $' + '{0:,.2f}'.format(fLabor), '\nFinal paint cost: $' + '{0:,.2f}'.format(fPaint))
    print('Tax cost: $' + '{0:,.2f}'.format(fTotalTax), '\nTotal job cost: $' + '{0:,.2f}'.format(fFinalTotal))

    # To the file
    myfile = open('PaintJobOutput.txt', 'w')
    myfile.write('Final labor cost: $' + '{0:,.2f}'.format(fLabor))
    myfile.write('\nFinal paint cost: $' + '{0:,.2f}'.format(fPaint))
    myfile.write('\nTax cost: $' + '{0:,.2f}'.format(fTotalTax))
    myfile.write('\nTotal job cost: $' + '{0:,.2f}'.format(fFinalTotal))

    myfile.close()


def main ():

    # Here we are calling the input function to get all the information from the user
    fSquarefeet = getFloat('Enter square feet of the wall: ')
    fPaintPrice = getFloat('Enter the price of the paint: ')
    fFeetPer = getFloat('Enter the feet per gallon of paint: ')
    fLaborHours = getFloat('Enter the labor hours per gallon of paint: ')
    fCostLabor = getFloat('Enter the cost of labor per hour: ')
    sState = getState()

    # This is where we find out how many gallons of paint we need
    iGallons = getGallonsOfPaint(fSquarefeet, fFeetPer)

    # Call the LaborHours function to determine how long it is going to take
    fHours = getLaborHours(iGallons, fLaborHours)

    # Calculating the labor cost
    fFinalLaborCost = getLaborCost(fHours, fCostLabor)

    # Calculating the paint cost
    fFinalPaintCost = getPaintCost(iGallons, fPaintPrice)

    # Calculating the sales tax
    fSalesTax = getSalesTax(sState)

    # Finally calling the print function with everything
    showCostEstimate(fFinalLaborCost, fFinalPaintCost, fSalesTax)


main()
