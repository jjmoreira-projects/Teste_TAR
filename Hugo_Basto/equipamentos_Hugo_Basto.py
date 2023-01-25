with open("devices.txt", "r") as file:
    equipamentos = file.readlines()

lista_equipamentos = []
for linha in equipamentos:
    lista_equipamentos.append(linha.strip())

while True:
    equipamentos = input("Equipamento a procurar (sair p/terminar): ")
    if equipamentos.lower() == "sair":
        break
    else:
        quantidade = 0
        for item in lista_equipamentos:
            if equipamentos in item:
                print(item)
                quantidade += 1
        if quantidade > 0:
            print(str(quantidade) + " equipamento(s) encontrado(s).")
        else:
            print("Equipamento Não existe na Lista.")