
def recursiveFunction(N):
    if (N == 0 or N == 1):
        return (1)
    return (N * recursiveFunction(N-1))

def C(N, M):
    res = recursiveFunction(N) // (recursiveFunction(M) * recursiveFunction(N-M))
    return (res)
    
if __name__ == "__main__":
    N, M = map(int, input().split())
    print(C(N, M))

