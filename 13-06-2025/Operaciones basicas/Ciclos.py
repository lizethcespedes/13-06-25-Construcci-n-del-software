#Ciclo white
contador = 0
while contador < 5:
    print(contador)
    contador += 1
#Ciclo For
frutas = ["pera", "mango", "mandarina"]
for fruta in frutas:
    print(fruta)
#Condicional if
x = 5
y = 10
if x > 3 and y < 12:
    print("Ambas condiciones son verdaderas.")
#Condicional else
grado = 8
if grado <= 8:
    print("Aun estas en secundaria.")
else:
    print("Ya estas en bachillerato")

#Condicional elif
edad = 24
if edad >= 18:
    print("Eres mayor de edad.")
elif edad < 18:
    print("Eres menor de edad.")
else:
    print("Edad no válida.")