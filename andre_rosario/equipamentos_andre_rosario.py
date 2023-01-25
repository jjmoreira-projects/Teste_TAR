#Abrir o ficheiro devices.txt
f = open("devices.txt", "r")

#Guardar todos os equipamentos no ficheiro de texto numa lista
lista_de_equipamentos = f.read().splitlines()

#Fazer a seguinte pergunta "Equipamento a procurar (sair p/terminar) :" até que o utilizador coloque "sair"
equipamento = input("Equipamento a procurar (sair p/ terminar): ")
while equipamento != "sair":
    #Para cada resposta anterior, deve procurar na lista criada em b) os equipamentos que correspondem e apresentar e contar quantos equipamentos encontra
    contador = 0
    for item in lista_de_equipamentos:
        if equipamento in item:
            contador += 1
            print(item)
    #No final deve mostrar a quantidade, caso não encontre (contagem igual a zero) deve apresentar a mensagem "Equipamento Não existe na Lista!"
    if contador == 0:
        print("Equipamento Não existe na Lista!")
    else:
        print("Foram encontrados", contador, "equipamentos")
    equipamento = input("Equipamento a procurar (sair p/ terminar): ")

#Fechar o ficheiro
f.close()