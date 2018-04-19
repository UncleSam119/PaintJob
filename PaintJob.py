

def getFloat(prompt):
    fInput = -1
    while fInput < 0:
       try:
           fInput = float(input(prompt))
       except ValueError:
           print('Input must be numerical non-negative')
    return fInput








def main ():



