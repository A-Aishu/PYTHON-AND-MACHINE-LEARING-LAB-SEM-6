nterms = int(input())
n1, n2 =0, 1
count = 0
if nterms <=0:
    print("Please enter the postive integer")
elif nterms == 1:
    print("Fibonacci Sequence upto",nterms,":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 =nth
        count += 1
