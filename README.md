
# MultiMergeSort

Este é um projeto de implementação paralela do algoritmo Merge Sort utilizando a biblioteca `multiprocessing` do Python. O Merge Sort é um algoritmo eficiente de ordenação que é particionado em várias tarefas menores, permitindo que essas tarefas sejam executadas em paralelo para acelerar o processo de ordenação.

## Como Funciona

O código implementa a função `mergeSort` que divide recursivamente a lista em duas metades até que cada sublista contenha apenas um elemento. Em seguida, as sublistas são mescladas em ordem. A paralelização é alcançada usando a biblioteca `multiprocessing` para executar as chamadas recursivas em diferentes processos, acelerando o processo de ordenação.

## Requisitos

- Python 3.x

## Uso

1. Clone o repositório ou baixe o arquivo `multimerge.py`.

2. No terminal, navegue até o diretório onde o arquivo `multimerge.py` está localizado.

3. Execute o seguinte comando:

   ```bash
   python main.py
   ```

4. O programa imprimirá a lista desordenada e a lista ordenada usando o algoritmo MultiMergeSort.

## Exemplo de Saída

```
Given array is: [12, 11, 13, 5, 6, 7]
Sorted array is: [5, 6, 7, 11, 12, 13]
```
