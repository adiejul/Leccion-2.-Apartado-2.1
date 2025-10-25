a= int(input("Introduce el primer número "))
b= int(input("Introduce el segundo número "))

suma= a + b
resta= a - b
multiplicacion= a * b
division= a / b
divEnt= a//b
resto= a%b
potencia= a**b

print("la suma de ", a, "+", b, "es", suma)
print("la resta de ", a, "-", b, "es", resta)
print("la multiplicacion de ", a, "x", b, "es", multiplicacion)
print("la división de ", a, "/", b, "es", division)
print("la division sin decimales de ", a, "/", b, "es", divEnt)
print("el resto de ", a, "y", b, "es", resto)
print("la potencia de ", a, "^", b, "es", potencia)