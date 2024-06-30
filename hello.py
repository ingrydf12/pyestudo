#mainpulação de strings e fatiamento

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

#f-string
print(f"meu nome é {texto.strip()} e tenho {idade} anos.")

#strings de múltiplas linhas
mensagem = """Olá, meu nome é Ingryd
e tenho 18 anos. Bom dia!
"""

print(mensagem)

#listas

frutas = ["laranja", "maca", "uva"]
print(frutas)
frutas = []

letras = list("python") #elemento iterado.
print(letras)
numeros = list(range(10)) #gera valores de 0 a 9
print(numeros)
carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print (carro)

# a função isinstance() retorna se um determinado objeto é de um tipo (boolean: True ou False)

carros = ("gol")
print(isinstance(carros, str))
# resultado: True

carros_new = ["gol", "fiat"]
print(isinstance(carros_new, list))
#resultado True

carros_new = ("gol", "fiat",)
print(isinstance(carros_new, tuple))
# resultado True