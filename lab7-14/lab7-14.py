
op_chars = "([{<"
end_chars = ")]}>"

stack = []

def fun(inList):
    cur_char = inList.pop(0)
    if (cur_char in op_chars):
        stack.append(cur_char)
        if (len(inList)):
            return (True & fun(inList))
        else:
            return (len(stack) == 0)

    if (len(stack)):
        last_char = stack[len(stack) - 1]
        if (op_chars.index(last_char) == end_chars.index(cur_char)):
            stack.pop()
            if (len(inList)):
                return (True & fun(inList))
            else:
                return (len(stack) == 0)
    else:
        return (False)

    return (len(stack) == 0)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        inList = [str(i) for i in f.readline()]

    if (inList.pop() == '.'):
        with open("output.txt", "w") as f:
            if (fun(inList)):
                f.write("YES")
            else:
                f.write("NO")

