#Task:

#Gnop has recently been learning how to use pygame (a game engine using python), and to practise his skills he decided to recreate pong.

#However, the recreation did not go as successfully as Gnop had wanted - there is a bug where the Pong ball gets stuck at the edges of the screen.

#Gnop is devastated, but instead of solving the bug, Gnop decides to make this a feature and decides that a stuck ball means a draw for each player.

#For each player, the score string of the player is a string representing the results of each round. 

#Each character of the string can be a:

#‘W’, representing a win. A win causes the score of the winner to increase by 3.

#‘L’, representing a loss. A loss causes the score of the player to decrease by 1. 

#‘D’, representing a draw. A draw causes the score of both players to increase by 1.

#Gnop is supposed to store the score string for both players, but he forgot to do so in his program!

#Given the score string of player A, find the score string of player B and hence calculate the final score of player B.

#*Note that a win by player A means a loss for player B and vice versa. Also, a draw by player  A means a draw for player B.
playerA = input("A: ")
score = 0
for x in playerA:
  if x == "W":
    score -= 1
  elif x == "L":
    score += 3
  else:
    score += 1
print(score)
