A, B, C = input("세 정수를 입력하세요: ").split()
A = int(A)
B = int(B)
C = int(C)

if A >= B:
    if A >= C:
        if B >= C:
            result = B
        else:
            result = C
    else:
        result = A
elif B >= C:
    if A >= C:
        result = A
    else:
        result = C
else:
    if A >= B:
        result = A
    else:
        result = B

print(result)
