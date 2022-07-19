import math as n

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

if a == 0:
    if b == 0 and c == 0:
        print("Phương trình  bậc 1 vô  số nghiệm:")
    elif b == 0 and c != 0:
        print("Phương trình  bậc vô nghiệm:")
else:
    D = b*b - 4*a*c
    if D > 0:
        x1 = (float)((-b + n.sqrt(D))) // (2 * a)
        x2 = (float)((-b - n.sqrt(D))) // (2 * a)
        print("Phương trình có 2 nghiệm là: x1 = ", x1, " và x2 = ", x2)
    elif D == 0:
        x1 = -b / (2 * a)
        print("Phương trình có nghiệp kép: x1 = x2 = ", x1)
    else:
        print("Phương trình vô nghiệm")