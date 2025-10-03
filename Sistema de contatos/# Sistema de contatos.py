
# Sistema de contatos, com cadastro, consulta e remoção de contatos
print("Bem vindo a Lista de Contatos do Daniel Mourão")

# Onde vou guardar os contatos em memória
lista_contatos = []
# Meu número do RU
meu_id = 4387915

# Programa principal que roda até o usuário sair
while True:
    print("\n--- MENU PRINCIPAL ---")
    print("1 - Cadastrar Contato")
    print("2 - Consultar Contato(s)")
    print("3 - Remover Contato") 
    print("4 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    # Opção 1 - Cadastrar contato, com ID automático
    if opcao == "1":
        print("\n--- MENU CADASTRAR CONTATO ---")
        
        # Mostra o ID automatico
        print(f"Id do Contato: {meu_id}")
        
        # Pede os dados do contato pro usuário
        nome = input("Digite o nome do Contato: ")
        atividade = input("Digite a atividade do contato: ")
        telefone = input("Digite o telefone do contato: ")
        
        # Cria o contato como um dicionário (estrutura de dados)
        novo_contato = {
            'id': meu_id,
            'nome': nome, 
            'atividade': atividade,
            'telefone': telefone
        }
        
        # Adiciona na lista de contatos e avisa o usuário que salvou o contato
        lista_contatos.append(novo_contato)
        print("Contato salvo!")
        
        # Aumenta o ID pro proximo contato automaticamente (para não repetir ID)
        meu_id = meu_id + 1
    
    # Opção 2 - Consultar contatos (por ID, por atividade ou todos)
    elif opcao == "2":
        while True:
            print("\n--- MENU CONSULTAR CONTATOS ---")
            print("1 - Ver Todos os Contatos")
            print("2 - Buscar por ID")
            print("3 - Buscar por Atividade")
            print("4 - Voltar")
            
            opcao_consulta = input("Escolha: ")
            
            # Ver todos os contatos cadastrados na lista de contatos em memória
            if opcao_consulta == "1":
                if len(lista_contatos) == 0:
                    print("Nenhum contato cadastrado!")
                else:
                    print("\n--- TODOS OS CONTATOS ---")
                    for contato in lista_contatos:
                        print(f"ID: {contato['id']}")
                        print(f"Nome: {contato['nome']}")
                        print(f"Atividade: {contato['atividade']}")
                        print(f"Telefone: {contato['telefone']}")
                        print("---")
            
            # Buscar por ID (escolhido pelo usuário)
            elif opcao_consulta == "2":
                try:
                    id_procurado = int(input("Digite o ID do contato: "))
                    encontrado = False
                    
                    for contato in lista_contatos:
                        if contato['id'] == id_procurado:
                            print("\n--- CONTATO ENCONTRADO ---")
                            print(f"ID: {contato['id']}")
                            print(f"Nome: {contato['nome']}")
                            print(f"Atividade: {contato['atividade']}")
                            print(f"Telefone: {contato['telefone']}")
                            print("---")
                            encontrado = True
                            break
                    
                    if not encontrado:
                        print("Contato não encontrado!")
                        
                except:
                    print("Digite um número válido!")
            
            # Buscar por atividade (escolhida pelo usuário)
            elif opcao_consulta == "3":
                atividade_procurada = input("Digite a atividade: ")
                encontrou_algo = False
                
                print(f"\n--- CONTATOS COM ATIVIDADE: {atividade_procurada} ---")
                for contato in lista_contatos:
                    if contato['atividade'] == atividade_procurada:
                        print(f"ID: {contato['id']}")
                        print(f"Nome: {contato['nome']}")
                        print(f"Atividade: {contato['atividade']}")
                        print(f"Telefone: {contato['telefone']}")
                        print("---")
                        encontrou_algo = True
                
                if not encontrou_algo:
                    print("Nenhum contato com essa atividade!")
            
            # Voltar ao menu principal
            elif opcao_consulta == "4":
                break
            else:
                print("Opção inválida!")
    
    # Opção 3 - Remover contato (por ID)
    elif opcao == "3":
        print("\n--- MENU REMOVER CONTATO ---")
        
        try:
            id_remover = int(input("Digite o ID do contato a remover: "))
            removeu = False
            
            for i in range(len(lista_contatos)):
                if lista_contatos[i]['id'] == id_remover:
                    lista_contatos.pop(i)
                    print("Contato removido!")
                    removeu = True
                    break
            
            if not removeu:
                print("Contato não encontrado!")
                
        except:
            print("Digite um número válido!")
    
    # Opção 4 - Sair do programa
    elif opcao == "4":
        print("Até logo!")
        break
    
    # Opção inválida no menu principal
    else:
        print("Opção inválida! Escolha 1, 2, 3 ou 4")