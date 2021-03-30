from workplace import addEvensOnly # <- - - - - - - Workplace Function
import sys

# dont touch this stuff 

numtasks = 4 # <- - - - - Number of tasks, also edit files
variables = {}
perfect = True

for i in range(1, numtasks+1):
  # Argument formatting
  testCase = list(map(int, open(("TestCases/testCase" + str(i) + ".py"), "r").readlines()))

  print("---------- test" + str(i) + " ----------")
  variables["t{0}t".format(i)] = open(("TaskResults/task" + str(i) + "Test.py"), "r").read()

  # Workplace Function Name - - -> arg - -> 
  variables["t{0}a".format(i)] = addEvensOnly(testCase)

  if variables["t{0}t".format(i)] == variables["t{0}a".format(i)]:
    print("|         Success         |")
  else:
    print("|       You failed.       |")
    perfect = False

print("---------------------------")

if perfect == True:
  print("\nCongratulations! You successfully completed the second problem of this competition, Add_Evens_Only! Go try the other ones!")