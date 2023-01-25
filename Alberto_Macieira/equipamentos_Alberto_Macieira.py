
with open("devices.txt", "r") as file:
    equipamento = file.readlines()

lista_equipamento = []
for linha in equipamento:
    lista_equipamento.append(linha.strip())

while True:
    equipamento = input("Equipamento a procurar (sair p/terminar): ")
    if equipamento.lower() == "sair":
        break
    else:
        contagem = 0
        for  item in lista_equipamento:
            if equipamento in item:
                print(item)
                contagem += 1
        
        
        if contagem > 0:
            print(str(contagem) + " equipamento(s) encontrado(s).")
        else:
            print("Equipamento Não existe na Lista.")