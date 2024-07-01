# listas
tutas = ["laranja", "maca", "uva"]

frutas = []

letras = list("python") #elemento iterado. >>> ['p', 'y', 't', 'h', 'o', 'n']

numeros = list(range(10)) #gera valores de 0 a 9 >>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]

#matriz(listas aninhadas)
matriz = [
	[1, "a", 2],
	["b", 3, 4]
	[6, 5, "c"]
]

matriz[0] # [1, "a", 2]
matriz [0][0] # 1
matriz [0][-1] # 2
matriz[-1][-1] # "c"

# conjuntos
number = [1, 2, 3, 1, 2 ,4]

lista = set(number)
print(lista)

# tuplas
carros_new = ("gol", "fiat",)
print(isinstance(carros_new, tuple))

# dicionarios
pessoa = {"nome": "Guilherme", "idade":28, "telefone":"3333-1234"}

contatos = {"guilherme@gmail.com":pessoa}
for chave in contatos:
	print(chave, contatos[chave])
 
#funcoes
def nome_funcao():
    print("função")
    
# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input("Insira o seu consumo médio em GB durante um mês:\n"))

# TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal:
def recomendar_plano(*consumo):
  if consumo <= 10.0:
    return "Plano Essencial Fibra - 50Mbps"
  elif consumo > 10.0 and consumo <= 20.0:
    return "Plano Prata Fibra - 100Mbps"
  elif consumo > 20.0:
    return "Plano Premium Fibra - 300Mbps"

# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))

# TODO: Crie uma Lista 'itens' para armazenar os equipamentos:
itens = []

# TODO: Crie um loop para solicita os itens ao usuário:
for i in range(3):
# TODO: Solicite o item e armazena na variável "item":
  item = input()
# TODO: Adicione o item à lista "itens":
  itens.append(item)
# Exibe a lista de itens
print("Lista de Equipamentos:")  
for item in itens:
    # Loop que percorre cada item na lista "itens"
    print(f"- {item}")