# Calculate Temp, Pressure or Volume from the ideal gas law
# The program uses the ideal gas equation 'PV=nRT' and three defined functions
# The user uses standard inputs of P, V, or T to define the function
# Finally the program returns a value for the chosen variable and prints it

def calcTPV(e,f,g):
  # calculates either temperature, pressure, or volume dependant on the values of e, f, and g
  # R=8.314
  
  # Asks for the moles of gas
  n=input('Input a value for the amount of gas in moles: ')
  
  if e == 0 and isnumber(e,f,g,n):
    temp=(abs(float(f))*abs(float(g)))/abs(float(n))*8.314 
    return temp

  elif f == 0 and isnumber(e,f,g,n):
    pres=(abs(float(n))*8.314*abs(float(e)))/abs(float(g)) 
    return pres

  elif g == 0 and isnumber(e,f,g,n):
    vol=(abs(float(n))*8.314*abs(float(e)))/abs(float(f)) 
    return vol  

  # If any of the inputs aren't numbers glaw is recalled
  else:
    print('Please input numerical values.') 
    askTPV()
    
def isnumber(a,b,c,d):
  # Proves whether an input is a number
  # Returns true if input is a number. returns false if input is not a number
  try:
    float(float(a)+float(b)+float(c)+float(d)) 
    return True
  except:
    return False

def glaw():
  # Asks the user what variable they want to calculate
  print
  print('Do you want to calculate Temperature, Pressure, or Volume?')
  getTPV=input('Enter T, P, or V: ');

  if getTPV.lower() =='t':
    V = raw_input('Input a value for volume in meters cubed: ') 
    P = raw_input('Input a value for pressure in pascals: ') 
    print('The temperature of the gas is: ', calcTPV(0,P,V), 'K')

  elif getTPV.lower() == 'p':
    V = raw_input('Input a value for volume in meters cubed: ') 
    T = raw_input('Input a value for temperature in kelvin: ') 
    print('The pressure of the gas is: ', calcTPV(T,0,V), 'Pa')

  elif getTPV.lower() =='v':
    P = raw_input('Input a value for pressure in pascals: ') 
    T = raw_input('Input a value for temperature in kelvin: ') 
    print('The volume of the gas is: ', calcTPV(T,P,0), 'm^3')
  
  # If the response to glaw isn't v,p, or t then glaw is recalled
  else:
    print('Not a valid response. Please follow the instructions.') 
    glaw()

print('This is a calculator for the ideal gas equation PV = nRT')
# Calls glaw() function  
glaw()
