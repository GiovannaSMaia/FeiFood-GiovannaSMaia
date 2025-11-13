from random import randint
menu ={
  1: "Não tem cadatro? Realizar novo cadastro",
  2: "Já tem cadastro? Faça o login",
  0: "Sair do app"}
loop = true

#Menus
def exibir_menu():
  print("Menu - Pizzaria Belo Molho")
  for opcao, descricao in menu.items():
    print(f"{opcao} - {descricao}")
  escolha = int(input("Escolha uma opção"))
  return escolha


def main():
  while loop == True:
    escolha = exibirmenu()
    if escolha==1:
      cadastrarusuario()
    elif escolha==2:
      fazerlogin()
    elif escolha==0:
      sair()
    else:
      print("Opção inválida. Escolha umm dos números acima")


def funcoesapp():
  while true:
    print()
    print("Bem vindo")
    print("1 - Mostrar cardápio")
    print("2 - Pesquise no Cardápio")
    print("3 - Listar pesquisas anteriores")
    print("4 - Cadastrar novo pedido")
    print("5 - Editar pedido")
    print("6 - Avaliar Pedido")
    print("7 - Sair")
    escolha_app = int(input("Escolha uma opção"))
    if escolha_app == 1:
      mostrarcardapio()
    elif escolha_app == 2:
      consultacardapio()
    elif escolha_app == 3:
      listarinformaçõesbuscadas()
    elif escolha_app == 4:
      cadastraspedido()
    elif escolha_app == 5:
      editarpedido()
    elif escolha_app == 6:
      avaliarpedido()
    elif escolha_app == 7:
      break
    else:
      print("Oção inválida. Escolha uma da opções acima")


def exibirmenu():
  print("Menu:")
    for opcao, descricao in menu.items():
        print(f"{opcao} - {descricao}")
    escolha = int(input("Escolha uma opção: "))
    return escolha


def editarpedido():
    print()
    print("Editar pedido:")
    print("1 - Excluir Pedido")
    print("2 - Adicionar Itens ao Pedido")
    print("3 - Remover Itens do Pedido")
    escolha_editar = int(input("Escolha uma opção: "))
    if escolha_editar == 1:
        editar_pedido_excluir()
    elif escolha_editar == 2:
        editar_pedido_adicionar_itens()
    elif escolha_editar == 3:
        editar_pedido_remover_itens()
    else:
        print("Opção inválida. Tente novamente.")


def cadastrarusuario():
    print()
    Nome = input("Digite seu primeiro nome: ")
    Sobrenome = input("Digite seu último sobrenome: ")
    nome = Nome[0].upper()+Nome[1:].lower() 
    sobrenome = Sobrenome[0].upper() + Sobrenome[1:].lower()
    telefone = input("Digite o telefone: ")
    email = input("Digite o e-mail: ")
    Idade = int(input("Digite sua idade: "))
    print()
    if Idade < 18:
        print("Menor de idade. Acesso Negado")
        return
    
    else:
        arquivo_usuarios = open("usuarios.txt", "a")
        arquivo_usuarios.write(f"{nome},{sobrenome},{telefone},{email},{Idade}\n")
        arquivo_usuarios.close()
        print("Usuário cadastrado com sucesso!")


def fazerlogin():
    print()
    print("Fazer Login: ")
    print()
    nome_procurar = input("Digite o primeiro nome do seu Login anteriormente cadastrado: ")
    sobrenome_procurar = input("Digite o sobrenome do seu Login anteriormente cadastrado: ")
    nome_procurar_atualizado = nome_procurar[0].upper()+nome_procurar[1:].lower()
    sobrenome_procurar_atualizado = sobrenome_procurar[0].upper() + sobrenome_procurar[1:].lower()
    with open("usuarios.txt", "r") as arquivo_login:
        conteudo = arquivo_login.readlines()   
    for linha in conteudo:
        nome, sobrenome, telefone, email, Idade,= linha.strip().split(",")
        if nome_procurar_atualizado.lower() == nome.lower() and sobrenome_procurar_atualizado.lower() == sobrenome.lower():
            print()
            print("Seu Usuário é: ")
            print(f"Nome: {nome}, {sobrenome} Telefone: {telefone}, E-mail: {email}, Idade: {Idade}")
            print("Login realizado com sucesso!")
            print()
            funcoes_app()

