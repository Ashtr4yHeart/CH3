numero = 1
#Bucle While como en el diagrama Rombo
while numero < 50:
      #Estructuras de control condicional
    if numero % 15 == 0:
       print("FizzBUzz")
    elif numero % 3 == 0:
       print("Fizz")
    elif numero % 5 == 0:
       print("Buzz")
    else:
       print(numero)
    numero += 1 #Incrementar el número para evitar un bucle infinito
#Fin del bucle While
