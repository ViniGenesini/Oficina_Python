''' 
EXERCÍCIO 6
Desenvolva um programa que leia o primeiro termo e a
razão de uma PA.No final, mostre os 10 primeiros termos
dessa progressão. Lendo o primeiro termo e a razão de
uma  PA, mostrandoos 10 primeiros termos da progressão 
usando a estrutura while. Perguntepara o usuário se ele
quer mostrar mais alguns termos. O programa encerra quando
ele disser que quer mostrar 0 termos.

'''

try:
    print("*** PROGRESSÃO ARTIMÉTICA ***\n")
    termo = float(input("Digite o 1º termo da PA: "))
    razao = float(input("Digite a razão da PA: "))
    i=0
    print("\n*** RESULTADO ***\n")
    while(i<10):
        print("{}º termo: ".format(i+1),termo)
        termo = termo + razao
        i+=1
    print("\n*** CONTINUAR? ***\n")
    resposta = int(input("- Para imprimir mais termos da PA, digite o número de termos desejados á mais.\n- Para encerrar o programa, digite 0.\n\nRESPOSTA: "))
    if(resposta==0):
        print("\n*** PROGRAMA ENCERRADO! ***")
    else:
        while(resposta>=1):
            while(i<10+resposta):
                print("{}º termo: ".format(i+1),termo)
                termo = termo + razao
                i+=1
        resposta2 = int(input("\n- Para imprimir mais termos da PA, digite o número de termos desejados á mais.\n- Para encerrar o programa, digite 0.\n\nRESPOSTA: "))
        if(resposta2==0):
            resposta = 0
            print("\n*** PROGRAMA ENCERRADO! ***")
        else:
            resposta = resposta + resposta2
except:
    print("\n*** VALOR INVÁLIDO: APENAS NÚMEROS! ***")
