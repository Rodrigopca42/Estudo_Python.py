altura: int 
salario: float 
nome: str 
sexo: str
profissao: str

nome = "Viviane Almeida"
profissao = "Psicanalista"
salario = 5850.5
altura = 1.65
sexo = "F"

print(f"A {profissao}, {nome} do sexo {sexo}, ganha R${salario:.2f} e mede {altura} de pura beleza.")

print("A {:s}, {:s} do sexo {:s}, ganha R${:.2f} e mede {:.2f} de pura beleza.".format(profissao,nome,sexo,salario,altura))
