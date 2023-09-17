#Task:

#In another world of snakes, the apples can have different sizes! 

#In fact, most of the apples are larger than the snake's mouth. The snake can only eat apples with size less than or equal to the size of its mouth. 

#However, the snake has the ability to grow. After eating an apple with size k, the size of the snake’s mouth increases by k.

#For example, if the snake’s mouth is currently size 5, after eating an apple of size 3, the snake’s mouth is now size 8. The snake can now eat apples with size less than or equal to 8.

#The snake begins with a mouth of size 1.

#You are first given an integer n, the number of apples available. 

#Next, you are given an array of apple sizes. (the array will contain n elements)

#Determine the maximum number of apples the snake can eat. The apples can be eaten in any order. 
mouth_size = 1
apples = int(input("n: "))
apple_sizes = []
sizes = input("sizes: ")
apple_sizes = sizes.split(" ")
for x in range(len(apple_sizes)):
  apple_sizes[x] = int(apple_sizes[x])


apple_sizes.sort()
count = 0
for y in apple_sizes:
  if mouth_size >= y:
    mouth_size += y
    count+=1
  else:
    break

print(count)
