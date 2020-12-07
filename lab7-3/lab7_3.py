
def gcd(A, B):
    if B == 0:
        return (A)
    return (gcd(B, A % B))


if __name__ == "__main__":
    A, B = map(int, input().split())
    with open("output.txt", "w") as f:
        f.write("НОД(%d,%d)=%d" % (A, B, gcd(A, B)))