def mostrarcardapio():
    # cardapio=open("cardapio.txt", "a")  
    # cardapio.write("------Cardápio------\n")
    # cardapio.write(f"Pizza, Moda-da-casa, R$_45, 1\n")
    # cardapio.write("Pizza, Marguerita, R$_45, 2\n")
    # cardapio.write("Pizza, Mussarela, R$_30, 3\n")
    # cardapio.write("Pizza, Bauru, R$_35, 4\n")
    # cardapio.write("Pizza, De-Calabresa, R$_40, 5\n")
    # cardapio.write("Pizza, Calacatu, R$_40, 6\n")
    # cardapio.write("Pizza, Baiana, R$_40, 8\n")
    # cardapio.write("Pizza, Portuguesa, R$_35, 9\n")
    # cardapio.write("Pizza, Carne-Seca, R$_40, 10\n")
    # cardapio.write("--------------------\n")
    # cardapio.close()
    with open("cardapio.txt", "r") as cardapio:
         conteudo = cardapio.readlines()   
         for linha in conteudo:
             pizza, sabor, rs, valor, id_sabor,= linha.strip().split(",") 
             print(f"{pizza} de {sabor} - Preço: R$ {valor} - Código: {id_sabor}")


def consultacardapio():
    print("Consulte no cardapio")
    sabor_consulta=input("Digite o sabor que deseja procurar:").lower()
    with open("cardapio.txt", "r") as arquivo_cardapio:
        consulta = arquivo_cardapio.readlines()

    for linha in consulta:
        pizza, sabor, rs, valor, id_sabor = linha.strip().split(",")
        if sabor_consulta == sabor.lower():
            print(f"{pizza} de {sabor}, R${valor}, Id:{id_sabor}")
            with open("consultas.txt", "a") as consultas:
                consultas.write(f"{pizza},de,{sabor},{valor},Id:,{id_sabor}\n")
            break 


def listarinformaçõesbuscadas():
    print("Informações buscadas:")
    with open("consultas.txt", "r") as consultas:
        conteudo = consultas.readlines()
        for linha in conteudo:
            pizza, de, sabor, valor, id,id_sabor= linha.strip().split(",") 
            print(f"{pizza} {de} {sabor} {valor} {id}{id_sabor}")


def cadastrarpedido():
    with open("cardapio.txt", "r") as cardapio:
        conteudo = cardapio.readlines() 
        for linha in conteudo:
            pizza, sabor, rs, valor, id_sabor= linha.strip().split(",") 
            print(f"{pizza} de {sabor} - Preço: R$ {valor} - Código: {id_sabor}")
    conta = 0
    sabores=[]
    while True:
        pedido = int(input("Digite o código do sabor que deseja pedir ou 0 para finalizar: \n"))
        if pedido == 0:
                id_pedido = int(randint(0,100))
                for sabor in sabores:
                    print(f"Sabores de Pizza pedidos:{sabor}")
                print()
                print("Finalizando pedido...")
                print()
                print(f"Total a pagar: R$ {conta}")
                print()
                print(f"Seu ID de pedido é: {id_pedido}, guarde ele para futuras consultas \n")
                print()
                with open("pedidos.txt", "a") as pedidos:
                    for sabor in sabores:
                        pedidos.write(f"Pizza,de,{sabor},ID:,{id_pedido}\n")
                with open("conta.txt", "a") as contas:
                    contas.write(f"Total,conta,{conta},ID:,{id_pedido}\n")
                break
        
        for linha in conteudo:
                pizza, sabor, rs, valor, id_sabor= linha.strip().split(",") 
                if pedido == int(id_sabor):
                    pedidoecontrado = True
                    print(f"Você pediu uma {pizza} de {sabor} no valor de R$ {valor}")
                    sabores.append(sabor)
                    conta += int(valor.strip().replace("R$_",""))


