nota1 = int (input("Digite a primeira nota: "))
nota2 = int (input("Digite a segunda nota: "))
n3 = (nota1 + nota2) / 2

if n3 >= 7:
    print(f"Aprovado com a nota: {n3}")
elif n3 <= 7:
    print(f"Reprovado com a nota: {n3}")
elif n3 == 10:
    print(f"Parabéns aprovado com a nota máxima {n3}.")