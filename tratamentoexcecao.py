#Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
#A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

#Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.

def calcular_idade():
    while True:
        nome = input("Informe o nome completo do usuário: ")
        try:
            ano_nasc = int(input("Informe o ano de nascimento do usuário (entre 1922 e 2021): "))
            if 1922 <= ano_nasc <= 2021:
                idade = 2022 - ano_nasc
                print(f"O usuário: {nome}, completou ou completará {idade} anos em 2022.")
                break
            else:
                print("Atenção! Digite um número entre 1922 e 2021.")
        except ValueError:
            print("Ops! Entrada inválida. Para o ano de nascimento informe números.")

calcular_idade()