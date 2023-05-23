a = 10
b = 20

if (a > b) :
  maior = a

else:
  maior = b

print('O maior número é :', maior)

numero = 40

if (numero % 2 == 0):
  print('este númeor é par', numero)

else : 
  print('este número é ímpar', numero)

# if <condição 1>:
   # Bloco de código que será executado caso condição seja True
 # elif <condição 2>:
  # Bloco de código que será executado caso condição 1 seja False e condição 2 seja True
 # else:
   # Bloco de código que será executado caso condição 1 seja False e condição 2 seja False
# Instrução fora do if 

s = 0
for i in range(5):
  s += 3*i
print(s)

s = 0
a = 1
while s < 5:
  s = 3*a
  a += 1
print(s)

print('Olá mundo!')