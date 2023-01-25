x = 0
y = 0
ficheiro = open("devices.txt", "r")
lista_equipamentos = []

for linha in ficheiro:
    linha = linha.strip()
    lista_equipamentos.append(linha)

ficheiro.close()

for item in lista_equipamentos:
    print (item)

while x != 1:
    nome_equipamento = input("Nome equipamento (sair p/terminar): ")
    if nome_equipamento == "sair":
        x=1
        break
    else:
        for item in lista_equipamentos:
            if item == nome_equipamento:
                y = y + 1
    if y != 0:
        print("Existem"+ str(y)+ "equipamentos que mencionou")
    else:
        print("Equipamento não existe na lista!")

                    

        
                        