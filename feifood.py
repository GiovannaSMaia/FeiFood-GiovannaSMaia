usuario={}
def cadastrarusuario():
    Nome = input("Digite seu primeiro nome: ")
    Sobrenome = input("Digite seu último sobrenome: ")
    nome_completo = Nome[0].upper()+Nome[1:].lower()+ Sobrenome[0].upper() + Sobrenome[1:]()
    print(nome_completo)
    Idade = int(input("Digite sua idade: "))
    Email = input("Digite seu email: ")
    Senha = input("Digite sua senha: ")
    usuario["Nome"]=nome_completo
    usuario["Idade"]=Idade
    usuario["Email"]=Email
    usuario["Senha"]=Senha
    print("Usuário cadastrado com sucesso!")
    
login= {}
def cadastrarlogin():
    email_login = input("Digite seu email para login: ")
    senha_login = input("Digite sua senha para login: ")
    # colocar email_login e senha_login dentro do dicionario login
    if email_login == usuario.get("Email") and senha_login == usuario.get("Senha"):
        print("Login bem-sucedido!")
    else:
        print("Email ou senha incorretos.")

cardapio = [
    1: {"nome": "Hambúrguer", "preço": 15.00},
    2: {"nome": "Pizza", "preço": 25.00},
    3: {"nome": "Salada", "preço": 10.00},
    4: {"nome": "Refrigerante", "preço": 5.00},
    5: {"nome": "Sobremesa", "preço": 8.00}]