import requests


# GET Avaliacoes

avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

# Acessando o código de status HTTTP
# print(avaliacoes.status_code)

# Acessando os dados da resposta
# print(avaliacoes.json())
# print(type(avaliacoes.json()))

# Acessando a quantidade de registros
# print(avaliacoes.json()['count'])

# Acessando a próxima página de resultados
# print(avaliacoes.json()['next'])

# Acessando os resultados desta página
# print(avaliacoes.json()['results'])
# print(type(avaliacoes.json()['results']))

# Aceessando o primeiro elemento da lista de resultados
# print(avaliacoes.json()['results'][0])

# Aceessando o último elemento da lista de resultados
# print(avaliacoes.json()['results'][-1])

# Acessando somente o nome da pessoa que fez a última avaliação
# print(avaliacoes.json()['results'][-1]['nome'])

# GET Avaliacao
# avaliacao = requests.get('http://localhost:8000/api/v2/avaliacoes/1/')
# print(avaliacao.json())

# GET Cursos
headers = {'Authorization': 'Token e8d3fff8b039a285c07d2eee2bb49851ff454678'}

cursos = requests.get(url='http://localhost:8000/api/v2/cursos/', headers=headers)

print(cursos.status_code)
print(cursos.json())