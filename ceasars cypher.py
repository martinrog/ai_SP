def verschuiven(n,ch):
    print(ch[n:])
    print(ch[:n])
    return ch[n:] + ch[:n]

print(verschuiven(1,"Martin"))