'''
* Escreva um programa em linha de comando para fazer questionário com o tema "Você está afim do seu melhor amigo?";
* Esse programa fará várias perguntas diferentes e aceitará apenas as entradas 'S' e 'N';
* Para cada pergunta respondida 'S', ele deve somar um ponto. Cada pergunta respondida 'N' ele não soma nada;
* Ao final da execução, o programa responderá o usuário de acordo com a soma dos pontos.
* A lista de perguntas é:
A) "Você já sonhou que seu melhor amigo era um unicórnio voando sobre arco-íris cor-de-rosa enquanto segurava um buquê de salsichas?"
B) "Você já se viu dançando a dança do frango em homenagem ao aniversário do seu melhor amigo, vestida de pinguim?"
C) "Se seu melhor amigo fosse um sorvete, ele seria o sorvete de pistache?"
D) "Você pensa em patos de borracha quando olha para o seu melhor amigo?"
E) "Você já escreveu um poema de amor épico para o seu melhor amigo usando apenas emojis de vegetais?"
F) "Você acha que seu melhor amigo seria um bom companheiro numa luta contra zumbis alienígenas usando almofadas como armas?"

* E a pontuação:
- De 0 a 2 pontos: você colocou seu melhor amigo na friendzone. O que é ótimo porque talvez ele seja apenas seu amigo
- De 3 a 4 pontos: Talvez haja amor, talvez seja hormônios. Vale a pena experimentar uns cinco minutos de trocação de beijo sem estragar a amizade.
- 5 ou mais pontos: É o amor /Que mexe com minha cabeça e me deixa assim/ Que faz eu pensar em você e esquecer de mim/ Que faz eu esquecer que a vida é feita pra
viver

'''
perguntas = ['Você já sonhou que seu melhor amigo era um unicórnio voando sobre arco-íris cor-de-rosa enquanto segurava um buquê de salsichas?',
             'Você já se viu dançando a dança do frango em homenagem ao aniversário do seu melhor amigo, vestida de pinguim?',
             'Se seu melhor amigo fosse um sorvete, ele seria o sorvete de pistache?',
             'Você pensa em patos de borracha quando olha para o seu melhor amigo?',
             'Você já escreveu um poema de amor épico para o seu melhor amigo usando apenas emojis de vegetais?',
             'Você acha que seu melhor amigo seria um bom companheiro numa luta contra zumbis alienígenas usando almofadas como armas?'
             ]
resposta_sim = 0
print('-'*20, 'Responda apensa com Sim ou Não', '-'*20)
for pergunta in perguntas:
    resposta = input(f'{pergunta}: ')
    if resposta == 's':
        resposta_sim += 1

if resposta_sim <= 2:
    print('você colocou seu melhor amigo na friendzone. O que é ótimo porque talvez ele seja apenas seu amigo')
elif resposta_sim >= 3 and resposta_sim <= 4:
    print('Talvez haja amor, talvez seja hormônios. Vale a pena experimentar uns cinco minutos de trocação de beijo sem estragar a amizade.')
else:
    print('É o amor /Que mexe com minha cabeça e me deixa assim/ Que faz eu pensar em você e esquecer de mim/ Que faz eu esquecer que a vida é feita pra viver')



print(resposta_sim)


def busca_binaria(lista: list):
    meio_lista = len(lista)/2
