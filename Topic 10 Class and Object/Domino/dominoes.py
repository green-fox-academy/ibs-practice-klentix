from Domino.domino import Domino

def initialize_dominoes():
    dominoes = []
    dominoes.append(Domino(5, 2))
    dominoes.append(Domino(4, 6))
    dominoes.append(Domino(1, 5))
    dominoes.append(Domino(6, 7))
    dominoes.append(Domino(2 ,4))
    dominoes.append(Domino(7, 1))
    return dominoes

dominoes = initialize_dominoes()
print(dominoes)
# You have the list of Dominoes
# Order them into one snake where the adjacent dominoes have the same numbers on their adjacent sides
# eg: [2, 4], [4, 3], [3, 5] ...

new_domino = []
new_domino.append(dominoes[0])
dominoes.remove(dominoes[0])
while len(dominoes) != 0:
    for i in dominoes:
        if new_domino[-1].values[1] == i.values[0]:
            new_domino.append(i)
            dominoes.remove(i)
print(dominoes)
print(new_domino)