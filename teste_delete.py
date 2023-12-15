import requests

headers = {'Authorization': 'Token e8d3fff8b039a285c07d2eee2bb49851ff454678'}
url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'


resultado = requests.delete(url=f'{url_base_cursos}6/', headers=headers)

# Testando o código HTTP
assert resultado.status_code == 204

# print(resultado.text)

# Testando se o tamanho do conteúdo retorno é 0
assert len(resultado.text) == 0
