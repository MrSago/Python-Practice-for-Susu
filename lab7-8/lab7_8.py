
def fun(ls, neg, pos):
	if (not len(ls)):
		return

	N = ls.pop()
	if (N < 0):
		neg.append(N)
		fun(ls, neg, pos)
	else:
		pos.append(N)
		fun(ls, neg, pos)


if __name__ == "__main__":
	with open("input.txt", "r") as f:
		ls = [int(i) for i in f.readline().split()]

	if (ls.pop() == 0):
		neg = []
		pos = []

		fun(ls, neg, pos)

		with open("output.txt", "w") as f:
			for i in neg:
				f.write(str(i) + ' ')
			for i in pos:
				f.write(str(i) + ' ')