# Comment one line
'''
    Author: Valentina
    Date: 20/01/2023
'''
print("Hello from main.py")

#Initialize variables 
user_name = "Valentina"
age = 17
gender = "F"
is_active = True
height= 1.72
pets = [" ", " "]

#Conditionals
if age > 17:
    print('Es mayor de edad')
else: 
    print('Es menor de edad')
# ---------------------------------
if gender == 'f' or gender == 'f':
    print('Femenino')
elif gender == 'M' or gender == 'm':
    print('Masculino')
elif gender =='NB' or gender == 'nb':
    print('No binario')
elif gender == 'SE' or gender == 'se':
    print('Sin especificar')
else:
    print('>>> Opcion invalida <<<')

'''
    Funciones con texto: lower() upper() capitalize()
    lower(): Convierte todo el texto en minuscula
    upper(): Convierte todo el tecto en mayuscula
    capitalize(): Primer caracter en mayusc y el resto en minusc 
'''
print (user_name)
print(user_name.lower())
print (user_name.upper())
print (user_name.capitalize())

#-------------Code implements upper() function
if gender.upper() == 'F':
    print('Femenino')
elif gender.upper() == 'M':
    print('Masculino')
elif gender.upper() == 'NB':
    print('No binario')
elif gender.upper() == 'SE':
    print('Sin especificar')
else:
    print('>>> Opción inválida <<<')

# Show list content
print (pets)

# Show list content. Use the function len(lista)
print (len(pets))

#Interpolacion de mensajes 
print (f'{user_name} tiene {age} años')

#Show content of specific index in list
print(pets[0])
print(pets[1])

#---------------For cicle ----------
#Iterar 10 veces
for i in range(0, 10):
    print(i)

for i in range(10):
    print(i)

for i in range(1, 11):
    print(i)

#---------------While------------
#Iterar 10 veces 
print(' -------------------------- ')
counter = 0
while counter < 10:
    print(counter)
    counter += 1