def pour_jug1_to_jug2(jug1, jug2, capacity1, capacity2):
  total_water = jug1 + jug2
  new_jug2 = min(capacity2, total_water)
  new_jug1 = max(0, total_water - capacity2)
  return new_jug1, new_jug2  

def water_jug_problem():
  jug1, jug2 = 0,0
  capacity1 = int(input("Enter the capacity of jug1: "))
  capacity2 = int(input("Enter the capacity of jug2: "))
  goal = int(input("Enter the desired amount: "))

  steps = [(jug1, jug2)]

  while True:
    if(jug1 == goal or jug2 == goal):
      break

    if(jug1 == 0):
      jug1 = capacity1
    elif(jug2 == capacity2):
      jug2 = 0
    else:
      jug1, jug2 = pour_jug1_to_jug2(jug1, jug2, capacity1, capacity2)

    steps.append((jug1, jug2))

  for i in steps:
    print(i)

water_jug_problem()
#==========================================================================
