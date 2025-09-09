# Esse é um exemplo de resolução para encontrar uma lista de palíndromos em uma frase sem
# espaços e qual o maior palíndromo encontrado. O algoritmo atual tem complexidade O(n²).
def findpalindromic(stringTest):
    listStr = [] # Lista para salvar cada palíndromo encontrado.
    for i in range(len(stringTest)):

        # Primeiro laço de repetição para fazer o indice i percorrer do
        # inicio até se aproximar do indice j.

        for j in range(len(stringTest), i+2, -1):

            # Segundo laço de repetição para fazer o indice j percorrer do final
            # até se aproximar do indice i. Ele para de executar quando o valor
            # de j é igual a ao i + 2. Assim o define que o algoritimo vai encontrar
            # palíndromos de tamanh mínimo de 3 caracteres.

            subStr = stringTest[i:j]
            # Recebe a subString de onde os indíces apontam
            # dentro da String recebida.

            if subStr == subStr[::-1]: # Verifica se elas são iguais mesmo após inverter.
                listStr.append(subStr) # Adiciona a lista de palíndromos encontrados.
        if j == (i + 2):
            break
    if len(listStr) < 1:

        # Verifica se a lista de palíndromos está vazia. Caso esteja adiciona
        # a String 'none'.

        listStr.append('none')
    return listStr

def findBiggerPalindromic(subStr): # Função para encontrar o maior palíndromo dentro da lista.
    bigPalindromic = ''
    for i in range(len(subStr)):
        # Laço de repetição para percorrer a String e comparar
        # cada palíndromo encontrado.
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

# Lista de palíndromos para testar e os resultados que se pode obter com palíndromos de no mínimo
# três (3) caracteres:
# 1. fastlevelup → contém level, eve
# 2. goodnoonman → contém noon
# 3. redmadamcar → contém madam, ada
# 4. quickcivicx → contém ickci, ckc, civic, ivi
# 5. zenracecarz → contém racecar, aceca, cec
# 6. helloradarplanet → contém radar, ada
# 7. fastcivicturbojet → contém tcivict, civic, ivi
# 8. greenlevelstation → contém level, eve, tat
# 9. moonnoonwalkerx → contém oonnoo, onno, noon
# 10. quickmadamdriver → contém madam, ada
# 11. blueracecartrack → contém racecar, aceca, cec, cartrac, artra, rtr
# 12. coolrotorengine → contém rotor, oto
# 13. darkrefermirror → contém refer, rkr, efe, ror
# 14. skytenetmatrix → contém tenet, ene
# 15. boldannafoxrun → contém anna
# 16. stormkayakpoint → contém kayak, aya
# 17. nightredividerx → contém redivider, edivide, divid, ivi
# 18. zebrastatslevel → contém stats, tat, level, eve
# 19. wilddeifiedzone → contém deified, eifie, ifi
# 20. braverotatorjet → contém rotator, otato, tat

# See PyCharm help at https://www.jetbrains.com/help/pycharm/