#Task:
#*Note: this is the hard version of the task. The only difference is that the hard version has larger numbers. There is NO difference in the problem statement. 

#*Note: 1-indexing is used in this question, meaning the first position is referred to as position 1, NOT position 0

#Pac Man is always scared of ghosts, as a ghost touching Pac Man would mean game over.

#However, there is a catch: after eating a power pellet, Pac Man can eat the ghost instead. 

#Pac Man is currently at position 1, and the ghost is currently at position n. There is a power pellet between them, at position p.

#Pac Man and the ghost both move towards each other, each of them at a speed of one position per second. However, when Pac Man reaches the position of the power pellet, it eats the power pellet and gains speed. It now travels two positions per second.

#The ghost, realising that it is about to be eaten, decides to run in the opposite direction. The speed of the ghost remains the same. 

#It is guaranteed that the power pellet is closer to Pac Man than the ghost. 

#When Pac Man and the ghost are in the same position, Pac Man eats the ghost. 

#Given integers n and p, determine the time when this happens. 

#Note: time starts at t = 1, see below example for more information. 
Ghost = int(input("n: "))
Pellet = int(input("p: "))
Pacman = 1
t = 1

while True:
  if Pacman >= Pellet:
    Pacman += 2
    Ghost += 1
  elif Pacman < Pellet:
    Pacman += 1
    Ghost -= 1
  
  t += 1
  #print(t, Pacman, Pellet, Ghost)
  if Pacman == Ghost:
    break
print(t)
