def_gcd_fun(n,m)
    if m==0:
        return n
    else:
        return gcd_fun(m,n%m)

if __name__ == "__main__":

    n = int(input())
    m = int(input())
    num = gcd_fun(n,m)
    print("The H.C.F.is",num)
    
