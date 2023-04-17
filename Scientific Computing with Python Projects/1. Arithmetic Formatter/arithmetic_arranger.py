def is_addition_subtraction(operator):
  if operator == '+' or operator == '-':
    return True
  return False

def operand_max_length(num1, num2):
  len1 = len(num1)
  len2 = len(num2)
  return len1 if len1 > len2 else len2

def add_dashes(length):
  dash = ""
  for dashes in range(length):
      dash += "-"
  return dash

def solve_problem(num1, operator, num2):
  if operator == '-':
    return int(num1) - int(num2)
  if operator == '+':
    return int(num1) + int(num2)
  
def arithmetic_arranger(problems, print_ans = False):
  if len (problems) > 5:
    return "Error: Too many problems."
  
  arranged_problems = ""
  first_line = ""
  second_line = ""
  dashes = ""
  sums = ""
  is_last = False
  
  for i, problem in enumerate(problems):
    
    if i == len(problems) - 1:
      is_last = True
    
    problem = problem.split()
    if not is_addition_subtraction(problem[1]):
      return "Error: Operator must be '+' or '-'."
    if not problem[0].isdigit() or not problem[2].isdigit():
      return "Error: Numbers must only contain digits."
    if len(problem[0]) > 4 or len(problem[2]) > 4:
      return "Error: Numbers cannot be more than four digits."

    max_length = operand_max_length(problem[0], problem[2])
    
    if not is_last:
      first_line += problem[0].rjust(max_length + 2) + "    "
      second_line += problem[1] + " "
      second_line += problem[2].rjust(max_length) + "    "
      dashes += add_dashes(max_length +2) + "    "
      sums += str(solve_problem(problem[0], problem[1], problem[2])).rjust(max_length + 2) + "    "
    else:
      first_line += problem[0].rjust(max_length + 2)
      second_line += problem[1] + " "
      second_line += problem[2].rjust(max_length)
      dashes += add_dashes(max_length +2)
      sums += str(solve_problem(problem[0], problem[1], problem[2])).rjust(max_length + 2)
      
  arranged_problems = first_line + "\n" + second_line + "\n" + dashes
  
  if print_ans:
    arranged_problems += "\n" + sums
    
  return arranged_problems