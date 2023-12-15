import requests

headers = {'Authorization': 'Token e8d3fff8b039a285c07d2eee2bb49851ff454678'}
url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'


curso_atualizado = {
    "titulo": "Novo Curso de Scrum 3",
    "url": "http://www.geekuniversity.com.br/ncs3"
}

# Buscando o curso com ID 6
# curso = requests.get(url=f'{url_base_cursos}6/', headers=headers)
# print(curso.json())


resultado = requests.put(url=f'{url_base_cursos}7/', headers=headers, data=curso_atualizado)


# Testando o código de status HTTP
assert resultado.status_code == 200

# Testando o título
assert resultado.json()['titulo'] == curso_atualizado['titulo']
