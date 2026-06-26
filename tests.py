
lista_numeros = []
bandera = True
cont = 0

for i in range(0, 2):
    numero = int(input('ingrese un numero: '))
    lista_numeros.append(numero)
    
opcion = str(input('desea seguir agregando numeros? (Y/N): '))

if opcion == 'Y':
    while bandera == True:
        numero = int(input('ingrese un numero: '))
        lista_numeros.append(numero)
        op = str(input('desea seguir agregando numeros? (Y/N): '))
        if op == 'N':
            bandera = False
    

total = restar(lista_numeros)

print(total)
        
