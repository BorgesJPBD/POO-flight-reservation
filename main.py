from voo import Voo
from cliente import Cliente
from faker import Faker
import random

fake = Faker()

# Lista para guardar os voos
voos = []

# Criando 10 voos
for i in range(10):
    numero_voo = "A" + str(random.randint(100, 999)) + random.choice(["A", "B", "C"])
    origem = fake.city()
    destino = fake.city()
    preco = round(random.randint(500, 3000))
    
    # Tripulação com 3 pessoas
    tripulacao = [fake.name(), fake.name(), fake.name()]
    piloto = fake.name()

    # Criando o voo
    voo = Voo(numero_voo, origem, destino, preco, tripulacao, piloto)

    # Preenchendo os 250 assentos com clientes
    for assento in voo.assentos:
        nome = fake.name()
        cpf = fake.unique.ssn()
        telefone = fake.phone_number()
        endereco = fake.address()
        cliente = Cliente(nome, cpf, telefone, endereco)
        assento.reservar(cliente)

    # Adiciona o voo na lista
    voos.append(voo)

# Mostra 10 assentos aleatórios de cada voo
for voo in voos:
    print("===================================")
    print(f"Voo {voo.numero} - {voo.origem} -> {voo.destino} - Preço: R${voo.preco}")
    print("Tripulação:", ", ".join(voo.tripulacao))
    print("Piloto:", voo.piloto)
    print("Assentos aleatórios:")

    voo.assentos_aleatorios()
    print("===================================\n")