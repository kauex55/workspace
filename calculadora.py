# define as funções para as operações
def soma(num1, num2):
    return num1 + num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    return num1 / num2

# solicita que o usuário escolha a operação
operacao = input("Qual operação você deseja realizar? (+, *, /): ")

# solicita que o usuário insira os números para a operação
numero1 = float(input("Insira o primeiro número: "))
numero2 = float(input("Insira o segundo número: "))

# realiza a operação selecionada e imprime o resultado
if operacao == '+':
    print(numero1, "+", numero2, "=", soma(numero1, numero2))

elif operacao == '*':
    print(numero1, "*", numero2, "=", multiplicacao(numero1, numero2))

elif operacao == '/':
    print(numero1, "/", numero2, "=", divisao(numero1, numero2))

else:
    print("Opção inválida!")            