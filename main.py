import multiprocessing

# Função para mesclar duas sub-listas ordenadas
def merge(arr, l, m, r):
    n1 = m - l + 1  # Tamanho da primeira metade
    n2 = r - m      # Tamanho da segunda metade

    L = arr[l : m + 1].copy()  # Cria uma cópia da primeira metade
    R = arr[m + 1 : r + 1].copy()  # Cria uma cópia da segunda metade

    i = j = 0  # Índices para percorrer L e R
    k = l  # Índice para percorrer o array final

    # Mescla os elementos de L e R de volta ao array original
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Adiciona quaisquer elementos restantes de L e R ao array
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# Função para executar o Merge Sort
def mergeSort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2

        # Cria processos para as chamadas recursivas usando multiprocessing
        process_left = multiprocessing.Process(target=mergeSort, args=(arr, l, m))
        process_right = multiprocessing.Process(target=mergeSort, args=(arr, m + 1, r))

        process_left.start()  # Inicia o processo da metade esquerda
        process_right.start()  # Inicia o processo da metade direita

        process_left.join()  # Espera pelo término do processo da metade esquerda
        process_right.join()  # Espera pelo término do processo da metade direita

        merge(arr, l, m, r)  # Mescla as duas metades ordenadas

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    arr_size = len(arr)

    print("Given array is:", arr)

    mergeSort(arr, 0, arr_size - 1)  # Chama a função de ordenação

    print("Sorted array is:", arr)
