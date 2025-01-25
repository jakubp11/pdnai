# from random import randint
# def nwd(a,b):
#     if a > b:
#         wieksza = a
#         mniejsza = b
#     if a < b:
#         wieksza = b
#         mniejsza = a
#     reszta = 1
#     while reszta != 0:
#         reszta = wieksza % mniejsza
#         wieksza = mniejsza
#         mniejsza = reszta
#     return wieksza

# def xxx(n):
#     l = []
#     while n > 0:
#         r = randint(1,10)
#         l.append(r)
#         n -= 1
#     return l




# def nww(a,b):
#     return (a*b)/nwd(a,b)

# def xxxx(a,b):
#     if a > b:
#         w = a
#         m = b
#     if b < a:
#         m = a
#         w = b 
#     r = 1
#     while r != 0:
#         r = w % m
#         w = m
#         m = r
#     return w


# print(xxxx(78,66))

# import math

# def czy(n:int)->bool:
#     if n < 2:
#         return False
#     elif n == 2:
#         return True
#     elif n % 2 == 0:
#         return False
#     i = 3
#     while i <= math.sqrt(n):
#         if n % i == 0:
#             return False
#         i += 2
#     return True

# ile = 0 
# for i in range(1,101):
#     if czy(i):
#         print(i)
#         ile += 1
#         print(f" ss{ile}")



# import math
# def czy(n:int)->bool:
#     if n < 2:
#         return False
#     elif n == 2:
#         return True
#     elif n % 2 == 0:
#         return False
#     i = 3
#     while i <= math.sqrt(n):
#         if n % i == 0:
#             return False
#         i += 2
#     return True
# ile = 0
# for i in range(1,101):
#     if czy(i):
#         print(i)
#         ile += 1
# print(f"sss{/ile}")


# import math
# def czy(n:int)->bool:
#     if n < 2:
#         return False
#     elif n == 2:
#         return True
#     elif n % 2 == 0:
#         return False
#     i = 3
#     while i <= math.sqrt(n):
#         if n % i == 0:
#             return False
#         i += 2
#     return True
# ile = 0
# l = []
# for i in range(1,101):
#     if ile == 10 :
#         break
#     elif czy(i):
#         l.append(i)
#         ile += 1
# print(f"sss{ile}")
# print(l)


def dzielw(n:int)->list:
    lst = []
    i = 1
    while i < n:
        if n % i ==0:
            lst.append(i)
        i += 1
    return lst

def suma(lst:list)->float:
    s = 0
    for el in lst:
        s += el
    return s

def czyldos(n:int)->bool:
    if n <= 1:
        return False
    elif suma(dzielw(n)) == n:
        return True
    return False

for i in range(1,10000):
    if czyldos(i):
        print(i)




