# Abrir o ficheiro devices.txt
with open("devices.txt", "r") as f:
    # Read the contents of the file into a list
    devices = f.read().splitlines()

# Crie uma variável para acompanhar se encontramos o dispositivo 
found = False

#Crie uma variavel para contar cada equipamento
contador=0;

# solicitar continuamente ao usuário um nome de dispositivo para pesquisar
while True:
    # Perguntar ao utilizador o nome do equipamento
    device_name = input("Equipamento a procurar (sair p/terminar) :")

    # se o utilizador escrever "sair" parar o loop
    if device_name == "sair":
        break

    
    for device in devices:
        # Check se o nome do equipamento esta na lista
        if device_name in device:
            found = True
            # Print se exstir
            print(device)
            contador+=1;
            


    # se nao estiver na lista print desta frase
    if not found:
        print("Nenhum equipamento encontrado com o nome:", device_name)
    else:
        found = False

    #print dos nº de equipamentos
    print("Quantidade", contador)
