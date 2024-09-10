def adicionar_contato(nome_contato, telefone_contato, email_contato, favorito=False):
  adicionar_lista_contato = { "nome": nome_contato, "telefone": telefone_contato, "email": email_contato, "favorito": favorito }
  lista_contato.append(adicionar_lista_contato)
  print(f"\nContato {nome_contato} adicionado com sucesso \n")

def visualizar_contato(lista_contato):
    for indice, contato in enumerate(lista_contato, start=1):
        status = "★" if contato["favorito"] else " "
        print(f"{indice}. {status} {contato['nome']}")
    return

def visualizar_contato_favorito(lista_contato):
    for indice, contato in enumerate(lista_contato, start=1):
        status = "★" if contato["favorito"] else " "
        if contato["favorito"]:
          print(f"{indice}. {status} {contato['nome']}")
        else: print("\nSem contantos Favoritos")
        return
        
def editar_contato(lista_contato):
    visualizar_contato(lista_contato)
    indice_contato = int(input("\nDigite o índice do contato a ser editado: "))
    indice_contato_ajustado = indice_contato - 1
    if 0 <= indice_contato_ajustado < len(lista_contato):
        contato_selecionado = lista_contato[indice_contato_ajustado]
        print(f"Editando contato: {contato_selecionado['nome']}")
        
        while True:
            print("\nSelecione como você gostaria de alterar o contato:")
            print("1. Editar o Nome")
            print("2. Editar o E-mail")
            print("3. Editar o Telefone")
            print("4. Adicionar contato aos favoritos")
            print("5. Apagar Contato")
            print("6. Sair do modo de edição")
            
            escolha_edit = int(input("Escolha uma opção: "))
            
            if escolha_edit == 1:
                novo_nome = input(f"Digite o novo nome do contato {contato_selecionado['nome']}: ")
                contato_selecionado['nome'] = novo_nome
                print("Nome alterado com sucesso!")
            elif escolha_edit == 2:
                novo_email = input(f"Digite o novo e-mail do contato {contato_selecionado['email']}: ")
                contato_selecionado['email'] = novo_email
                print("E-mail alterado com sucesso!")
            elif escolha_edit == 3:
                novo_telefone = input(f"\nDigite o novo telefone do contato {contato_selecionado['telefone']}: ")
                contato_selecionado['telefone'] = novo_telefone
                print("\nTelefone alterado com sucesso")
            elif escolha_edit == 4:
                print(f"\nContato {contato_selecionado['nome']} adicionado aos favoritos")
                contato_selecionado["favorito"] = True
            elif escolha_edit == 5:
                print(f"\nContato {contato_selecionado['nome']} excluido com sucesso")
                lista_contato.remove(contato_selecionado)
                
            elif escolha_edit == 6:
                print("\nSaindo do modo de edição") 
                break
            else:
                print("Opção inválida. Tente novamente.")
    else:
        print("Índice inválido. Tente novamente.")

lista_contato = []

while True:
    print("Agenda de contatos:")
    print("1. Adicionar Contato")
    print("2. Visualizar Contatos")
    print("3. Editar Contato")
    print("4. Contatos Favoritos")
    print("5. Apagar Contato")
    print("6. Encerrar Programa")
    
    escolha = int(input("\nEscolha uma das opções: "))
    if escolha == 1:
        nome_contato = input("\nDigite o nome do contato: ")
        telefone_contato = input("\nDigite o telefone do contato: ")
        email_contato = input("\nDigite o e-mail do contato: ")
        adicionar_contato(nome_contato, telefone_contato, email_contato)
    elif escolha == 2:
        visualizar_contato(lista_contato)
    elif escolha == 3:
        editar_contato(lista_contato)
    elif escolha == 4:
        visualizar_contato_favorito(lista_contato)
    elif escolha == 6:
        break

print("Programa Encerrado")
        
    
    

lista_contato = []

while True:
  print("Agenda de contatos:")
  print("1. Adicionar Contato")
  print("2. Visualizar Contatos")
  print("3. Editar Contato")
  print("4. Contatos Favoritos")
  print("5. Apagar Contato")
  print("6. Encerrar Programa")
  
  escolha = int(input("\nEscolha uma das opções: "))
  if escolha == 1:
    nome_contato = input("\nDigite o nome do contato: ")
    telefone_contato = input("\nDigite o telefone do contato: ")
    email_contato = input("\nDigite o e-mail do contato: ")
    adicionar_contato(nome_contato, telefone_contato, email_contato)
  elif escolha == 2:
    visualizar_contato(lista_contato)
  elif escolha == 3:
    editar_contato(lista_contato)
  elif escolha == 7:
    break
