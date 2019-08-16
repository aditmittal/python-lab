def fib(n):
    a=0
    b=1
    f=1
    for i in range (1,n+1):
        print(f)
        f = a + b
        a = b
        b = f
fib(7)
