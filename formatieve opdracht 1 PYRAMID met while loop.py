def piramid():
    grootte = int(input("Hoe groot?"))
    pirm = ""
    f = 1
    while (f-1) != grootte:
        pirm += "*  " * f
        pirm += "\n"
        f += 1
    f = grootte - 1
    while (f+1) != 0:
        pirm += "*  " * f
        pirm += "\n"
        f = f - 1
    print(pirm)
piramid()