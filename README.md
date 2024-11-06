# Sistema de Contas - 📧🔑

Bem-vindo ao **Sistema de Contas**, uma aplicação simples para criação e login em contas de usuários. Este sistema permite que você crie uma nova conta, faça login na sua conta existente ou saia do sistema. 

### Tecnologias Utilizadas
- **Python**: A linguagem de programação utilizada para criar o sistema.
- **pwinput**: Biblioteca utilizada para entrada segura de senhas (evita que as senhas sejam visíveis ao digitar).

### Características
- **Criação de Conta**: Crie uma conta fornecendo um e-mail válido e uma senha segura.
- **Login**: Faça login com seu e-mail e senha.
- **Sair**: Encerre o sistema a qualquer momento.

### Funcionalidades 🎮

- **Criar uma Conta**: Você pode criar uma nova conta fornecendo um e-mail válido e uma senha que atenda aos seguintes requisitos:
  - Pelo menos uma letra maiúscula.
  - Pelo menos uma letra minúscula.
  - Pelo menos um caractere especial (ex: `@`, `#`, `!`, etc.).
  
- **Fazer Login**: Depois de criar sua conta, você pode acessar o sistema fazendo login com o seu e-mail e senha.

- **Sair do Sistema**: Caso queira sair, basta selecionar a opção "Sair" e o sistema será encerrado.

### Como Usar 🚀

1. **Rodando o Sistema**:
   - O sistema começa com uma mensagem de boas-vindas.
   - Você será apresentado com três opções: 
     1. Criar uma nova conta
     2. Fazer login
     3. Sair do sistema
     
2. **Criar Conta**:
   - Quando você escolher a opção para criar uma conta, será solicitado o e-mail e a senha.
   - A senha deve ser forte (contendo pelo menos uma letra maiúscula, uma minúscula e um caractere especial).
   - Após isso, você precisará confirmar a senha.

3. **Login**:
   - Se você já tem uma conta, pode fazer login fornecendo o e-mail e a senha.
   - Se o login for bem-sucedido, o sistema dará as boas-vindas!

4. **Sair**:
   - Para sair do sistema, basta escolher a opção "Sair" e o sistema será encerrado com uma mensagem de despedida.

### Estrutura do Projeto 🏗️

- **`main.py`**: Arquivo principal que executa o loop de interação com o usuário e oferece as opções de menu (criar conta, fazer login, sair).
- **`funcs.py`**: Contém as funções para criação de conta (`criar_conta`), validação de e-mail (`validador_email`), verificação de senha (`passwordVerificator`), e login (`entrar`).

### Exemplo de Execução 💻

Ao executar o programa, o fluxo seria o seguinte:

```bash
🌟 Bem-vindo ao Sistema de Contas!
Aqui você pode criar uma nova conta ou acessar sua conta existente de forma fácil e segura.
Vamos começar? Escolha uma das opções abaixo:

    1. Criar uma nova conta
    2. Fazer login
    3. Sair do sistema

Escolha uma opção (1, 2, 3): 1

🔑 Criando uma nova conta...
Digite o seu e-mail: usuario@example.com
Crie uma senha segura: ********
Confirme sua senha: ********
Conta criada com sucesso! 🎉

Escolha uma opção (1, 2, 3): 2

🔓 Entrando na sua conta...
Digite seu e-mail para login: usuario@example.com
Digite sua senha: ********
✔️ Bem-vindo à sua conta! 🎉

Escolha uma opção (1, 2, 3): 3
👋 Saindo... Até logo!
