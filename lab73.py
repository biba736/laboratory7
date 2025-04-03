def fibSearch(A, elem):
    # если искомый элемент за границами диапазона,то делать нечего
    if not A:
        return []

    if elem > A[-1] or elem < A[0]:
        return None

    # вычисляем нужное число Фибоначчи
    fibs = [0, 1]
    while fibs[-1] < len(A):
        fibs.append(fibs[-1] + fibs[-2])

    # вызываем рекурсивную функцию3
    return fibSearchRec(A, elem, 0, fibs[-2], fibs[-1], len(A), [])

def fibSearchRec(A, elem, left, fkm1, fk, n, B):
    # если подмассив пустой ИЛИ из одного элемента, который не равен elem, то делать нечего
    if fk == 0:
        return B
    if (fk == 1):
        B.append(A[left])
        return B
    # если подмассив из одного элемента, который равен elem, то возвращаем ответ и завершаемся
    # вычисляем (k-2)-е число Фибоначчи
    fkm2 = fk - fkm1
    # вычисляем mid - правый элемент первого подмассива (смотрим, чтобы он не выпал за границы)
    mid = min(left + fkm2 - 1, n - 1)
    B.append(A[mid])
    # выполняем сравнение и рекурсивный вызов на одной из частей
    if A[mid] == elem:
        return B
    elif A[mid] > elem:
        return fibSearchRec(A, elem, left, fkm1 - fkm2, fkm2, n, B)
    else:
        return fibSearchRec(A, elem, left + fkm2, fkm2, fkm1, n, B)

'''elem = int(input())
A = list(map(int, input().split()))
print(" ".join(map(str, fibSearch(A, elem))))'''