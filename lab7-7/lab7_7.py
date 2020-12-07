
def F(x):
	return (x**4 - 10)

def countRound(N):
	count = 0
	while (N < 1):
		N = N*10
		count += 1
	return (count)

def toFixed(num, digits=0):
	return (f"{num:.{digits}f}")

def recFun(a, b, eps):
	x = (a+b)/2
	if (F(x) == 0.0):
		return (x)

	if (F(a) * F(x) < 0.0):
		b = x
	elif (F(b) * F(x) < 0.0):
		a = x

	if (abs(b-a) > 2*eps):
		return (recFun(a, b, eps))
	return (x)


if __name__ == "__main__":
	a, b, eps = map(float, input().split())
	print("Корень уравнения x = %s" % toFixed(recFun(a, b, eps), countRound(eps)))
