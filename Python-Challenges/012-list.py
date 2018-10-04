if __name__ == '__main__':
    n = int(input())

    l = []
    for _ in range(n):
        s = input().split()
        cmd = s[0]
        var = s[1:]
        if cmd !="print":
            cmd += "("+ ",".join(var) +")"
            eval("l."+cmd)
        else:
            print(l)
