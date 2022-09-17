

i = []
for a in range(0,3):
    print("a "+ str(a))
    for b in range(a):
        print("b "+ str(b))
        print(str(a) + "," + str(b))
        i.append((a,b))
