#Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:

#1: Soma
#2: Subtração
#3: Multiplicação
#4: Divisão
#0: Sair

#Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

#Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa executar a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar.

#É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado. 


def calculadora():
    operacoes = {
        1: lambda x, y: x + y,
        2: lambda x, y: x - y,
        3: lambda x, y: x * y,
        4: lambda x, y: x / y if y != 0 else None
    }

    while True:
        print("---Calculadora---")
        print(">>> MENU <<<")
        print("Escolha o número correspondente a operação matemática: ")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        try:
            opc = int(input("Informe o número da opção: "))
            if opc not in range(0, 5):
                print("Atenção! Número informado não é válido.")
                continue

            if opc == 0:
                print("Operação encerrada...")
                break

            num1 = float(input("Informe o primeiro número: "))
            num2 = float(input("Informe o segundo número: "))

            resultado = operacoes[opc](num1, num2)
            if resultado is None:
                print("Ops! Divisão por zero, negada.")
            else:
                print(f"Resultado da operação {list(operacoes.keys())[opc-1]} é: {resultado}")

        except ValueError:
            print("Atenção! Informe apenas números.")

calculadora()