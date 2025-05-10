def solve(A):
    A.sort()
    N = len(A)

    def chain_len(start):
        cnt = 1
        curr = A[start]
        for x in A[start+1:]:
            if x >= curr + 9:
                cnt += 1
                curr = x
        return cnt

    # 1) Найти K
    K = chain_len(0)

    # 2) Бинарным поиском найти максимально возможный старт
    lo, hi = 0, N-1
    best_i = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if chain_len(mid) >= K:
            best_i = mid
            lo = mid + 1
        else:
            hi = mid - 1

    # 3) Ответ: длина цепочки и размер самой маленькой коробки
    return K, A[best_i]

# Чтение из файла / тестирование
if __name__ == '__main__':
    data = list(map(int, open('26_21910.txt').read().split()))
    N, sizes = data[0], data[1:]
    k, smallest = solve(sizes)
    print(k, smallest)
