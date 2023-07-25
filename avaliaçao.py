import os

#define o N, número inteiro positivo
N = int(input("Insira um número:"))

#define a lista dos números
for i in range(1,N+1):  
    #define que se o número for divisível por 3 e 5 fará uma ação
    if i % 3==0 and i % 5==0:
        #executa a ação se o comando anterior for verdadeiro
        print("SenaiJundiai")   
    #também compara se o número é divisível por 3
    elif i % 3==0:
        print("Senai")
    #também compara se o número é divisível por 5
    elif i % 5==0:
        print("Jgtundiai")
    #se o número não for divisível por nenhum desses aparecerá em forma normal
    else:
        print (i)

os.system ("pause")
  