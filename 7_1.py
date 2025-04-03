def binSearchRec(A, elem, left, right, B):
    if left > right:
        return -1
    mid = (left + right)//2
    B.append(A[mid])
    if A[mid] == elem:
        print(" ".join(map(str, B)))
    elif A[mid] > elem:
        return binSearchRec(A, elem, left, mid - 1, B)
    else:
        return binSearchRec(A, elem, mid + 1, right, B)

elem = int(input())
A = list(map(int, input().split()))
B = []
binSearchRec(A, elem, 0, len(A) - 1, B)