x = float(input("Nhap x = "))
n = int(input("Nhap n = "))
S = 0.0
if n % 2 == 0:
    S = 2016*x
    T = x
    M = 1
    for i in range(2, n+1):
        T *= x
        M *= 3
        S *= T/M

print("S = ", S)


