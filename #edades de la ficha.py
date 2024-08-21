#promedio de las edades de los aprendices

edad = 17
cantidad = 18
promedio = float()

print ("cantidad de los aprendices: ", cantidad)
for i in range (1, cantidad):
    print ("Ingresa la edad de los aprendices: ", edad)
    
    promedio = promedio + edad 
    
promedio = promedio/cantidad
print ("El promedio es: ", promedio)
    