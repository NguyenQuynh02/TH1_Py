import math

x1 = float(input("x1= "))
y1 = float(input("y1= "))
x2 = float(input("x2= "))
y2 = float(input("y2= "))

D = math.sqrt((x2-x1)**2+(y2-y1)**2)
M = math.fabs(x2-x1)+math.fabs(y2-y1)
C = 1 - (x1*x2 + y1*y2) // math.sqrt(x1*x1+y1*y1)*math.sqrt(x2*x2+y2*y2)

print("Khoảng cách Euclidean giữa A và B: ", D)
print("Khoảng cách Manhattan giữa A và B: ", M)
print("Khoảng cách Cosin giữa A và B: ", C)
