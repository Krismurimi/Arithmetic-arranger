import re


def arithmetic_arranger(problems, solve = False):
  first = ""
  second = ""
  lines = ""
  sumv = ""
  string = ""
  if len(problems) > 5:
   return "Error: Too many problems."
    
  for problem in problems:
    if re.search("[^\s0-9,+-]",problem):
      if re.search("[/]",problem) or re.search("[*]",problem):
        return "Error: Operator must be '+' or '-'."
      return "Error: Numbers must only contain digits."
      
    parts = problem.split()
    v1 = parts[0]
    op = parts[1]
    v2 = parts[2]
    if (len(v1) >= 5 or len(v2) >= 5 ) :
      return "Error: Numbers cannot be more than four digits."

    
    result = ""
    if op == '+':
      result = str(int(v1) + int(v2))
    elif op == '-':
      result = str(int(v1) - int(v2))

    length = max(len(v1),len(v2)) + 2
    top = str(v1).rjust(length)
    btm = op + str(v2).rjust(length -1)
    line = ""
    res = str(result).rjust(length)

    for s in range(length):
      line += "-"
      
    if problem != problems[-1]:
      first += top + '    '
      second += btm + '    '
      lines += line + '    '
      sumv += res + '    '
    else:
      first += top
      second += btm
      lines += line
      sumv += res

  if solve:
    string = first + "\n" + second + "\n" + lines + "\n" + sumv
  else:
    string = first + "\n" + second + "\n" + lines
  return string




    
      
      
      
    

