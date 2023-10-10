cor = input("Digite uma cor: ").lower().strip() 

match cor:
    case "verde":
        print ("Pode passar!")
    case "amarelo":
        print ("Mantenha a Atenção!")
    case "vermelho":
        print("Pare!")
    case _:
        print("Cor inválida.")