
def bitwiseAND(a,b):
  output = 1
  if( a == "1" and b == "1"):
    output = 1
    print("AND ({},{}) = {} (TRUE)".format(a,b,output))
  else:
    ouput = 0
    print("AND ({},{}) = {} (FALSE)".format(a,b,output))
  pass
    
def bitwiseOR(a,b):
  output = 1

  if( a == "1" and b == "0"):
    ouput = 1
    print("OR ({},{}) = {} (TRUE)".format(a,b,output))
  elif(a == "0" and b == "1"):
    ouput = 1
    print("OR ({},{}) = {} (TRUE)".format(a,b,output))
  elif(a == "1" and b == "1"):
    output = 0
    print("OR ({},{}) = {} (FALSE)".format(a,b,output))
  elif( a == "0" and b == "0"):
    output = 0
    print("OR ({},{}) = {} (FALSE)".format(a,b,output))
  pass

def bitwiseXOR(a,b):
  output = 1 
  if(a == "1" and b == "0"):
    output = 1
    print("XOR ({},{}) = {} (TRUE)".format(a,b,output))
  elif(b == "1" and a == "0"):
    output = 1 
    print("XOR ({},{}) = {} (TRUE)".format(a,b,output))
  else:
    output = 0 
    print("XOR ({},{}) = {} (FALSE)".format(a,b,output))
  pass

def bitwiseNOR(a,b):
  output = 1
  if(a == "0" and b == "0"):
    output = 1
    print("NOR ({},{}) = {} (TRUE)".format(a,b,output))
  elif(a == "1" and b == "0"):
    output = 1 
    print("NOR ({},{}) = {} (TRUE)".format(a,b,output))
  elif(a=="0" and b == "1"):
    output = 1
    print("NOR ({},{}) = {} (TRUE)".format(a,b,output))
  else:
    output = 0
    print("NOR ({},{}) = {} (FALSE)".format(a,b,output))
  pass

def bitwiseNAND(a,b):
  output = 1
  if(a=="1" and b == "0"):
    output = 1
    print("NAND ({},{}) = {} (TRUE)".format(a,b,output))
  elif(a=="0" and b == "1"):
    output = 1
    print("NAND ({},{}) = {} (TRUE)".format(a,b,output))
  else:
    output = 0
    print("NAND ({},{}) = {} (FALSE)".format(a,b,output))
  pass

def bitwiseNOT(a,b):
  output = 1
  if( a == "1" and b == "0"):
    output = 1
    print("NOT ({},{}) = {} (TRUE)".format(a,b,output))
  elif(a == "0" and b == "1"):
    ouput = 1
    print("NOT ({},{}) = {} (TRUE)".format(a,b,output))
  elif( a == "0" and b == "0"):
    output = 1
    print("NOT ({},{}) = {} (TRUE)".format(a,b,output))
  else:
    output = 0
    print("NOT ({},{}) = {} (FALSE)".format(a,b,output))
  pass

def bitwiseXNOR(a,b):
  output = 1
  if( a == "1" and b == "1"):
    ouput = 1
    print("XNOR ({},{}) = {} (TRUE)".format(a,b,output))
  elif(a == "0" and b == "0"):
    output = 1
    print("XNOR ({},{}) = {} (TRUE)".format(a,b,output))
  else:
    output = 0 
    print("XNOR ({},{}) = {} (FALSE)".format(a,b,output))
  pass


print("Logic Gates:")
print("Enter a value for A (0 or 1): ")
a = input()
print("Enter a value for B (0 or 1): ")
b = input()
 
op = True 
while(op == True):
  print("select one of the following operators: AND, OR, NAND, NOR, XOR, or XNOR")
  operator = input()
  if(operator == "AND"):
      print("AND operator selected.")
      bitwiseAND(a,b)
      op = False
  elif(operator == "OR"):
      print("OR operator selected.")
      bitwiseOR(a,b)
      op = False
  elif( operator == "XOR"):
      print("XOR operator selected.")
      bitwiseXOR(a,b)
      op = False
  elif(operator == "NAND"):
      print("NAND operator selected.")
      bitwiseNAND(a,b)
      op = False
  elif(operator == "NOR"):
      print("NOR operator selected.")
      bitwiseNOR(a,b)
      op = False
  elif(operator == "NOT"):
      print("NOT operator selected.")
      bitwiseNOT(a,b)
      op = False
  elif(operator == "XNOR"):
      print("XNOR operator selected.")
      bitwiseXNOR(a,b)
      op = True
  
