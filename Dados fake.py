from faker import Faker

fake = Faker('pt-BR')

nome = fake.name()
endereco = fake.address()
email = fake.email()

print(f'Nome: {nome}')
print(f'endereço: {endereco}')
print(f'email: {email}')
print('_'*30)

perfil = fake.profile()
for k, v in perfil.items():
    print(f'{k}: {v}')

