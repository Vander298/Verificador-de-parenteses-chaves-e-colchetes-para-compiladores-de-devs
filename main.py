"""
================================================================
VERIFICADOR DE PARENTESES/COLCHETES/CHAVES BALANCEADOS
================================================================

Autor do software: Vanderley Faria Renovato

PROBLEMA:
Editores de codigo, compiladores e interpretadores precisam
verificar se os simbolos de abertura e fechamento de uma
expressao ou trecho de codigo -- parenteses (), colchetes []
e chaves {} -- estao corretamente balanceados. Isso significa
que todo simbolo de abertura deve ter um fechamento
correspondente, na ordem certa (o ultimo simbolo aberto deve
ser o primeiro a ser fechado). Um codigo com simbolos mal
balanceados normalmente indica erro de sintaxe e pode causar
comportamento incorreto ou falhas de compilacao.

SOLUCAO:
O problema foi resolvido utilizando o TAD Pilha (estrutura
LIFO - Last In, First Out - "ultimo a entrar, primeiro a
sair"), implementada com lista (equivalente ao array do C).
A logica funciona da seguinte forma:

  1. O texto de entrada e percorrido caractere a caractere.
  2. Ao encontrar um simbolo de ABERTURA ( [ {, ele e
     empilhado (colocado no topo da pilha).
  3. Ao encontrar um simbolo de FECHAMENTO ) ] }, o programa
     desempilha o simbolo do topo e verifica se ele corresponde
     ao simbolo de abertura esperado. Se a pilha estiver vazia
     ou o simbolo nao corresponder, a expressao esta incorreta.
  4. Ao final do percurso, se a pilha estiver vazia, todos os
     simbolos foram corretamente fechados e a expressao esta
     BALANCEADA. Caso contrario, ha simbolos que abriram e
     nunca foram fechados, e a expressao esta NAO BALANCEADA.

A escolha da Pilha se justifica porque o problema exige
lembrar, na ordem inversa, quais simbolos foram abertos por
ultimo -- exatamente o comportamento LIFO da estrutura.
================================================================
"""

CAPACIDADE = 100

# ---------- TAD Pilha (lista, com limite de capacidade) ----------


class Pilha:
    """Pilha de caracteres implementada sobre uma lista Python,
    respeitando uma capacidade maxima (assim como o array em C)."""

    def __init__(self):
        self.itens = []

    def vazia(self):
        return len(self.itens) == 0

    def cheia(self):
        return len(self.itens) == CAPACIDADE

    def empilhar(self, c):
        """Empilha um caractere no topo. Retorna True se OK, False se pilha cheia."""
        if self.cheia():
            return False
        self.itens.append(c)
        return True

    def desempilhar(self):
        """Desempilha o caractere do topo.
        Retorna (True, caractere) se OK, (False, None) se pilha vazia."""
        if self.vazia():
            return False, None
        return True, self.itens.pop()


# ---------- Logica do problema ----------


def abertura_correspondente(fechamento):
    """Retorna o simbolo de abertura que combina com o simbolo de
    fechamento recebido. Ex: ')' -> '(', ']' -> '[' etc."""
    correspondencias = {')': '(', ']': '[', '}': '{'}
    return correspondencias.get(fechamento, '\0')


def eh_abertura(c):
    return c in '([{'


def eh_fechamento(c):
    return c in ')]}'


def verificar_balanceamento(texto):
    """
    Recebe uma expressao/trecho de codigo e verifica se os simbolos
    de abertura/fechamento estao corretamente balanceados.
    Retorna True se estiver balanceado, False caso contrario.
    """
    p = Pilha()

    for c in texto:
        if eh_abertura(c):
            p.empilhar(c)
        elif eh_fechamento(c):
            # Fechou um simbolo, mas a pilha esta vazia:
            # nao ha nada aberto para fechar.
            ok, topo = p.desempilhar()
            if not ok:
                return False

            # O que estava aberto nao combina com o que foi fechado
            # agora. Ex: abriu '(' mas fechou ']'.
            if topo != abertura_correspondente(c):
                return False
        # outros caracteres (letras, numeros, operadores) sao
        # ignorados: nao afetam o balanceamento

    # Se sobrou algo na pilha, ha simbolos que abriram e nunca
    # foram fechados.
    return p.vazia()


# ---------- Programa principal ----------


def main():
    print("=======================================")
    print(" VERIFICADOR DE PARENTESES BALANCEADOS")
    print("=======================================")
    print("Autor: Vanderley Faria Renovato")
    print("Data: 15/09/2026")
    print("O que foi feito: Programa em Python que usa o TAD Pilha")
    print("para verificar se ( ) [ ] { } de uma expressao")
    print("estao corretamente balanceados.")
    print("O que resolveu: identifica automaticamente erros")
    print("de sintaxe causados por simbolos abertos sem")
    print("fechamento, fechados sem abertura, ou fechados")
    print("na ordem errada.")
    print("=======================================\n")
    print("Digite uma expressao (ou 'sair' para encerrar):\n")

    while True:
        try:
            entrada = input("> ")
        except EOFError:
            break

        if entrada == "sair":
            break

        if verificar_balanceamento(entrada):
            print("Resultado: BALANCEADO (correto)\n")
        else:
            print("Resultado: NAO BALANCEADO (erro)\n")

    print("Encerrando o programa.")


if __name__ == "__main__":
    main()