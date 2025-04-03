def insert2Mas(A, n, i, elem):
    # если вставлять уже некуда, пишем full
    if len(A) == n:
        print("full")

    # в цикле печатаем переносы элементов
    for j in range(n, i, -1):
        A[j] = A[j + 1]
        print(f"A[{j}] = A[{j - 1}]")

    # печатаем копирование элемента elem в нужное место
    A[i] = elem
    print(f'A[{i}] = {elem}')

n, i, elem = map(int, input().split())
A = list(map(int, input().split()))
insert2Mas(A, n, i, elem)