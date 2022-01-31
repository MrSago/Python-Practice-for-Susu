
def div(A, B):
    if (A > 0 and A >= B):
        return (1 + div(A-B, B))
    return (0)

if __name__ == "__main__":
    A, B = map(int, input().split())
    with open("output.txt", "w") as f:
        f.write("div(%d,%d)=%d" % (A, B, div(A, B)))

