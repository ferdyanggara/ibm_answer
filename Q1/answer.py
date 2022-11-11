case = """5
XL XXXXXXXXXL XXS M XXS
4
L M L XXS"""

def solve(case):
  if case[2] > case[0]: 
    return "No"
  from collections import Counter 
  shirt_map = Counter(case[1].split(" "))
  request_map = Counter(case[3].split(" "))
  for req_shirt, quantity in request_map.items(): 
    while quantity > 0: 
      if not req_shirt: 
        return "No"
      if len(req_shirt) > 1001: 
        return "No"
      if req_shirt in shirt_map and shirt_map[req_shirt] != 0: 
        shirt_map[req_shirt] -= 1
        quantity -= 1
      else: 
        if "X" in req_shirt and "S" in req_shirt: 
          req_shirt = req_shirt[1:]
        elif req_shirt == "S":
          req_shirt = "M"
        elif req_shirt == "M":
          req_shirt = "L"
        elif "L" in req_shirt:
          req_shirt = "X" +req_shirt
  return "Yes"
      

print(solve(case.split("\n")) == "Yes")



