
import pwinput
import re

###################

# 1. CRIAR CONTA


def criar_conta(contas_no_sistema):
    conta = {}

    erro = True
    count = 0
    while erro:
        email = input('Digite o seu e-mail: ').lower()
        if validador_email(email):
            erro = False
        else:
            count += 1
            if count == 3:
                print('\n\t🚨 Você excedeu o limite de tentativas\n\tVoltando ao menu...')
                return
            
            print('\n⚠️ E-mail inválido! Por favor, insira um e-mail válido.')


    erro = True
    while erro:
        password = pwinput.pwinput(prompt = 'Crie uma senha segura: ')
        strong_password = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[\W_]).{8,}$'

        # caracteres = len(password)
        count = 0
        while not re.match(strong_password, password):      #and caracteres < 8:
            print('\n⚠️ Senha fraca! A senha deve conter:\n\t- Pelo menos uma letra maiúscula\n\t- Pelo menos uma letra minúscula\n\t- Pelo menos um caractere especial\n\t- No mínimo 8 caracteres')
            password = pwinput.pwinput(prompt = 'Crie uma senha segura: ')
            count += 1
            if count == 3:
                print('\n\t🚨 Você excedeu o limite de tentativas\n\tVoltando ao menu...')
                return

        if passwordVerificator(password):
            conta['senha'] = password
            erro = False
        
        else:
            return

    contas_no_sistema[email] = conta
    print('\nConta criada com sucesso! 🎉\n')        
            



###################

# 1.1. VALIDAR EMAIL


def validador_email(email):
    return '@' in email and '.' in email.split('@')[-1] 




###################

# 1.2. VALIDAR SENHA


def passwordVerificator(password):
    passwordConfirm = pwinput.pwinput(prompt = 'Confirme sua senha: ')

    count = 0
    while password != passwordConfirm:
        print('\n⚠️ As senhas não coincidem! Por favor, tente novamente.')
        passwordConfirm = pwinput.pwinput(prompt = 'Confirme sua senha: ')
        count += 1
        if count == 3:
            print('\n\t🚨 Você excedeu o limite de tentativas\n\tVoltando ao menu...')
            return 
    print('\n✔️  Senha confirmada com sucesso!')

    return True




###################

# 2.1 VALIDAR ENTRADA


def validador_entrada(opcoes_validas, entrada):
        if entrada not in opcoes_validas:
            print('\n⚠️ Opção inválida! Por favor, escolha uma das opões fornecidas\n')
            return False
        else:
            return True




###################

# 2. ENTRAR


def entrar(contas_no_sistema):

    erro = True
    count = 0
    while erro:
        
        email = input('E-mail de login: ').lower()
        if validador_email(email):
            erro = False
        else:
            count += 1
            if count == 4:
                print('\n\t🚨 Você excedeu o limite de tentativas\n\tVoltando ao menu...')
                return
            
            print('\n⚠️ E-mail inválido! Por favor, insira um e-mail válido.')
            


    if email in contas_no_sistema:
        password = pwinput.pwinput(prompt = 'Digite sua senha: ')

        count = 0
        while password != contas_no_sistema[email]['senha']:
            print('\n⚠️ Senha incorreta. Tente novamente.')
            password = pwinput.pwinput(prompt = 'Digite sua senha: ')
            count += 1

            if count == 3:
                validador = False

                count = 0
                while not validador:
                    decisao = input('Deseja recuperar sua senha? (s/n): ').lower()
                    opcoes = {'s', 'n'}
                    validador = validador_entrada(opcoes, decisao)
                    count += 1
                    if count == 3:
                        print('\n\t🚨 Você excedeu o limite de tentativas\n\tVoltando ao menu...')
                        return


                if decisao == 's':
                    recuperar_senha(contas_no_sistema)
                    return 
                else:
                    return 


        print('\n✔️ Bem-vindo à sua conta! 🎉')
    
    else:
        print('\n🚨 Email nao cadastrado! Insira um e-mail válido ou cadastre um novo e-mail')




###################

# 3. RECUPERAR SENHA


def recuperar_senha(contas_no_sistema):
    erro = True
    count = 0
    while erro:
        email = input('E-mail de login: ').lower()
        if validador_email(email):
            erro = False
        else:
            print('\n⚠️ E-mail inválido! Por favor, insira um e-mail válido.')
            count+=1
            if count == 3:
                print('\n\t🚨 Você excedeu o limite de tentativas\n\tVoltando ao menu...')
                return

    count = 0
    while email not in contas_no_sistema:
        print('\nEmail nao cadastrado! Insira um e-mail válido')
        email = input('E-mail de login: ').lower()
        count+=1
        if count == 3:
            print('\n\t🚨 Você excedeu o limite de tentativas\n\tVoltando ao menu...')
            return


    erro = True
    while erro:
        password = pwinput.pwinput(prompt = 'Nova senha: ')
        strong_password = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[\W_]).+$'

        caracteres = len(password)

        count = 0
        while not re.match(strong_password, password) and caracteres < 8:
            print('\n⚠️ Senha fraca! A senha deve conter:\n\t- Pelo menos uma letra maiúscula\n\t- Pelo menos uma letra minúscula\n\t- Pelo menos um caractere especial\n\t- No mínimo 8 caracteres')
            password = pwinput.pwinput(prompt = 'Crie uma nova senha segura: ')

            count += 1
            if count == 3:
                print('\n\t🚨 Você excedeu o limite de tentativas\n\tVoltando ao menu...')
                return


        if passwordVerificator(password):
            contas_no_sistema[email]['senha'] = password
            erro = False
