n1 = int(input('Digite um número: '))
print(type(n1))

n2 = input('Digite um outro número: ')
print(type(n2))

n3 = int(input('Digite um número: '))
n4 =int(input('Digite mais um número: '))
s1 = (n1 - n3) / n4

#print(f"O resultado do calculo entre  {n1} , {n3} e {n4} tem o valor : {s1}")
print ('O resultado do calculo entre {}, {} e {} tem o valor: {}'. format(n1, n3, n4, s1))