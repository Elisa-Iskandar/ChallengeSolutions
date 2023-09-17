#Task:
#Given an array of numbers, N, with 0 being a path and 1 being an obstacle, find out how many times Mario will need to jump to reach the end of the array. 

#Mario can jump over any amount of obstacles in one go, but he can’t jump over a path.

#E.g given the array [0,1,1,0,0,1,0,1,0,0,1,0] mario will need to make 4 jumps to get to the end

pathway = str(input("path: "))
array = []
prev = None
for x in range(len(pathway)):
  if pathway[x] == '0' or pathway[x] != prev:
    array.append(pathway[x])
  prev = pathway[x]
jump = 0
for x in array:
  if x == '1':
    jump += 1

print(jump)
    
