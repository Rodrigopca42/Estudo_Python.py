n = input("Digite Algo: ")
print("O tipo primitivo desse valor é  {} ". format(type(n)))
print("Só tem espaços? {} " . format(n.isspace()))
print("É um número? {} ". format(n.isnumeric()))
print("É alfabético? {} ". format(n.isalpha()))
print("É alfanumérico? {} ". format(n.isalnum()))
print("Está em maiusculo? {}". format(n.isupper()))
print("Está em minuscula? {} ". format(n.islower()))
print("Está Capitalizada? {} ". format(n.istitle()))#capitalizado quer dizer que tem letras maiusculas e minusculas ao mesmo tempo.