def insertMas2Mas(A, n, i, B):
    # если вставлять уже некуда, пишем full
    k = len(B)
    if len(A) - n < k:
        print("full")
    # в цикле печатаем переносы элементов
    for j in range(n + k - 1, i + k - 1, -1):
        A[j] = A[j - k]
        print(f"A[{j}] = A[{j - k}]")

    # печатаем копирование элемента elem в нужное место
    for e in range(k):
        A[i + e] = B[e]
        print(f"A[{i + e}] = {B[e]}")


n, i = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
insertMas2Mas(A, n, i, B)