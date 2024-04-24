print("Semana No. 12: Ejercicio 1")
print("a. Sumatoria")
print("b. Factorial")
print("c. Tablas de multiplicar")
print("d. Número perfecto")
print()
opcion=input("Elija una opcion del menú para realizar: ")
match(opcion):
    case "a":
        N=0
        while N<=0:
            N=int(input("Ingrese un número N mayor que 0 "))
            if N<=0:
                print("El número ingresado debe ser mayor a 0 ") 
        sumatoria=0
        for cont in range(1, N+1):
            sumatoria+=cont
        print("La sumatoria es: ", sumatoria)
    case "b":
        while N<=0:
            N=int(input("Ingrese un número N mayor que 0 "))
            if N<=0:
                print("El número ingresado debe ser mayor a 0 ") 
        factorial=1
        for cont in range(1,N+1):
            factorial*=cont
        print("El factorial del numero N es: ", factorial)
    case "c":
        for i in range(1, 10):
            for j in range(1,11):
                print(i*j, "\t", end='')
            print()
    case "d":
        while N<=0:
            N=int(input("Ingrese un número N mayor que 0 "))
            if N<=0:
                print("El número ingresado debe ser mayor a 0 ")
        acumulador=0
        for factor in range(1, N):
            if N%factor==0:
                acumulador+=factor
        if N==acumulador:
            print("Su número es perfecto")
        else:
            print("Su número no es perfecto")
    case _:
        print("Eliga una opcion valida")