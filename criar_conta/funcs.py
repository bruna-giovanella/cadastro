
import pwinput
import re


def criar_conta(contas_no_sistema):
    conta = {}

    erro = True
    while erro:
        email = input('Digite o seu e-mail: ')
        if validador_email(email):
            erro = False
        else:
            print('\n⚠️ E-mail inválido! Por favor, insira um e-mail válido.')

    erro = True
    while erro:
        password = pwinput.pwinput(prompt = 'Crie uma senha segura: ')
        strong_password = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[\W_]).+$'
        
        caracteres = len(password)

        while not re.match(strong_password, password) and caracteres < 8:
            print('\n⚠️ Senha fraca! A senha deve conter:\n\t- Pelo menos uma letra maiúscula\n\t- Pelo menos uma letra minúscula\n\t- Pelo menos um caractere especial\n\t- No mínimo 8 caracteres')
            password = pwinput.pwinput(prompt = 'Crie uma senha segura: ')

        if passwordVerificator(password):
            conta['senha'] = password
            erro = False

    contas_no_sistema[email] = conta
    print('\nConta criada com sucesso! 🎉\n')     
            


def validador_email(email):
    return '@' in email and '.' in email.split('@')[-1] 



def passwordVerificator(password):
    passwordConfirm = pwinput.pwinput(prompt = 'Confirme sua senha: ')

    while password != passwordConfirm:
        print('\n⚠️ As senhas não coincidem! Por favor, tente novamente.')
        passwordConfirm = pwinput.pwinput(prompt = 'Confirme sua senha: ')
    print('\n✔️ Senha confirmada com sucesso!')

    return True



def entrar(contas_no_sistema):

    erro = True
    while erro:
        email = input('E-mail de login: ')
        if validador_email(email):
            erro = False
        else:
            print('\n⚠️ E-mail inválido! Por favor, insira um e-mail válido.')

    if email in contas_no_sistema:
        password = pwinput.pwinput(prompt = 'Digite sua senha: ')

        while password != contas_no_sistema[email]['senha']:
            print('\n⚠️ Senha incorreta. Tente novamente.')
            password = pwinput.pwinput(prompt = 'Digite sua senha: ')

        print('\n✔️ Bem-vindo à sua conta! 🎉')
    
    else:
        print('\nEmail nao cadastrado! Insira um e-mail válido ou cadastre um novo e-mail')
    
