#Actividad 2 
print("T11-DM-1244424")
x = int(input("Ingrese un numero mayor a 0: "))
a = int(input("Ingrese un numero mayor a 0: "))
n = int(input("Ingrese un numero mayor a 0: "))

def serie1(n):
    d = int(0)
    c = 0
    for i in range(n):
        d += 1
        c1 = 1/d
        c = c + c1
    print(c)
    
def serie2(n):
    d = int(0)
    c = 0
    for i in range(n):
        d+=1
        c1 = 1/(2**d)
        c = c + c1
    print(c)

def serie3(x,a,n):
    d = int(0)
    c = 1
    k = 1 
    
    for i in range(n):
        d+=1
        c1 = (x*d)(a**(d-k))
        k += 1
        c = c + c1
    print(c)

if n <= 0:
    print("Ingrese un numero valido, que sea mayor a 0")
else:
    serie1(n)
    serie2(n)
    serie3(x,a,n)