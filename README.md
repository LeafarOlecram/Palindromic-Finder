# Palindromic Finder 
`README.md`:

Este projeto é um exemplo em **Python** para encontrar todos os palíndromos em uma string **sem espaços** e identificar o maior palíndromo encontrado.  
O algoritmo atual tem complexidade **O(n²)**, suficiente para frases curtas e médias.

````markdown
## 🚀 Como funciona
- Percorre a string analisando todas as substrings possíveis.
- Verifica se a substring é igual à sua versão invertida (`[::-1]`).
- Salva todos os palíndromos encontrados em uma lista.
- Retorna também o maior palíndromo identificado.

---

## 📂 Estrutura do código

```python3
def findpalindromic(stringTest):
    listStr = []  # Lista para salvar cada palíndromo encontrado.
    for i in range(len(stringTest)):
        # Primeiro laço percorre os índices iniciais.
        for j in range(len(stringTest), i+2, -1):
            # Segundo laço percorre os índices finais, procurando palíndromos
            # de no mínimo 3 caracteres.
            subStr = stringTest[i:j]
            if subStr == subStr[::-1]:
                listStr.append(subStr)
        if j == (i + 2):
            break
    if len(listStr) < 1:
        listStr.append('none')
    return listStr


def findBiggerPalindromic(subStr):
    bigPalindromic = ''
    for i in range(len(subStr)):
        if len(subStr[i]) >= len(bigPalindromic):
            bigPalindromic = subStr[i]
    if len(bigPalindromic) < 1:
        bigPalindromic = 'none'
    return bigPalindromic


# Início do programa:
string = ""
palindromic = findpalindromic(string)
print('Lista de palíndromos: ', palindromic)
print('Maior palíndromo encontrado: ', findBiggerPalindromic(palindromic))
````

---

## 🧪 Exemplos de teste

Strings de entrada e palíndromos identificados (mínimo 3 caracteres):

1. `fastlevelup` → level, eve
2. `goodnoonman` → noon
3. `redmadamcar` → madam, ada
4. `quickcivicx` → ickci, ckc, civic, ivi
5. `zenracecarz` → racecar, aceca, cec
6. `helloradarplanet` → radar, ada
7. `fastcivicturbojet` → tcivict, civic, ivi
8. `greenlevelstation` → level, eve, tat
9. `moonnoonwalkerx` → oonnoo, onno, noon
10. `quickmadamdriver` → madam, ada
11. `blueracecartrack` → racecar, aceca, cec, cartrac, artra, rtr
12. `coolrotorengine` → rotor, oto
13. `darkrefermirror` → refer, rkr, efe, ror
14. `skytenetmatrix` → tenet, ene
15. `boldannafoxrun` → anna
16. `stormkayakpoint` → kayak, aya
17. `nightredividerx` → redivider, edivide, divid, ivi
18. `zebrastatslevel` → stats, tat, level, eve
19. `wilddeifiedzone` → deified, eifie, ifi
20. `braverotatorjet` → rotator, otato, tat

---

## 📦 Requisitos

* Python 3.7 ou superior
* Nenhuma biblioteca externa é necessária

---

## ▶️ Como executar

Clone este repositório ou copie o código em um arquivo chamado `palindromic_finder.py`:

```bash
python palindromic_finder.py
```

Edite a variável `string` no código para testar diferentes frases.

---

## 📘 Referências

* [Palíndromos (Wikipedia)](https://pt.wikipedia.org/wiki/Pal%C3%ADndromo)

* [Documentação oficial Python](https://docs.python.org/3/)
