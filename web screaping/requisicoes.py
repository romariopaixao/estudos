import requests
# Jogando a requisição atravaes do metodo get para a variavel response
response = requests.get('https://www.w3schools.com/python/python_strings.asp')

# Statuso do código, vai retornar algum daqueles status HTTPS
print('Status code ',response.status_code)
print('↓↓ Header ↓↓')
# Método para trazer o cabecario do site
print(response.headers)
#Método para trazer todo o conteudo html do site requistado
print('\n ↓↓ Content ↓↓')
print(response.content)
