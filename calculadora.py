#declaração das função 
def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

def calculadora():
    operacao = input("Escolha a operação a ser executada (+, -, *, /): ")
    num1 = float(input("Informe o primeiro número: "))
    num2 = float(input("Informe o segundo número: "))

    if operacao == "+":
        resultado = adicao(num1, num2)
        print("O resultado da adição é:", resultado)
    elif operacao == "-":
        resultado = subtracao(num1, num2)
        print("O resultado da subtração é:", resultado)
    elif operacao == "*":
        resultado = multiplicacao(num1, num2)
        print("O resultado da multiplicação é:", resultado)
    elif operacao == "/":
        resultado = divisao(num1, num2)
        print("O resultado da divisão é:", resultado)
    else:
        print("Atenção! Operação inválida.")

calculadora()

