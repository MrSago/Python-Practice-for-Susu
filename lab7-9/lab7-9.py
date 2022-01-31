
def fun(q, ls):
    if (len(q)):
        ls.append(q.pop())
        fun(q, ls)
    else:
        return

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        q = [str(i) for i in f.readline()]
    ls = []
    fun(q, ls)
    with open("output.txt", "w") as f:
        for i in ls:
            f.write(i)

