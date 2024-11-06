
from funcs import criar_conta
from funcs import entrar

contas_no_sistema = {}

# Boas-vindas ao sistema
print("\n🌟 Bem-vindo ao Sistema de Contas!")
print("Aqui você pode criar uma nova conta ou acessar sua conta existente de forma fácil e segura.")
print("Vamos começar? Escolha uma das opções abaixo:\n")

flag = True

while flag:
    
    def conta():
        print('\n\t1. Criar uma nova conta')
        print('\t2. Fazer login')
        print('\t3. Sair do sistema')
        
        validador = False

        while not validador:
            caminho = input('\nEscolha uma opção (1, 2, 3): ')
            opcoes_validas = {'1', '2', '3'}
            validador = validador_entrada(opcoes_validas, caminho)
        
        if caminho == '1':
            print('\n\t🔑 Criando uma nova conta...')
            criar_conta(contas_no_sistema)
        elif caminho == '2':
            print('\n\t🔓 Entrando na sua conta...')
            entrar(contas_no_sistema)
        elif caminho == '3':
            print('\n👋 Saindo... Até logo!')
            global flag
            flag = False
            return  
            

    
    def validador_entrada(opcoes_validas, entrada):
        if entrada not in opcoes_validas:
            print('\n⚠️ Opção inválida! Por favor, escolha uma opção entre 1 e 2.\n')
            return False
        else:
            return True
        
    conta()
