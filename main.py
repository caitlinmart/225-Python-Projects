


def bitwiseOR(P, Q):
     
    P = P.replace(" ","")
    Q = Q.replace(" ", "")
    result =""

    if(len(P) > len(Q)):
      Q = Q.zfill(len(P))
    if(len(Q) > len(P)):
      P = P.zfill(len(Q))

    for i in range(len(P)):
      result += str(int(P[i]) or int(Q[i]))
    return (print(result))
pass



def bitwiseAND(P,Q):

  P = P.replace(" ","")
  Q = Q.replace(" ", "")
  result =""

  if(len(P) > len(Q)):
    Q = Q.zfill(len(P))
  if(len(Q) > len(P)):
    P = P.zfill(len(Q))

  for i in range(len(P)):
      result += str(int(P[i]) and int(Q[i]))
  return(print(result))
pass


def bitwiseXOR(P,Q):

  P = P.replace(" ","")
  Q = Q.replace(" ", "")
  result = ""

  if(len(P) > len(Q)):
    Q = Q.zfill(len(P))
  if(len(Q) > len(P)):
    P = P.zfill(len(Q))

  for i in range(len(P)):
      result += str(int(P[i]) ^ int(Q[i]))
  return(print(result))

pass

def isSatisfiable(P):

  p = True
  q = False
  r = False
  str1 = ""
  str2 = ""
  output = True
  
  for i in P:
    str1 += i

  for i in P:
    if( i == '^'):
      str2 = str2 + " and "
    elif( i == 'v'):
      str2= str2 + " or "
    elif( i == '~'):
      str2 = str2 + " not "
    elif( i == '@'):
      str2 = str2 + " ^ "
    else: 
      str2 = str2 + i
    
  if( eval(str2)):
    output = True
  else:
    output = False
  
  p = False
  q = True
  r = False

  if( eval(str2)):
    output = True
  else:
    output = False

  p = False
  q = False
  r = True

  if( eval(str2)):
    output = True
  else:
    output = False


  return(print(output))
  
  pass

isSatisfiable(['(', 'p', 'v', 'q', 'v' , 'r', ')',  '^', '(', '~', 'p', 'v', '~', 'q', 'v', '~', 'r', ')' ])

bitwiseAND("1","0")