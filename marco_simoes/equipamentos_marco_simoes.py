def ler_equipamentos_do_ficheiro(nome_ficheiro):
    equipamentos = []
    with open(nome_ficheiro, 'r') as file:
        for line in file:
            equipamentos.append(line.strip())
    return equipamentos

if __name__ == '__main__':
    equipamentos = ler_equipamentos_do_ficheiro("devices.txt")
    while True:
        termo_a_procurar = input("Equipamento a procurar (sair p/terminar): ")
        if termo_a_procurar.lower() == "sair":
            break
        equipamentos_correspondentes = [equipamento for equipamento in equipamentos if termo_a_procurar in equipamento]
        if equipamentos_correspondentes:
            for equipamento in equipamentos_correspondentes:
                print(equipamento)
            print("Foram encontrados {} equipamentos.".format(len(equipamentos_correspondentes)))
        else:
            print("Equipamento não existe na lista.")