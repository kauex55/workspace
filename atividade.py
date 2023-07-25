import os

a = (input("Digite o primeiro número: "))
b = (input("Digite o segundo número: "))
c = (input("Digite o terceiro número: "))
d = (input("Digite o quarto número: "))
e = (input("Digite o quinto número: "))

números = [a,b,c,d,e]
números.sort()
print(f"A mediana dos valores {números} é {números[2]}")

os.system("pause")