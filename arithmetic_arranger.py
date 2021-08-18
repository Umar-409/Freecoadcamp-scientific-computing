import re

def arithmetic_arranger(problems, solve=False):
  if(len(problems) > 5):
    return "Error: Too many problems."

  first = ""
  secound = ""
  lines = ""
  sumx = ""
  string = ""
  for problem in problems:
    if (re.search("[^\s0-9.+-]", problem)):
      if re.search("[/]", problem or re.search("[*]", problem)):
        return "Error: Operator must be '+' or '-'."
      return 'Error: Numbers must only contain digits.'

    firstnumber = problem.split(" ")[0]
    operator = problem.split(" ")[1]
    secoundnumber = problem.split(" ")[2]

    if (len(firstnumber) >=5 or len(secoundnumber) >= 5):
      return "Error: Numbers cannot be more than four digits."

    sum = ""
    if(operator == "+"):
      sum = str(int(firstnumber) + int(secoundnumber))
    elif (operator == "-"):
      sum = str(int(firstnumber) - int(secoundnumber))

    length = max(len(firstnumber), len(secoundnumber)) + 2
    top = str(firstnumber).rjust(length)
    bottom = operator + str(secoundnumber).rjust(length - 1)
    line = ""
    res = str(sum).rjust(length)
    for s in range(length):
      line += "-"

    if problem != problems[-1]:
      first += top + '    '
      secound += bottom + '    '
      lines += line + '    '
      sumx += res + '    '
    else:
      first += top
      secound += bottom
      lines += line
      sumx += res

  if solve:
    string = first + "\n" + secound + "\n" + lines + "\n" + sumx
  else:
    string = first + "\n" + secound + "\n" + lines
  return string