def editar_pedido_excluir():
    print("Excluir pedido")   
    id_pedido_excluir=int(input("Digite o ID do pedido que deseja excluir: "))
    
    with open("pedidos.txt", "r") as arquivo_pedidos:
        conteudo = arquivo_pedidos.readlines()
        arquivo_pedidos.close()
        pedidosantigos=conteudo.copy()

    with open("conta.txt", "r") as arquivo_conta:
        conta = arquivo_conta.readlines() 
        arquivo_conta.close()
        contasantigas=conta.copy()

    for linha in pedidosantigos:
        pizza, de, sabor, id, id_pedido = linha.strip().split(",") 
        if str(id_pedido_excluir) == id_pedido: 
            print(f"{pizza} {de} {sabor} {id}{id_pedido}")
    print()
    confirmarcao = input("Deseja realmente excluir o pedido? SIM ou NAO: ").lower()
    print()
    if confirmarcao == "sim":
        pedidos=[]
        for linha in pedidosantigos:
            if str(id_pedido_excluir) not in linha:
                pedidos.append(linha)
        
        with open("pedidos.txt", "w") as arquivo_pedidos:
             arquivo_pedidos.writelines(pedidos)
        print("Pedido excluído")

        conta=[]
        for linha in contasantigas:
            if str(id_pedido_excluir) not in linha:
                conta.append(linha)
       
        with open("conta.txt", "w") as arquivo_conta:
            arquivo_conta.writelines(conta)
        print("Conta excluída")


def editar_pedido_adicionar_itens():
    print("Adicionar itens ao pedido") 
    mostrarcardapio()  
    print()
    
    id_pedido_adicionar=int(input("Digite o ID do pedido que deseja adicionar itens: "))
    
    while True:
        
        novosabor = int(input("Digite o codido do novo sabor que deseja adicionar ou 0 para finalizar: "))
        
        if novosabor == 0:
            break
        
        with open("cardapio.txt", "r") as cardapio:
            for linha in cardapio:
                    pizza, sabor_cardapio,rs,valor_cardapio, id_sabor= linha.strip().split(",")  
                    if int(id_sabor) == novosabor:
                        sabor = sabor_cardapio
                        print(f"Sabor {sabor} adicionado ao pedido.")
                        with open("pedidos.txt", "a") as arquivo_pedidos:
                            arquivo_pedidos.write(f"Pizza,de,{sabor},ID:,{id_pedido_adicionar}\n")
                            print("Seu novo sabor foi adicionado")
                            print()
                            break


def editar_pedido_remover_itens():
    print("Remover itens do pedido") 
    id_pedido_remover=int(input("Digite o ID do pedido que deseja remover itens: "))
    
    with open("pedidos.txt", "r") as arquivo_pedidos:
        conteudo = arquivo_pedidos.readlines()
    pedidosantigos=conteudo.copy()

    pedidos=[]
    for linha in conteudo:
        pizza, de, sabor, id, id_pedido = linha.strip().split(",") 
        if str(id_pedido_remover) == id_pedido.strip():
            print(f"{pizza} {de} {sabor} {id}{id_pedido}")
            pedidos.append(sabor)
    

    id_sabor_remover = int(input("Digite a posição queo sabor que deseja remover se encontra: "))
    id_sabor_remover=int(id_sabor_remover)-1

    sabor_remover = pedidos[id_sabor_remover]

    nova_lista_pedidos=[]
    for linha in pedidosantigos:
        pizza, de, sabor, id, id_pedido = linha.strip().split(",")
        if sabor == sabor_remover and str(id_pedido_remover) == id_pedido.strip():
            print(f"Sabor {sabor} removido do pedido.")
            continue
        nova_lista_pedidos.append(linha if linha.endswith('\n') else linha + '\n')
    
    with open("pedidos.txt", "w") as arquivo_pedidos:
        arquivo_pedidos.writelines(nova_lista_pedidos)


def avaliarpedido():
    print("Avaliar pedido")
    print()
    id_pedido=int(input("Digite o ID do pedido que quer avaliar: "))
    avaliacao = int(input("De uma nota de 1 a 5 para o pedido, sendo 1 péssimo e 5 ótimo: "))
    comentario = input("Deixe um comentário sobre o pedido: ")
    if avaliacao >=1 and avaliacao <=5:
        with open("avaliacoes.txt", "a") as avaliacoes:
            avaliacoes.write(f"ID Pedido: {id_pedido}, Avaliacao: {avaliacao}, Comentario: {comentario}\n")
        print("Obrigado pela avaliação!")
    else: 
        print("Nota invalida, digite um número de 1 a 5")


def sair():
    """
    Função para sair do programa.
    :return: None
    """
    print("Saindo...")
    exit() 
            
if __name__ == "__main__":
    main() 
