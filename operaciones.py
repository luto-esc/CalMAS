#recibe una lista de numeros los suma y devuelve el valor
def sumar(lista_num):
    total = 0
    #recorre la lista
    for n in lista_num:
        #suma cada numero a un acumulador
        total = total + n
    
    return total

#
def restar(lista_num):
    total = 0

    for n in lista_num:
        
        total = total - n

    return total