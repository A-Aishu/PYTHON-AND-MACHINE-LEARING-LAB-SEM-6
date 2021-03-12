def gcd(n,m):
    if n == 0:
        return m
    return gcd(m%n,n)

def lcm(n,m):
    return (n / gcd(n,m))*m

if__name__ == "__main__":
    n = int(input())
    m = int(input())
    print("The L.C.M.is",int(lcm(n,m)))
