# Simulador G.S. Java - Versão Simplificada com Comentários
# Autor: Lucas dos Santos Oliveira
# Disciplina: Computational Thinking using Python
# Objetivo: Simular funcionalidades básicas do app G.S. Java para prevenção e alerta de desastres

def mostrar_menu():
    # Exibe o menu principal com as opções do programa
    print("\n==== MENU G.S. Java ====")
    print("1 - Ver desastres por região")
    print("2 - Ver tutoriais de prevenção")
    print("3 - Simular alerta por localização")
    print("4 - Sair")

def desastres_por_regiao(regiao):
    # Retorna uma lista com os desastres comuns na região informada
    if regiao == "Japao":
        return ["Terremoto", "Tsunami", "Vulcao"]
    elif regiao == "Brasil":
        return ["Enchente", "Deslizamento"]
    elif regiao == "EUA":
        return ["Furacao", "Incendio Florestal", "Nevasca"]
    else:
        return []  # Região não cadastrada

def mostrar_tutorial(desastre):
    # Retorna um tutorial simples para o desastre informado
    if desastre == "Terremoto":
        return "Durante um terremoto, proteja sua cabeça e afaste-se de janelas."
    elif desastre == "Enchente":
        return "Evite áreas baixas e vá para locais elevados."
    elif desastre == "Furacao":
        return "Mantenha janelas fechadas e estoque suprimentos."
    else:
        return "Tutorial não disponível para esse desastre."

def simular_alerta(pais):
    # Retorna uma mensagem de alerta com base no país informado
    if pais == "Japao":
        return "ALERTA: Possível terremoto detectado!"
    elif pais == "Brasil":
        return "ALERTA: Risco de enchente na região."
    else:
        return "Nenhum alerta ativo neste momento."

# Programa principal - controle do fluxo do menu
opcao = 0

while opcao != 4:  # Enquanto a opção for diferente de 4 (sair)
    mostrar_menu()  # Mostra as opções para o usuário
    opcao = int(input("Escolha uma opção: "))  # Recebe a escolha do usuário

    if opcao == 1:
        regiao = input("Digite o nome da região (Japao, Brasil, EUA): ")
        desastres = desastres_por_regiao(regiao)
        if len(desastres) > 0:
            print("Desastres comuns nessa região:")
            for d in desastres:
                print("- " + d)
        else:
            print("Região não cadastrada.")

    elif opcao == 2:
        desastre = input("Digite o nome do desastre (Terremoto, Enchente, Furacao): ")
        tutorial = mostrar_tutorial(desastre)
        print("Tutorial:")
        print(tutorial)

    elif opcao == 3:
        pais = input("Digite o país atual do celular: ")
        alerta = simular_alerta(pais)
        print(alerta)

    elif opcao == 4:
        print("Encerrando o simulador. Obrigado!")
    else:
        print("Opção inválida. Tente novamente.")
