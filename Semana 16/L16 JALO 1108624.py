print("Semana No. 16: Ejercicio 1\n")
import random
arreglo=[]
def LlenarVector(arreglo):
    for i in range(10):
        r=random.randint(1,100)
        arreglo.append(r)
    return arreglo
def Promedio(arreglo):
    sumatoria=0
    for valor in arreglo:
        sumatoria+=valor
    promedio=sumatoria/len(arreglo)
    return promedio
def ParesImpares(arreglo):
    sumapar=0
    sumaimpar=0
    for i in range(len(arreglo)):
        if i%2==0:
            sumapar+=arreglo[i]
        else:
            sumaimpar+=arreglo[i]
    print("Su suma de pares son", sumapar)
    print("Su suma de impares son", sumaimpar)
def ContarParImpar(matriz):
    par=0
    impar=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]%2==0:
                par+=1
            else:
                impar+=1
    print("La cantidad de números pares es", par)
    print("La cantidad de números impares", impar)
def NumeroMayorMenor(matriz):
    mayor=matriz[0][0]
    menor=matriz[0][0]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]>mayor:
                mayor=matriz[i][j]
            elif matriz[i][j]<menor:
                menor=matriz[i][j]
    print("su numero mayor es ", mayor)
    print("su numero menor es", menor)
LlenarVector(arreglo)
print(arreglo)
print("Su promedio es: ", Promedio(arreglo))
print("La longitud de su arreglo es: ", len(arreglo))
ParesImpares(arreglo)
#Ejercicio2
print("\nSemana 16: Ejercicio 2\n")
filas=int(input("Ingrese la cantidad de filas: "))
columnas=int(input("Ingrese la cantidad de columnas "))
matriz=[]
for i in range(filas):
    temp=[]
    for j in range(columnas):
        r=random.randint(1,1001)
        temp.append(r)
    matriz.append(temp)
print(matriz)
ContarParImpar(matriz)
NumeroMayorMenor(matriz)

        


