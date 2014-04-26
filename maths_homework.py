import pylab

def draw_shape(coordinates,name,style=''):
    coordinates.append(coordinates[0])
    x = [x for x,_ in coordinates]
    y = [y for _,y in coordinates]
    pylab.plot(x,y,style,label = name, linewidth=3)

# A
A = [[1,9], [3,9], [4,11], [2,11]]
draw_shape(A, 'A: parallelogram','orange')

# B
B = [[9,1], [6,8], [9,11], [12,8]]
draw_shape(B, 'B: kite')

# C
C = [[-3,2], [-6,6], [-9,6], [-12,2]]
draw_shape(C, 'C: trapezium','pink')

# D

D = [[-7,8], [-9,16], [-5,16]]
draw_shape(D, 'D: isosceles triangle')


# E
E = [[3,-2], [1,-4], [2,-6],[4,-6], [5,-4]]
draw_shape(E, 'E: pentagon')

# F
F = [[8,-13], [12,-13], [12,-17], [8,-17]]
draw_shape(F, 'F: square')

# G
G = [[-3,-3], [-5,-5], [-12,-5], [-10,-3]]
draw_shape(G, 'G: parallelogram')

# H
H = [[-3,-11], [-3,-15], [-7,-15]]
draw_shape(H, 'H: right angle triangle')

pylab.xlim(-20,20)
pylab.ylim(-20,20)
pylab.grid()
pylab.legend(prop={"size":8})
pylab.title('maths homework 26.4.14\nCharlotte Hull')
pylab.show()
