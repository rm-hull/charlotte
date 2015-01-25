import sys
import mcpi.minecraft as minecraft
import mcpi.block as block

row = 0
column = 0
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

letters = dict(
    C = [124,130,130,130,68],
    h = [254,32,32,32,30],
    a = [28,34,34,62,2],
    r = [30,32,32,32,16],
    l = [252,2,2,2,4],
    o = [28,34,34,34,28],
    t = [32,32,252,34,34],
    e = [28,42,42,42,16],
)
    
def is_odd(x):
    if x % 2 == 0:
        return False
    else:
        return True

def place_block(blocktype):
    global row
    row  = row + 1
    if blocktype == '#':
        mc.setBlock(pos.x+3, pos.y+row, pos.z+column, block.GLOWING_OBSIDIAN.id)  
        
def next_column():
    global column
    global row
    row = 0
    column = column + 1
    
def print_column(x):
    for b in range(8):
        if is_odd(x):
            place_block('#')
        else:
            place_block(' ')
        x = x/2
       
    next_column()
              
def print_letter(c):
    print_column(0)   # print a spacer column
    for i in letters[c]:
        print_column(i)
        
def print_word(w):
    for c in w:
        print_letter(c)
     
print_word('Charlotte') 
