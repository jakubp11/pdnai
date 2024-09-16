import math
a = float(input())
b = float(input())
c = float(input())
delta = b**2 - 4*a*c
if delta > 0:
    print(f"x1 = {(-b+math.sqrt(delta))/(2*a)}")
    print(f"x2 = {(-b+math.sqrt(delta))/(2*a)}")
elif delta == 0:
    print(f"x0 = {-b/(2*a)}")
else:
    print("brak pierwiastków")
