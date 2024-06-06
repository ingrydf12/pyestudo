nome = "guilhErme"

print(nome.upper()) # transforma tudo em maiúscula
print(nome.lower()) # transforma tudo em minúscula
print(nome.title()) # transforma a primeira letra maiúscula e o resto minúscula

texto = " Ingryd  "

print(texto.strip()) #remove espaços em branco
print(texto.lstrip()) # remove espaços em branco da esquerda
print(texto.rstrip()) # remove espaços em branco da direita

idade = 18

print("Meu nome é {} e tenho {} anos.".format(texto.strip(), idade))

#outra forma usando o format
#lembnrando que a primeira posição é 0 
print("Meu nome é {1} e tenho {0} anos".format(idade, texto.strip()))