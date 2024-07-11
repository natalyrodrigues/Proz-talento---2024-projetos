#Precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.

#Escreva um código que imprima todos os números exceto o número 13.
#Escreva mais dois códigos que resolvam o mesmo problema, mas dessa vez usando os outros dois tipos de #laços de repetição aprendidos.

#Como desafio, imprima eles em ordem decrescente (20, 19, 18...).


#Ultilizando o laço de repetição for

print("Ultilizando o for: ")
for i in range(1,21):
    if i != 13:
        print(i)
        if i == 20:
            print("--------------")
        
#Laço de repetição While
i = 1

print("Usando While: ")
while i <= 20:
    if i != 13:
        print(i)
    i += 1
print("-----------------")   

#Ordem decrescente Range 
print("Usando Range em ordem decrescente: ")
for i in range(20, 0, -1):
    if i != 13:
        print(i)
print("-----------------")
        
#Randint (mostra numeros aleatorios)
import random 

print("Mostra números aleatórios com randint: ")
for i in range(20):
    i = random.randint(1,20)
    while i == 13:
        i = random.randint(1,20)
    print(i)