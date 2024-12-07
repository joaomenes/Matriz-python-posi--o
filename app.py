from typing import List

def move_zeros(zeroList: List[int]) -> List[int]:
    # Usando for comprehension, percorrer a lista encontrar as ocorrências de zero e adicionando em uma lista nova.
    novaList = [retirandoZero for retirandoZero in zeroList if retirandoZero == 0]

    while 0 in zeroList:
        zeroList.remove(0)
        
    semZeros = zeroList + novaList

    return semZeros  # Retornando sem o zero.


move_zeros([1, 0, 1, 2, 0, 1, 3])
