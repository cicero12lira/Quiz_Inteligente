def nome():
    print("\nOlá!! Sejá muito bem vindo ao quiz feito em Python!")
    print("Como gostaria de ser chamado? \n")
    global meu_nome
    meu_nome = input("Nome: ")

    print(meu_nome, '''a seguir você responderar a quatro questões, para se dá bem acerte no minímo três questões. Ok? :\n
    ''')

    print("Sem enrrolação vamos começar...\n")
    pergunta1()

def refazer():
    print("\nEntão bora ",meu_nome, "\n")
    pergunta1()

    
def pergunta1():
    print ('''Questão 1:
                Um pedreiro diz: "Se eu tivesse dois tijolos a mais,
                o dobro deste número seria 100". Quantos tijolos ele tem?
                
                a)  50
                b)  52
                c)  44
                d)  42
                e)  48'''
                )
    resposta01()
def resposta01():                
    resposta = input("Sua resposta: ")
    while True:
        if resposta != "a" and resposta != "b" and resposta != "c" and resposta != "d" and resposta != "e":
            print("Escola entre as opções a, b, c, d, e")
            resposta01()
            
        else:
            if resposta == "e":
                print("VOCÊ ACERTOU!!\n")
                global pontuacao
                pontuacao = 2
                pergunta2()
            else:
                print ("VOCÊ ERROU!")
                pontuacao = 0
                pergunta2()
                
def pergunta2():
    print('''Questão 2:
                Pedro tem 6 bolas de gude a mais do que Jorge. Os dois juntos têm 54. Quanto tem cada um?
                a)  30 e 24
                b)  24 e 26
                c)  28 e 26
                d)  32 e 22
                e)  34 e 20''')
    resposta02()

def resposta02():
    resposta = input("Sua resposta: ")
    while True:
        if resposta != "a" and resposta != "b" and resposta != "c" and resposta != "d" and resposta != "e":
            print("Escola entre as opções a, b, c, d, e")
            resposta02()
            
        else:
            if resposta == "a":
                print("VOCÊ ACERTOU!!\n")
                global pontuacao
                pontuacao = pontuacao + 2
                pergunta3()
            else:
                print ("VOCÊ ERROU!")
                pergunta3()
    
def pergunta3():
    print ('''Questão 3:
                Se seis latas de leite custam 72 reais, qual o preço de 9 latas?
                a)  87 reais
                b)  115 reais
                c)  108 reais
                d)  100 reais
                e)  90 reais''')
    resposta03()
    
def resposta03():
    resposta = input("Sua resposta: ")
    while True:
        if resposta != "a" and resposta != "b" and resposta != "c" and resposta != "d" and resposta != "e":
            print("Escola entre as opções a, b, c, d, e")
            resposta03()
            
        else:
            if resposta == "c":
                print("VOCÊ ACERTOU!!\n")
                global pontuacao
                pontuacao = pontuacao + 2
                pergunta4()
            else:
                print ("VOCÊ ERROU!")
                pergunta4()
    
def pergunta4():
    print ('''Questão 4:
                Num elevador que suporta 600 quilos, quantas caixas de 48 quilos, pode-se levar por vez?
                a)  13
                b)  11
                c)  10
                d)  15
                e)  12''')
    resposta04()
    
def resposta04():
    resposta = input("Sua resposta: ")
    while True:
        if resposta != "a" and resposta != "b" and resposta != "c" and resposta != "d" and resposta != "e":
            print("Escola entre as opções a, b, c, d, e")
            resposta04()
            
        else:
            if resposta == "e":
                print("VOCÊ ACERTOU!!\n")
                global pontuacao
                pontuacao = pontuacao + 2
                pergunta05()
            else:
                print ("VOCÊ ERROU!")
                pergunta05()

def pergunta05():
    print ('''Questão 5:
                O termometro subiu 6 graus, e isso representa a metade da temperatura de antes. A quantos graus está agora?
                a)  16 graus
                b)  18 graus
                c)  12 graus
                d)  24 graus
                e)  22 graus''')
    resposta05()
                    
def resposta05():
    resposta = input("Sua resposta: ")
    while True:
        if resposta != "a" and resposta != "b" and resposta != "c" and resposta != "d" and resposta != "e":
            print("Escola entre as opções a, b, c, d, e")
            resposta05()
            
        else:
            if resposta == "b":
                print("VOCÊ ACERTOU!!\n")
                global pontuacao
                pontuacao = pontuacao + 2
                print("FIM DO QUIZ!\n")
                total()
            else:
                print ("VOCÊ ERROU!\n")
                print("FIM DO QUIZ!\n")
                total()


def total():
    global pontuacao
    if pontuacao > 5:
        print("PARABENS VOCÊ PASSOU NO QUIZ INTELIGENTE!")
        print("Sua pontuação foi: ",pontuacao)
        print("Deseja refazer o quiz inteligente? s/n")
        deseja_refazer()
    else:
            print("Não foi dessa vez!")
            print("Sua pontuação foi ",pontuacao," para passar nesse quiz você deve atingir no minimo 6")
            continuar = input('Deseja refezer o quiz s/n: ')
            while True:
                if continuar != "n" and continuar != "s":
                    print("Você deve escolher entre 's' ou 'n'")
                    deseja_refazer()
                else:
                    if continuar == 's':
                        refazer()  
                    else:
                        print("OBRIGADO POR PARTICIPAR DO QUIZ INTELIGENTE!\n")
                        encerrar_o_programa()
def deseja_refazer():
    repetir = input("_")
    while True:
        if repetir != "n" and repetir != "s":
            print("Você deve escolher entre 's' ou 'n'")
            deseja_refazer()
        else:
            if repetir == 's':
                refazer()  
            else:
                print("OBRIGADO POR PARTICIPAR DO QUIZ INTELIGENTE!\n")
                encerrar_o_programa()
        
                    
def encerrar_o_programa():
    quit()


nome()
   
       

    

    

    

    