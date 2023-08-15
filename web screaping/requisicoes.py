import requests
from bs4 import BeautifulSoup

response = requests.get('https://g1.globo.com')
# Jogando a requisição atravaes do metodo get para a variavel response

content = response.content
# Variavel contente recebe o conteudo HTML do site

site = BeautifulSoup(content, 'html.parser')
#Site recebe o conteudo do site, e converte para objeto. Segundo parametro indicando que é HTML

noticia = site.find('div', attrs={'class': 'feed-post-body'})
#HTML da noticia - Buca no site, pela tag dic com o atributo do dicionario acima

titulo = noticia.find('a', attrs={'class': 'feed-post-link'})
#HTML da do titulo da noticia - Buca na noticia, pela tag 'a' com o atributo do dicionario acima

subtitulo = noticia.find('a', attrs={'class': 'gui-color-primary gui-color-hover feed-post-body-title bstn-relatedtext'})
print(subtitulo.prettify()) #atributo prettify formata o texto para o padrao html
print('Titulo da noticia: ', titulo.text) #atributo text pega so oconteudo de dentro da tag

