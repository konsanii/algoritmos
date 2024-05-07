def tem_igual(*args):
    for i in range(len(args)):
        n = args[i]
        for j in range(i+1, len(args)):
            if args[1]==args[j]:
                return True
    return False

print(tem_igual(1,3,6,8,9,8))