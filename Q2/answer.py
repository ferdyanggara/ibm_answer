allValid = True 
errorCodes = []

with open('/Users/ferdy/interview/ibm_answer/Q2/input.txt', 'r') as f: 
  for idx, input in enumerate(f.readlines()):
    if idx > 0: 
      input = input.split(" ")
      if input[1] == "false":
        allValid = False
        errorCodes.append(input[2].strip("\n"))

if allValid: 
  print("Yes")
else: 
  print("No")
  print(" ".join(errorCodes), end="")
