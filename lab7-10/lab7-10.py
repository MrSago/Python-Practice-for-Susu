
alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
nums = ['0','1','2','3','4','5','6','7','8','9']

def check(ls):
    symbol = ls.pop()

    if (len(ls)):
        if (symbol in alph or symbol in nums):
            return (True and check(ls))
        else:
            return (False)
    elif (symbol in alph):
        return (True)
    else:
        return (False)

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        str_list = [str(i) for i in f.readline()]
    
    if (str_list[-1] == '.'):
        str_list.pop()
        with open("output.txt", "w") as f:
            if (check(str_list)):
                f.write("TRUE")
            else:
                f.write("FALSE")

