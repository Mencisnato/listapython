#1 questão:
# Inicialize uma lista para armazenar os números que atendem ao critério
numeros_que_atendem = []

# Verifique os números no intervalo de 1000 a 2000
for numero in range(1000, 2001):
    if numero % 11 == 5:
        numeros_que_atendem.append(numero)

# Exiba os números que atendem ao critério
print("Números entre 1000 e 2000 que divididos por 11 têm resto igual a 5:")
for numero in numeros_que_atendem:
    print(numero)

#2 questão:

n = int(input("Digite um valor inteiro e positivo (n): "))

if n <= 0:
    print("O valor de 'n' deve ser um número inteiro positivo.")
else:
    soma = 0
    for i in range(1, n + 1):
        soma += 1/i

    print(f"A soma da série 1 + 1/2 + 1/3 + ... + 1/{n} é igual a: {soma:.2f}")

#questão 3:
# Loop externo de 1 a 10 (para os números de 1 a 10)
for i in range(1, 11):
    print(f"Tabuada do {i}:")

    # Loop interno de 1 a 10 (para os múltiplos)
    for j in range(1, 11):
        resultado = i * j
        print(f"{i} x {j} = {resultado}")

    # Pula uma linha entre as tabuadas
    print()
#4 questão:
# Inicializa uma lista para armazenar os grupos
grupos = []

# Ler cinco grupos de quatro valores
for _ in range(5):
    grupo = []
    for _ in range(4):
        valor = int(input("Digite um valor: "))
        grupo.append(valor)
    grupos.append(grupo)

# Mostrar os grupos na ordem lida
print("Grupos na ordem lida:")
for grupo in grupos:
    print(grupo)

# Mostrar os grupos na ordem crescente
print("Grupos na ordem crescente:")
for grupo in grupos:
    grupo.sort()
    print(grupo)

# Mostrar os grupos na ordem decrescente
print("Grupos na ordem decrescente:")
for grupo in grupos:
    grupo.sort(reverse=True)
    print(grupo)
#5 questão:
# Inicializa uma lista para armazenar os grupos
grupos = []

# Ler cinco grupos de quatro valores
for _ in range(5):
    grupo = []
    for _ in range(4):
        valor = int(input("Digite um valor: "))
        grupo.append(valor)
    grupos.append(grupo)

# Mostrar os grupos na ordem lida
print("Grupos na ordem lida:")
for grupo in grupos:
    print(grupo)

# Mostrar os grupos na ordem crescente
print("Grupos na ordem crescente:")
for grupo in grupos:
    grupo.sort()
    print(grupo)

# Mostrar os grupos na ordem decrescente
print("Grupos na ordem decrescente:")
for grupo in grupos:
    grupo.sort(reverse=True)
    print(grupo)

# Inicializa uma lista para armazenar os nomes dos clientes e os valores de compras
clientes = []

# Lê o nome e o valor das compras de cada cliente
for _ in range(15):
    nome = input("Digite o nome do cliente: ")
    compras = float(input("Digite o valor das compras do cliente no ano passado: "))
    clientes.append((nome, compras))

# Calcula e mostra o bônus para cada cliente
print("Bônus para os clientes:")
for nome, compras in clientes:
    if compras < 1000:
        bonus = compras * 0.10
    else:
        bonus = compras * 0.15

    print(f"{nome}: R${bonus:.2f}")
#6 questão:
# Inicializa as variáveis
preco_base = 5.00
despesas = 200.00
ingressos_base = 120
aumento_ingressos = 26
lucro_maximo = 0
preco_maximo = 0
vendidos_maximo = 0

# Loop para variar o preço do ingresso de R$5,00 a R$1,00 com incrementos de R$0,50
for preco_ingresso in range(500, 0, -50):
    preco_real = preco_ingresso / 100  # Convertendo centavos para reais
    ingressos_vendidos = ingressos_base + aumento_ingressos * (5 - preco_real)
    lucro = (preco_real * ingressos_vendidos) - despesas

    # Verifica se o lucro atual é o máximo
    if lucro > lucro_maximo:
        lucro_maximo = lucro
        preco_maximo = preco_real
        vendidos_maximo = ingressos_vendidos

    print(f"Preço do Ingresso: R${preco_real:.2f}, Ingressos Vendidos: {ingressos_vendidos}, Lucro: R${lucro:.2f}")

# Exibe o lucro máximo esperado, preço do ingresso e quantidade de ingressos vendidos
print(f"\nLucro Máximo Esperado: R${lucro_maximo:.2f}")
print(f"Preço do Ingresso para Lucro Máximo: R${preco_maximo:.2f}")
print(f"Quantidade de Ingressos Vendidos para Lucro Máximo: {vendidos_maximo}")

#7 questão:
# Inicializa a variável para contar as pessoas maiores de 18 anos
quantidade_maior_dezoito = 0

# Loop para receber a idade de 10 pessoas
for i in range(10):
    idade = int(input(f"Digite a idade da pessoa {i + 1}: "))
    
    if idade >= 18: