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
    
''' Desenvolva uma função programa que valide se um número de telefone tem o formato correto.
O formato aceito para números de telefone é: (XX) 9XXXX-XXXX, onde X representa um dígito de 0 a 9. Lembre-se de respeitar os espaços entre os números quando preciso.'''

# Conheça mais sobre o Regex: https://docs.python.org/pt-br/3.8/howto/regex.html
# Conheça mais sobre o 're' do python: https://docs.python.org/pt-br/3/library/re.html

# Módulo 're' que fornece operações com expressões regulares.
import re


 # TODO: Crie uma função chamada 'validate_numero_telefone' que aceite um argumento 'phone_number':
def validate_numero_telefone(phone_number):
    pattern = r'^\(\d{2}\) 9\d{4}-\d{4}$'
    # TODO: Defina um padrão de expressão regular (regex) para validar números de telefone no formato (XX) 9XXXX-XXXX:
   
    # A função 're.match()' para verifica se o padrão definido corresponde ao número de telefone fornecido.
    # O 're.match()' retorna um objeto 'match' se houver correspondência no início da string, caso contrário, retorna 'None'.
    if re.match(pattern, phone_number):  
        # TODO: Agora crie um return, para retornar que o número de telefone é válido:
      return "Número de telefone é válido."
       # TODO: Crie um else e return, caso não o número de telefone seja inválido:
    else:
        return "Número de telefone é inválido."
    

# Solicita ao usuário que insira um número de telefone e armazena o valor fornecido na variável 'phone_number'.
phone_number = input()  

# TODO: Chame a função 'validate_numero_telefone()' com o número de telefone fornecido como argumento e armazene o resultado retornado na variável 'result'.
result = validate_numero_telefone(phone_number)

# Imprime o resultado:
print(result)