import random

palavras = ['banana', 'melancia', 'laranja', 'limao', 'uva', 'abacaxi', 'manga']

def escolher_palavra(palavras):
    palavra = random.choice(palavras)
    return palavra

def exibir_palavra(palavra, letras_corretas):
    for letra in palavra:
        if letra in letras_corretas:
            print(letra, end=' ')
        else:
            print('*', end=' ')
    print()

def solicitar_letra(letras_digitadas):
    while True:
        letra = input('Digite uma letra: ').lower()
        if len(letra) != 1:
            print('Por favor, digite apenas uma letra.')
        elif letra in letras_digitadas:
            print('Você já digitou essa letra. Por favor, digite outra.')
        elif not letra.isalpha():
            print('Por favor, digite apenas letras.')
        else:
            return letra

def atualizar_palavra(palavra, letras_corretas, letra):
    for i in range(len(palavra)):
        if palavra[i] == letra:
            letras_corretas[i] = letra

def adicionar_parte_do_corpo(erros):
    partes_do_corpo = ['cabeça', 'tronco', 'braço esquerdo', 'braço direito', 'perna esquerda', 'perna direita']
    print('Você errou! Falta apenas', len(partes_do_corpo) - erros, 'partes para o enforcado.')
    print('  ________     ')
    print(' |        |    ')
    print(' |        ' + ('O' if erros >= 1 else ''))
    print(' |       ' + ('/|\\' if erros >= 3 else '') + (' |' if erros >= 2 else ''))
    print(' |        ' + ('|' if erros >= 4 else ''))
    print(' |       ' + ('/ \\' if erros >= 6 else '') + ('\\' if erros == 5 else ''))
    print(' |              ')
    print(' |              ')
    print('--------------')
    return erros + 1

def jogar():
    palavra = escolher_palavra(palavras)
    letras_corretas = ['_'] * len(palavra)
    letras_digitadas = []
    erros = 0

    while True:
        exibir_palavra(palavra, letras_corretas)
        letra = solicitar_letra(letras_digitadas)
        letras_digitadas.append(letra)

        if letra in palavra:
            atualizar_palavra(palavra, letras_corretas, letra)
        else:
            erros = adicionar_parte_do_corpo(erros)

        if erros == 6:
            print('Você perdeu! A palavra era', palavra)
            break
        elif '_' not in letras_corretas:
            print('Parabéns! Você adivinhou a palavra', palavra)
            break

if __name__ == '__main__':
    jogar()