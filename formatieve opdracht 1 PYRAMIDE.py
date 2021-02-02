def piramid():
    grootte = int(input("Hoe groot?"))
    pirm = ""
    f= 1
    for i in range(grootte):
        pirm += "*  "*f
        pirm += "\n"
        f+=1
    f= grootte-1
    for i in range(grootte,1,-1):
        pirm += "*  "*f
        pirm += "\n"
        f = f -1
    print(pirm)

piramid()