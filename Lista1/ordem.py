a = int (input("Entra com o valor de a: "))
b = int (input("Entra com o valor de b: "))
c = int (input("Entra com o valor de c: "))

if a >= b and a >= c :
    if b > c:
        print("ordem: " ,a,b,c)
    else:
        print("ordem: " ,a,c,b)
if b >= a and b >= c :
    if a > c:
        print("ordem: " ,b,a,c)
    else:
        print("ordem: " ,b,c,a)
 
if c >= a and c >= b :
    if a > b:
        print("ordem: " ,c,a,b)
    else:
        print("ordem: " ,c,b,a)
 
         
    
