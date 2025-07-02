a =int(input("digite um numero"))


def fatorial(N):
    if N < 0:
        print("nao é possivel fatoras")
    else:
        f = 1
        for i in range(1,N+1):
            f *= i
    print("o fatorial de {} igual a {}".format(N,f))
fatorial(a)
