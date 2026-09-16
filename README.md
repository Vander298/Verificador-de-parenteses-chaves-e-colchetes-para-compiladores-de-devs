# Verificador de Parênteses, Chaves e Colchetes

Programa em Python que verifica se os símbolos de abertura e fechamento — `()`, `[]` e `{}` — de uma expressão ou trecho de código estão corretamente balanceados. É o tipo de checagem que editores de código, compiladores e interpretadores fazem para detectar erros de sintaxe antes mesmo de tentar compilar ou executar o código.

## 📋 O problema

Para que uma expressão esteja sintaticamente correta, todo símbolo de abertura precisa ter um fechamento correspondente, na ordem certa — o último símbolo aberto deve ser o primeiro a ser fechado. Alguns exemplos:

| Expressão | Resultado |
|---|---|
| `(a + [b * c])` | ✅ Balanceado |
| `{[a, b), c}` | ❌ Não balanceado (fechamento fora de ordem) |
| `(a + b` | ❌ Não balanceado (abriu e nunca fechou) |
| `a + b)` | ❌ Não balanceado (fechou sem abrir) |

## 🧠 Solução

O problema é resolvido com uma **Pilha (Stack)** — estrutura de dados **LIFO** (*Last In, First Out*, "último a entrar, primeiro a sair"). A lógica é:

1. Percorrer o texto de entrada caractere a caractere.
2. Ao encontrar um símbolo de **abertura** (`(`, `[`, `{`), empilhar.
3. Ao encontrar um símbolo de **fechamento** (`)`, `]`, `}`), desempilhar o topo e verificar se ele corresponde ao fechamento esperado.
   - Se a pilha estiver vazia ou o símbolo não corresponder, a expressão está incorreta.
4. Ao final, se a pilha estiver vazia, todos os símbolos foram corretamente fechados — a expressão está **balanceada**. Caso contrário, sobraram símbolos abertos sem fechamento.

A Pilha é a estrutura ideal aqui porque o problema exige lembrar, na ordem inversa, quais símbolos foram abertos por último — exatamente o comportamento LIFO.

## 🚀 Como executar

Requer apenas Python 3 (nenhuma biblioteca externa é necessária).

```bash
python verificador_balanceamento.py
```

O programa entra em modo interativo:

```
=======================================
 VERIFICADOR DE PARENTESES BALANCEADOS
=======================================
Digite uma expressao (ou 'sair' para encerrar):

> (a + [b * c])
Resultado: BALANCEADO (correto)

> {[a, b), c}
Resultado: NAO BALANCEADO (erro)

> sair
Encerrando o programa.
```

## 📁 Estrutura do projeto

```
.
├── verificador_balanceamento.py   # Código-fonte principal
└── README.md                      # Este arquivo
```

## 🛠️ Detalhes técnicos

- **Estrutura de dados:** Pilha (`Pilha`), implementada com lista Python e capacidade máxima configurável.
- **Complexidade de tempo:** O(n), onde `n` é o tamanho da expressão — cada caractere é visitado uma única vez.
- **Complexidade de espaço:** O(n) no pior caso (expressão só com símbolos de abertura).

## ✍️ Autor

**Vanderley Faria Renovato**

## 📄 Licença

Este projeto está disponível para uso livre e educacional.
