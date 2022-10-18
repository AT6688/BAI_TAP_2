import math

a = float(input ("nhap chieu dai canh a: "))
b = float(input ("nhap chieu dai canh b: "))
c = float(input ("nhap chieu dai canh c: "))

s=(a+b+c)/2

area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print(" Dien tich cua tam giac la: ", area)
