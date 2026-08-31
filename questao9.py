idade = int(input("Digite sua idade: "))
if idade > 0 and idade <= 12:
    print("Crianca")
elif idade >= 13 and idade <= 17:
    print("Adolescente")
elif idade >= 18 and idade <= 59:
    print("Adulto")
else:
    print("Idoso!")