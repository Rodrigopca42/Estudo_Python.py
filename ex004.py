salario1 : float ; salario2 : float
nome1 : str; nome2: str
sexo1: str; sexo2: str
idade1 : int; idade2 : int


nome1 = input("Nome da primeira pessoa: ")
idade1 = int(input("Digite a idade :"))
sexo1 = input("digite o sexo (F/M): ")
salario1 = float(input("Digite o valor do salario do(a) {nome1} :"))

nome2 = input("Qual é o nome da segunda pessoa? ")
idade2 = int(input("Digite a idade :"))
sexo2 = input("digite o sexo (F/M): ")
salario2 = float(input("Digite o valor do salario do(a) {nome2} :"))

print(f"Nome1 : {nome1}")
print(f"Idade: {idade1}")
print(f"Sexo: {sexo1}")
print(f"E ganha por mês: R${salario1:.2f}")

print(f"Nome2 : {nome2}")
print(f"Idade: {idade2}")
print(f"Sexo: {sexo2}")
print(f"E ganha por mês: R${salario2:.2f}")