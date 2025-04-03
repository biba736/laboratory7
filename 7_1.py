def binSearch(A, elem):
    # если искомый элемент за границами диапазона,то делать нечего
    if elem < A[0] or elem > A[-1]:
        return None

    # определим верхнюю границу и вызовем рекурсивную функцию
    return binSearchRec(A, elem, 0, len(A) - 1, [])


def binSearchRec(A, elem, left, right, B):
    # если подмассив пустой, то делать нечего
    if left > right:
        return B

    # определяем средний элемент
    mid = (left + right) // 2
    B.append(A[mid])

    # выполняем сравнение и рекурсивный вызов на одной из половин
    if A[mid] == elem:
        return B
    elif A[mid] > elem:
        return binSearchRec(A, elem, left, mid - 1, B)
    else:
        return binSearchRec(A, elem, mid + 1, right, B)


elem = int(input())
A = list(map(int, input().split()))
print(" ".join(map(str, binSearch(A, elem))))