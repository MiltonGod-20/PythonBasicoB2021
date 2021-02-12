#EJERCICIO 1
n=int(input("INGRESE CANTIDAD DE ESCALONES: "))
for i in range(n+1):
    print('$'*i)
    


#EJERCICIO 2
num=int(input("INGRESE UN VALOR: "))
if num > 1:
    cont = 0
    for i in range(2, num):
        resto=num%i
        if resto==0:
            cont+=1
    if cont==0:
        print("EL NUMERO: " +str(num)+"ES PRIMO")
    else :
            print("EL NUMERO: "  +str(num)+ "NO ES PRIMO")

    


