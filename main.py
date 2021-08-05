print("Hello")
# Create a list with numbers 1 to 5
# Create a Function that takes the previous list and returns a list of 
# Touples with the number and the number squared
# Output Example [(1,1),(2,4), ...]

def SquaredTuple(list):
  
  OutputList = []  
  TuplaTemp = ()

  for i in list:
    TuplaTemp = (i,i*i)
    OutputList.append(TuplaTemp)
    TuplaTemp = ()
  
  return OutputList

NumberList = (1,2,3,4,5)

print(SquaredTuple(NumberList))
