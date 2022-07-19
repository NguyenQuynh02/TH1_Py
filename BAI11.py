#Nhập một số nguyên có ít hơn 5 chữ số, in ra màn hình
#cách đọc số nguyên đó
#(ví dụ: số 1523 đọc là: 1 ngàn 5 trăm 2 chục 3 đơn vị).
n = int(input("Nhập một số nguyên : "))
while n < 0 or n >= 10000:
    print("n thuộc [0,9999]. Mời nhập lại: ")
    n = int(input("Nhập một số nguyên: "))
N = n//1000
T = (n % 1000)//100
C = (n % 100)//10
D = n % 10
print("{} nghìn {} trăm {} chục {} đơn vị".format(N, T, C, D))