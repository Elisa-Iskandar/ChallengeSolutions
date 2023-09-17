#Task:

#Note: rows are referred to as lanes in this question

#Always staying on the plant side can be boring, so it is time for you to join the zombies!

#In the game mode of “I, Zombie”, you play as the zombie. 

#You are given an integer n, representing the dimensions of the lawn. The lawn will be of n * n size.

#There are n lanes in the lawn, and each lane has n plants in it. 

#The number on the i-th row and the j-th column represents the attack power of the plant at that position. 

#The higher the attack power of a plant, the plant will be stronger and deadlier.

#The lane attack power is defined as the sum of the attack power of the plants in that lane. 

#Since you are playing as the zombies, you want to pick the lane which has the lowest lane attack power so that you have a bigger chance of winning. 

#Determine the lane number with the lowest attack power. Your answer should be an integer between 1 and n.

#Note: your answer should be based on 1-indexing, which means the first lane is referred to as lane 1, and the last lane is referred to as lane n.
lawn_sum = []
sum = 0

for x in range(n):
  lane = str(input("lane: "))
  lane_list = list(lane.split(" "))
  for y in range(n):
    sum += int(lane_list[y])
  lawn_sum.append(sum)
  sum = 0

#print(lawn_sum)
smallest = lawn_sum[0]
for y in range(len(lawn_sum)):
  if lawn_sum[y] < smallest:
    smallest = lawn_sum[y]
    output = y

print(output+1)
