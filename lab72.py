def interpolSearch(A, elem):
    # если искомый элемент за границами диапазона,то делать нечего
    if not A:
        return []

    if elem < A[0] or elem > A[-1]:
        return None

    # определим верхнюю границу и вызовем рекурсивную функцию
    return interpolSearchRec(A, elem, 0, len(A) - 1, [])

def interpolSearchRec(A, elem, left, right, B):
    # если подмассив пустой ИЛИ elem за границами диапазона, то делать нечего
    if left > right:
        return B
    if elem < A[left] or elem > A[right]:
        return B
    # если левая и правая границы совпадают, то mid по формуле вычислять нельзя! (почему?)
    if A[left] == A[right]:
        B.append(A[left])
        return B
    # иначе - вычисляем mid по формуле
    try:
        mid = round(left + (elem - A[left]) * ((right - left) / (A[right] - A[left])))
        mid = max(left, min(mid, right))
    except ZeroDivisionError:
        mid = left
    B.append(A[mid])
    # выполняем сравнение и рекурсивный вызов на одной из частей
    if A[mid] == elem:
        return B
    elif A[mid] > elem:
        return interpolSearchRec(A, elem, left, mid - 1, B)
    else:
        return interpolSearchRec(A, elem, mid + 1, right, B)

"""elem = int(input())
A = list(map(int, input().split()))
print(" ".join(map(str, interpolSearch(A, elem))))"""