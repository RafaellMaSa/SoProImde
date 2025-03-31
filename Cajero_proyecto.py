
saldo = 0  

while True :
    print ("1. Deposito")
    print ('2. Retiro')
    print ('3. Salir')
    opcion = input("Seleccione la transaccion que desea realizar ")

    match opcion: 
        case '1':
            deposito = float(input("Digite el monto que desea depositar "))
            if deposito == 0:
                print ("El monto a depositar debe ser mayor a 0")
            else:
                saldo += deposito
                print ('Saldo actual:', saldo) 
        case '2':
            retiro = float(input('Digite el monto que desea retirar'))
            if retiro == 0:
                print ('El monto a retirar debe ser mayor a cero')
            elif retiro > saldo:
                print ('No hay suficientes fondos') 
            else : 
                saldo -= retiro
                print ('Saldo actual: ', saldo)
        case '3': 
            break
    salida = input('Si desea continuar digite "O", de lo contrario digite "X"').upper()
    if salida == 'X': 
        break
print ('Su saldo final es de: ', saldo)

    
