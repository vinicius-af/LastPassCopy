from random import choice
import string

#função que confere se o arquivo existe
def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False 
    else:
        return True

#função que cria o arquivo
def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print('Arquivo criado com sucesso!')

#função que lê o arquivo
def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo!')
    else: 
        print(a.read())
    finally:
        a.close()

#função que cadastra novas senhas
def criarsenha(nome, usuario='desconhecido', senha='nula'):
    try:
        a = open(nome, 'at')
    except:
        print('Houve um erro no cadastro!')
    else:
        try:
            a.write(f'| User:{usuario} |........| Senha:{senha} |\n')
        except:
            print('Houve um erro na hora de escrever os dados!')
        else:
            print(f'Novo registro do usuário {usuario} adicionado')
            a.close()


arq = 'senhas.txt'

#analisa se o arquivo existe ou precisa ser criado
if arquivoexiste(arq):
    print('Arquivo encontrado com sucesso!')
else:   
    criararquivo(arq)

#sistema principal
while True:
    print('O que deseja fazer?')
    print('[1]Ver meus usuários:')
    print('[2]Cadastrar um novo usuário')
    print('[3]Gerar uma senha')
    choose = int(input('Digite aqui:'))
    if choose == 1:
        lerarquivo(arq)
    elif choose == 2:
        usuario = str(input('Defina o nome de usuário para o cadastro: '))
        dcas = str(input('Deseja gerar uma senha para o usuário?[s/n]: '))
        #gera a senha
        if dcas == 's':
            LMM = ''
            LMD = ''
            LNM = ''
            LMS = ''
            senha1 = ''

            #cores
            vermelho = '\033[1;31m'
            verde = '\033[1;32m'
            negrito = '\033[;1m'

            while True: 
                tamanho = int(input(f'{negrito}Digite o tamanho da sua senha(máximo de 99 caracteres):{negrito} '))
                if tamanho > 99:
                    print(f'{vermelho}Digite um número válido!{vermelho}')
                elif tamanho <= 0:
                    print(f'{vermelho}Digite um número válido!{vermelho}')
                else:
                    break   
            while True:
                MsL = (input(f'{negrito}Letras maiúsculas?(s/n):{negrito} '))
                if MsL == 's':
                    LMD += string.ascii_uppercase
                    break
                elif MsL == 'n':
                    LNM == None
                    break
                else:
                    print(f'{vermelho}Resposta inválida{vermelho}')
            while True:
                msL = (input(f'{negrito}Letras minúsculas?(s/n):{negrito} '))
                if msL == 's':
                    LMM += string.ascii_lowercase
                    break
                elif msL == 'n':
                    LNM == None
                    break
                else:
                    print(f'{vermelho}Resposta inválida{vermelho}')
            while True:
                nmL = (input(f'{negrito}Números?(s/n):{negrito} '))
                if nmL == 's':
                    LNM += string.digits
                    break
                elif nmL == 'n':
                    LNM == None
                    break
                else:
                    print(f'{vermelho}Resposta inválida{vermelho}')
            while True:
                nms = (input(f'{negrito}Símbolos?(s/n):{negrito} '))
                if nms == 's':
                    LMS += string.punctuation
                    break
                elif nmL == 'n':
                    LMS == None
                    break
                else:
                    print(f'{vermelho}Resposta inválida{vermelho}')

            valores = LNM + LMM + LMD + LMS
            for i in range(tamanho):
                senha1 += choice(valores)

            senha = senha1
        else:
            senha = str(input('Digite sua senha:')) 

        criarsenha(arq, usuario, senha)   
    elif choose == 3:
        LMM = ''
        LMD = ''
        LNM = ''
        LMS = ''
        senha = ''

        #cores
        vermelho = '\033[1;31m'
        verde = '\033[1;32m'
        negrito = '\033[;1m'

        while True: 
            tamanho = int(input(f'{negrito}Digite o tamanho da sua senha(máximo de 99 caracteres):{negrito} '))
            if tamanho > 99:
                print(f'{vermelho}Digite um número válido!{vermelho}')
            elif tamanho <= 0:
                print(f'{vermelho}Digite um número válido!{vermelho}')
            else:
                break   
        while True:
            MsL = (input(f'{negrito}Letras maiúsculas?(s/n):{negrito} '))
            if MsL == 's':
                LMD += string.ascii_uppercase
                break
            elif MsL == 'n':
                LNM == None
                break
            else:
                print(f'{vermelho}Resposta inválida{vermelho}')
        while True:
            msL = (input(f'{negrito}Letras minúsculas?(s/n):{negrito} '))
            if msL == 's':
                LMM += string.ascii_lowercase
                break
            elif msL == 'n':
                LNM == None
                break
            else:
                print(f'{vermelho}Resposta inválida{vermelho}')
        while True:
            nmL = (input(f'{negrito}Números?(s/n):{negrito} '))
            if nmL == 's':
                LNM += string.digits
                break
            elif nmL == 'n':
                LNM == None
                break
            else:
                print(f'{vermelho}Resposta inválida{vermelho}')
        while True:
            nms = (input(f'{negrito}Símbolos?(s/n):{negrito} '))
            if nms == 's':
                LMS += string.punctuation
                break
            elif nmL == 'n':
                LMS == None
                break
            else:
                print(f'{vermelho}Resposta inválida{vermelho}')

        valores = LNM + LMM + LMD + LMS
        for i in range(tamanho):
            senha += choice(valores)
        dsj = str(input('Deseja cadastrar essa senha com um usuário?[s/n]: '))
        if dsj == 's':
            usuario = str(input('Digite o usuário que deseja realizar o cadastro: '))
            criarsenha(arq, usuario, senha)
        elif dsj == 'n':
            print('OK! Sua senha foi gerada!')
            print(senha)
        else:
            print('Resposta inválida!')
