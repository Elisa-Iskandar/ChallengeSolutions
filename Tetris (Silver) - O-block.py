#Task:

#The O-block is the square piece in tetris. This piece takes up 4 cells. 

#The playing field is a board of n * m (n rows and m columns). 

#As a tetris player, your goal is to minimise the number of empty cells in your playing field by only putting O-blocks.

#Just like the original game, the blocks fall from top to bottom. Once you are done placing an O-block, another O-block begins to fall. 

#You must use the full block. In other words, for every O-block you place, all 4 cells of the O-block must be inside the playing field. 

#Given integers n and m, find out the minimum number of empty cells you can obtain by placing the O-blocks optimally. 
rows = int(input("n: "))
cols = int(input("m: "))
blocks = 0
if rows <= 1 or cols <= 1:
  print(0)
for x in range(rows//2):
  if cols%2 == 0:
    blocks += (cols/2)
  else:
    blocks += (cols//2)
occupied = blocks*4
field = rows*cols
empty = field - occupied
print(empty)
